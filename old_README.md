# SaaS Template FastAPI

A complete FastAPI-based SaaS template with authentication, organization management, and email functionality.

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Git

### 1. Clone and Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd SaaS-Template-FastAPI-

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
# Copy environment template
copy .example.env .env

# Edit .env file with your settings:
# - Update DB_PASSWORD (if using PostgreSQL)
# - Update MAIL_USERNAME and MAIL_PASSWORD for email functionality
# - Other settings have good defaults
```

### 4. Database Setup
```bash
# Apply database migrations (creates SQLite database automatically)
alembic upgrade head
```

### 5. Start the Server
```bash
# Start FastAPI server with auto-reload
uvicorn src.app.main:app --reload
```

## 📋 Complete Command Sequence

Here's the exact sequence to run when opening this project:

```bash
# 1. Navigate to project directory
cd path/to/SaaS-Template-FastAPI-

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Start the server
uvicorn src.app.main:app --reload
```

That's it! The server will be running at http://localhost:8000

## 🌐 Access Points

- **API Base URL:** http://localhost:8000
- **Interactive API Docs:** http://localhost:8000/docs
- **ReDoc Documentation:** http://localhost:8000/redoc

## 🗄️ Database

- **Type:** SQLite (no setup required)
- **File:** `saas_template.db` (auto-created)
- **Migrations:** Applied automatically with `alembic upgrade head`

## ⚙️ Environment Variables

Key variables in `.env` file:

```env
# Database (SQLite - no changes needed)
DB_NAME=saas_template
DB_USERNAME=postgres
DB_PASSWORD=password
DB_HOSTNAME=localhost
DB_PORT=5432

# Authentication (auto-generated secure keys)
ACCESS_SECRET_KEY=your_generated_key
REFRESH_SECRET_KEY=your_generated_key

# Email (update with your credentials)
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_FROM=your_email@gmail.com
```

## 🛠️ Development Commands

```bash
# Run tests
pytest

# Format code
black .

# Check code style
black --check .

# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## 📁 Project Structure

```
src/
├── app/                 # Main application
│   ├── main.py         # FastAPI app entry point
│   ├── config.py       # Configuration settings
│   ├── database.py     # Database connection
│   └── utils/          # Utility functions
├── auth/               # Authentication module
├── organization/       # Organization management
├── migrations/         # Database migrations
└── tests/             # Test files
```

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Use different port
   uvicorn src.app.main:app --reload --port 8001
   ```

2. **Database connection issues:**
   ```bash
   # Reset database
   rm saas_template.db
   alembic upgrade head
   ```

3. **Package installation issues:**
   ```bash
   # Upgrade pip first
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 🚀 Features

- ✅ User Authentication (JWT)
- ✅ Organization Management
- ✅ Email Verification
- ✅ Multi-tenant Architecture
- ✅ SQLite Database (no setup required)
- ✅ Auto-generated API Documentation
- ✅ Database Migrations
- ✅ Password Hashing
- ✅ CORS Support

## 📝 API Endpoints

- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/org/create` - Create organization
- `GET /api/v1/org/list` - List organizations

## 🎯 Next Steps

1. Update email credentials in `.env`
2. Customize authentication settings
3. Add your business logic
4. Deploy to production

---

**Happy Coding! 🚀**