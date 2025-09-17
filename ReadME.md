# SaaS Template FastAPI - Quick Start Guide

## 🚀 Commands to Run the Server

### When Opening This Project for the First Time:

```bash
# 1. Navigate to project directory
cd path/to/SaaS-Template-FastAPI-

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Start the server
uvicorn src.app.main:app --reload
```

### When Opening This Project Again (After First Setup):

```bash
# 1. Navigate to project directory
cd path/to/SaaS-Template-FastAPI-

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Start the server
uvicorn src.app.main:app --reload
```

## 🌐 Access Your Application

- **Main API**: http://localhost:8000/
- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

## ✅ What's Already Configured

- ✅ **Database**: SQLite (no setup required)
- ✅ **Environment Variables**: All configured with secure defaults
- ✅ **Dependencies**: All packages installed and compatible
- ✅ **Migrations**: Database tables created and ready
- ✅ **Authentication**: JWT system ready
- ✅ **Email System**: Configured (update credentials in .env if needed)

## 🔧 Environment Variables (Optional Updates)

Edit `.env` file if you want to customize:

```bash
# Database (SQLite - no changes needed)
DB_NAME=saas_template
DB_USERNAME=postgres
DB_PASSWORD=password

# Email (update with your credentials)
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

# Frontend URL (update if different)
FRONTEND_URL=http://localhost:3000
```

## 🛠️ Additional Commands

```bash
# Run tests
python -m pytest

# Check database migrations
alembic current

# Apply new migrations (if any)
alembic upgrade head

# Deactivate virtual environment
deactivate
```

## 🎯 That's It!

Your SaaS Template FastAPI server is ready to use. Just run the 3 commands above and visit http://localhost:8000/docs to explore the API!