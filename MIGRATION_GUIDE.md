# Flask-Migrate Usage Guide

## Overview
Flask-Migrate is now set up for your project. It helps you manage database schema changes.

## Important Commands

### 1. Initialize migrations (Already done!)
```bash
flask --app main db init
```

### 2. Create a new migration (After changing models)
```bash
flask --app main db migrate -m "Description of changes"
```

### 3. Apply migrations to database
```bash
flask --app main db upgrade
```

### 4. Rollback last migration
```bash
flask --app main db downgrade
```

### 5. Show migration history
```bash
flask --app main db history
```

### 6. Show current migration version
```bash
flask --app main db current
```

## Workflow

1. **Make changes to your models** in `Database/models.py`
2. **Create a migration**: `flask --app main db migrate -m "Added new field"`
3. **Review the migration** in `migrations/versions/` folder
4. **Apply the migration**: `flask --app main db upgrade`

## Next Step

Run this command to apply the initial migration and create the users table:
```bash
flask --app main db upgrade
```

## Project Structure
- `main.py` - Flask app with database configuration
- `Database/models.py` - Database models
- `migrations/` - Migration files (auto-generated)
- `migrations/versions/` - Individual migration scripts
