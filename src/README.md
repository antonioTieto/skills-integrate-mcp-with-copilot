# Mergington High School Activities API

A FastAPI application that allows students to view and sign up for extracurricular activities. Now features persistent database storage using SQLite and SQLAlchemy!

## Features

- ✅ View all available extracurricular activities
- ✅ Sign up for activities
- ✅ **NEW**: Persistent data storage (SQLite database)
- ✅ Data survives server restarts
- ✅ Activity capacity management

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will automatically:
- Initialize the SQLite database
- Create all necessary tables
- Populate initial activities data

### 3. Access the Application

- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Documentation**: http://localhost:8000/redoc

### 4. Database Location

The SQLite database file is created at:
```
src/activities.db
```

## Architecture

### Technology Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

### Data Models
The application uses two main database tables:
1. **Activity** - Stores activity information
2. **Participant** - Stores student information

See [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) for detailed data model documentation.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/activities` | Get all activities with participant counts |
| POST | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up a student for an activity |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister a student from an activity |

## Data Model

All data is now persisted in SQLite database, which means:
- ✅ Data survives server restarts
- ✅ Multiple concurrent users supported
- ✅ Activity capacity limits enforced
- ✅ No data loss

**Activities** - Stores activity information:
- Name (unique)
- Description
- Schedule
- Maximum participants
- List of enrolled students

**Participants** - Stores student information:
- Email (unique)
- Activities enrolled in
- Enrollment timestamps

## Database Management

### Initialize Database
On first run, the database automatically initializes with all tables and initial data.

### Reset Database
To clear and reinitialize:
```bash
rm src/activities.db
python app.py
```

### Backup Database
```bash
cp src/activities.db src/activities.db.backup
```

## Documentation

For more details on the database migration and architecture, see [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md).
