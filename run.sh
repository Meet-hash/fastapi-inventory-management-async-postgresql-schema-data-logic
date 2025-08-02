#!/bin/bash
set -e

echo "Starting Docker containers..."
docker-compose up -d --build

until docker exec $(docker-compose ps -q db) pg_isready -U stockuser -d stockdb; do
  echo "Waiting for Postgres..."
  sleep 2
done
echo "Postgres is ready."

if [ -f schema.sql ]; then
  echo "Applying schema.sql to DB..."
  cat schema.sql | docker exec -i $(docker-compose ps -q db) psql -U stockuser -d stockdb
fi

echo "Installing Python dependencies..."
docker exec $(docker-compose ps -q fastapi) pip install -r /code/requirements.txt

echo "Setup complete! FastAPI running at http://localhost:8001"
