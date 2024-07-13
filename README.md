# product_service

This service manages products within the ecommerce platform.

## Project Overview

The `product_service` handles CRUD operations for products. It interacts with the `auth_service` for authentication and authorization using JSON Web Tokens (JWT).

## Setup Instructions

### Normal Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/ankitjhunjhunwala03/product_service/tree/main
   cd product_service
   ```

2. **Setup virtual environment (optional but recommended)**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   cp .env.example .env
   nano .env  # Edit with appropriate values
   ```

   Ensure to set up variables like `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `AUTH_SERVICE_URL`, and any specific settings required for your setup. `AUTH_SERVICE_URL` should point to the base URL of your `auth_service`.

5. **Run migrations (if applicable)**

   ```bash
   python manage.py migrate
   ```

6. **Start the server**

   ```bash
   python manage.py runserver
   ```

   The product service should now be running at `http://localhost:8001`.

### Docker Compose Setup

Ensure you have Docker and Docker Compose installed.

1. **Build and start the service**

   ```bash
   # Navigate to the project directory
   cd product_service
   
   # Build and start the services
   docker-compose up --build product_service
   ```

### Kubernetes Setup

Ensure you have `kubectl` configured and a Kubernetes cluster running.

1. **Apply the Kubernetes configurations**

   ```bash
   # Navigate to the Kubernetes directory
   cd product_service/kubernetes
   
   # Apply the Kubernetes configurations
   kubectl apply -f .
   ```

## Usage

### Endpoints

- **Create Product**: `/api/products/create/`
  - Method: POST
  - Payload: `name`, `description`, `price`, etc.
  - Description: Create a new product (requires authentication).
  
- **Update Product**: `/api/products/<product_id>/update/`
  - Method: PUT
  - Payload: `name`, `description`, `price`, etc.
  - Description: Update an existing product (requires authentication).
  
- **List Products**: `/api/products/`
  - Method: GET
  - Description: List all products.
  
- **Retrieve Product**: `/api/products/<product_id>/`
  - Method: GET
  - Description: Retrieve details of a specific product.
  
### Authentication

All endpoints are protected and require a valid JWT token obtained from the `auth_service`. Include the token in the `Authorization` header of your requests:

```
Authorization: Bearer <token>
```