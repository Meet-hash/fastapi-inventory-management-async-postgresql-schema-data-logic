# Inventory Management Async PostgreSQL Task

## Task Overview
StockSpace is launching an inventory platform using FastAPI. The API's routing and endpoint scaffolding for adding and listing products is complete. Your job is to deliver a robust PostgreSQL schema to store products and to implement the asynchronous data-access logic for these endpoints. Effective database design is crucial because product volume and warehouse performance directly affect StockSpace's business.

## Guidance
- The FastAPI routing (`main.py`) and request/response models are already scaffolded.
- Complete the PostgreSQL database schema in `schema.sql` and implement SQLAlchemy models and async logic in `models.py` and `crud.py`.
- Use `run.sh` to build the environment and apply your schema using Docker Compose.

## Objectives
- Design a normalized `products` table, including primary keys, appropriate data types, uniqueness constraints, and relevant indexes.
- Implement the SQLAlchemy model that matches your schema, supporting async queries for product creation and product listing.
- Write the async-compatible DB logic so the provided endpoints can store and fetch product records properly from PostgreSQL, using best practices for async database connections.
- Ensure that all fields (name, description, price, quantity, and created_at) are accurately managed in the schema and FastAPI code integration.

## How to Verify
- After running `run.sh`, test the `/products/` POST endpoint to add new products and confirm records appear in the database.
- Use the `/products/` GET endpoint to retrieve a list of all products and verify full, correct data is returned from the database.
- Attempt adding a duplicate product name; verify the unique constraint prevents this.
- Examine the PostgreSQL table in a client (e.g., pgAdmin) to confirm schema, indexes, and that data is stored as expected.