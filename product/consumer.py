# import sys, os
#

# def setup():
#     sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#     module = os.path.split(os.path.dirname(__file__))[-1]
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_service.settings".format(module))
#     import django
#     django.setup()
#
#
# setup()

from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaError
import json
from product.models import Product
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        conf = {
            'bootstrap.servers': settings.KAFKA_URL,
            'group.id': "product-group",
            'auto.offset.reset': 'earliest'
        }
        consumer = Consumer(**conf)
        consumer.subscribe(['product_updates'])

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            message = json.loads(msg.value().decode('utf-8'))
            self.update_product_quantity(message)

    def update_product_quantity(self, message):
        product_id = message['product_id']
        quantity = message['quantity']

        try:
            product = Product.objects.get(id=product_id)
            product.quantity += int(quantity)
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated product {product_id}'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Product {product_id} does not exist'))
