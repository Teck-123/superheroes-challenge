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

## API Endpoints

### Heroes

#### GET /heroes
Returns a list of all heroes.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

#### GET /heroes/:id
Returns a specific hero with their powers.

**Response (Success):**
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": "Hero not found"
}
```

### Powers

#### GET /powers
Returns a list of all powers.

**Response:**
```json
[
  {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
]
```

#### GET /powers/:id
Returns a specific power.

**Response (Success):**
```json
{
  "description": "gives the wielder super-human strengths",
  "id": 1,
  "name": "super strength"
}
```

**Response (Not Found):**
```json
{
  "error": "Power not found"
}
```

#### PATCH /powers/:id
Updates a power's description.

**Request Body:**
```json
{
  "description": "Valid Updated Description"
}
```

**Response (Success):**
```json
{
  "description": "Valid Updated Description",
  "id": 1,
  "name": "super strength"
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Description must be at least 20 characters long"]
}
```

### Hero Powers

#### POST /hero_powers
Creates a new hero-power relationship.

**Request Body:**
```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

**Response (Success):**
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Strength must be one of: Strong, Weak, Average"]
}
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