# Superheroes Challenge API

A Flask REST API for managing superheroes and their powers.

## Features

- CRUD operations for heroes and powers
- Many-to-many relationship between heroes and powers through HeroPower
- Data validation and error handling
- JSON serialization with proper relationship handling

## Setup

1. Install dependencies:
```bash
pipenv install
pipenv shell
```

2. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

3. Seed the database:
```bash
python seed.py
```

4. Run the application:
```bash
python app.py
```

## Data Models

### Hero
- `id`: Integer (Primary Key)
- `name`: String (Required)
- `super_name`: String (Required)

### Power
- `id`: Integer (Primary Key)
- `name`: String (Required)
- `description`: Text (Required, min 20 characters)

### HeroPower
- `id`: Integer (Primary Key)
- `strength`: String (Required, must be 'Strong', 'Weak', or 'Average')
- `hero_id`: Integer (Foreign Key)
- `power_id`: Integer (Foreign Key)

## Validations

- **Power description**: Must be present and at least 20 characters long
- **HeroPower strength**: Must be one of 'Strong', 'Weak', or 'Average'

## Testing

Use the provided Postman collection to test all endpoints. Import `challenge-2-superheroes.postman_collection.json` into Postman to run the complete test suite.