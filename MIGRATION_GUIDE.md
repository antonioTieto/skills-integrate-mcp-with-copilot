# Database Migration Guide

## Overview

This update migrates the Mergington High School Activities API from in-memory storage to persistent SQLite database storage using SQLAlchemy ORM.

## What Changed

### ✅ Before (In-Memory)
- All data stored in a Python dictionary
- Data lost on server restart
- No data persistence
- Limited scalability

### ✅ After (Persistent Database)
- Data stored in SQLite database (`activities.db`)
- All data persists across server restarts
- Proper data models with relationships
- Ready for future cloud migrations
- Better performance for larger datasets

## Files Added

1. **`database.py`** - SQLAlchemy configuration and session management
2. **`models.py`** - Database models for Activity and Participant
3. **`init_db.py`** - Database initialization and initial data population

## Files Modified

1. **`app.py`** - Updated to use database instead of in-memory storage
2. **`requirements.txt`** - Added SQLAlchemy dependency

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize Database
The database is automatically initialized when the application starts:
```bash
python app.py
```

On first run:
- Database file (`activities.db`) is created
- All tables are created
- Initial activities data is populated

### 3. Verify Setup
The database file should appear in the `src/` directory:
```bash
ls -la src/activities.db
```

## Data Model

### Activity Table
```
- id: Integer (Primary Key)
- name: String (Unique)
- description: String
- schedule: String
- max_participants: Integer
- created_at: DateTime
- updated_at: DateTime
- participants: Many-to-Many relationship with Participant
```

### Participant Table
```
- id: Integer (Primary Key)
- email: String (Unique)
- created_at: DateTime
- activities: Many-to-Many relationship with Activity
```

### Association Table
```
- activity_participants: Tracks many-to-many relationship
  - activity_id (Foreign Key)
  - participant_email (Foreign Key)
```

## API Compatibility

The API endpoints remain identical to ensure backward compatibility:

| Method | Endpoint | Status |
|--------|----------|--------|
| GET | `/activities` | ✅ Works the same |
| POST | `/activities/{activity_name}/signup` | ✅ Works the same |
| DELETE | `/activities/{activity_name}/unregister` | ✅ Works the same |

## Backup & Recovery

### Backup Database
```bash
# Copy the database file
cp src/activities.db src/activities.db.backup
```

### Restore from Backup
```bash
# Restore the database
cp src/activities.db.backup src/activities.db
```

### Reset Database
```bash
# Delete the existing database (will be recreated on next startup)
rm src/activities.db
```

## Future Enhancements

This persistent database foundation enables:
- ✅ Role-based access control
- ✅ Full event lifecycle management
- ✅ Attendance tracking
- ✅ Financial management
- ✅ Cloud migrations (Firebase, PostgreSQL, etc.)

## Troubleshooting

### Database Lock Error
If you see "database is locked", ensure only one instance of the app is running.

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Data Not Persisting
Check that `src/activities.db` file exists and has write permissions.

---

**Next Steps:** With persistent storage in place, the next priority feature is implementing Role-Based Access Control (Issue #21).
