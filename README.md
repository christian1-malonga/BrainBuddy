# BrainBuddy AI - Student Management System

A full-stack application with Django REST API backend and React frontend for student management and authentication.

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8+ with pip
- Node.js 16+ with npm
- Git

### 1. Backend Setup (Django)

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers channels

# Run database migrations (SQLite is used by default)
python manage.py migrate

# Start the Django development server
python manage.py runserver
```

The backend will run on: `http://localhost:8000`

### 2. Frontend Setup (React)

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install axios react-router-dom @heroicons/react

# Configure API endpoint
# Create .env file in FRONTEND directory with:
VITE_API_URL=http://localhost:8000/api

# Start the React development server
npm run dev
```

The frontend will run on: `http://localhost:5173`

## 🔑 Test Credentials

A test user has been created for you to test the login functionality:

**Login Credentials:**
- **Student Number:** `12345`
- **Password:** `testpass123`

**User Details:**
- Name: John Doe
- Email: test@student.com
- Faculty: Computer Science
- Department: Software Engineering

## 📱 How to Test

### Method 1: Login with Test User
1. Open `http://localhost:5173` in your browser
2. Click "Login to BrainBuddy"
3. Enter the test credentials:
   - Student Number: `12345`
   - Password: `testpass123`
4. Click "Login"
5. You should be redirected to the Dashboard

### Method 2: Register New User
1. Open `http://localhost:5173` in your browser
2. Click "Register" 
3. Fill out the registration form with your details
4. Click "Create an account"
5. You'll be automatically logged in and redirected to the Dashboard

## 🏗️ Architecture

### Backend (Django REST API)
- **Framework:** Django 5.2 with Django REST Framework
- **Authentication:** JWT tokens using djangorestframework-simplejwt
- **Database:** SQLite (for easy setup)
- **CORS:** Configured for React frontend

**API Endpoints:**
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - Get user profile (requires authentication)
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Frontend (React)
- **Framework:** React 18 with Vite
- **Styling:** Tailwind CSS
- **State Management:** React Context (useAuth hook)
- **Authentication:** JWT token storage in localStorage
- **Components:** Modular UI components with reusable Button, Input, Card components

## 🔐 Authentication Flow

1. **Registration:** User fills form → Data sent to Django → JWT tokens returned → Auto-login
2. **Login:** User enters credentials → Django validates → JWT tokens returned → Dashboard access
3. **Token Validation:** On app load, stored token is validated with backend
4. **Protected Routes:** Dashboard requires valid authentication
5. **Logout:** Tokens removed from localStorage, user logged out

## 🎨 Features

### Backend Features
- Custom Student user model with student-specific fields
- JWT authentication with refresh tokens
- CORS enabled for cross-origin requests
- RESTful API design
- Password validation and hashing

### Frontend Features
- Modern, responsive UI with dark theme
- Real-time form validation
- Error handling and user feedback
- Protected routing with authentication checks
- Token-based authentication with auto-refresh
- Loading states and user feedback

### Dashboard Features
- Welcome message with user's name
- Statistics cards (mock data for demonstration)
- Recent activity tracking
- Quick action buttons
- Logout functionality

## 🛠️ Development Notes

### Backend Configuration
- Database changed from PostgreSQL to SQLite for easier setup
- JWT authentication configured with custom serializer
- CORS configured to allow requests from React frontend
- Custom user model extends Django's AbstractUser

### Frontend Configuration
- Vite configured for React development
- Tailwind CSS for utility-first styling
- Authentication context provides global auth state
- API calls configured to connect with Django backend

## 🔧 Troubleshooting

### Common Issues

1. **Backend won't start:**
   - Ensure all Python packages are installed: `pip install django djangorestframework djangorestframework-simplejwt django-cors-headers channels`
   - Run migrations: `python manage.py migrate`

2. **Frontend won't start:**
   - Install dependencies: `npm install`
   - Clear cache: `npm run dev --force`

3. **Login doesn't work:**
   - Ensure backend is running on port 8000
   - Check browser console for CORS errors
   - Verify test credentials: Student Number `12345`, Password `testpass123`

4. **CORS errors:**
   - Backend includes CORS headers for localhost:5173
   - Make sure both servers are running on correct ports

### API Testing
You can test API endpoints directly using curl or Postman:

```bash
# Register new user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@test.com",
    "first_name": "Jane",
    "last_name": "Smith",
    "student_number": "67890",
    "faculty": "Engineering",
    "department": "Mechanical Engineering",
    "password": "newpass123"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "student_number": "12345",
    "password": "testpass123"
  }'
```

## 📄 Project Structure

```
AI CR7/
├── BACKEND/
│   ├── accounts/          # User authentication app
│   │   ├── models.py      # Student user model
│   │   ├── serializers.py # JWT and user serializers
│   │   ├── views.py       # API endpoints
│   │   └── urls.py        # URL routing
│   ├── school_system/     # Django project settings
│   │   ├── settings.py    # Project configuration
│   │   └── urls.py        # Main URL routing
│   └── manage.py          # Django management script
├── FRONTEND/
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom React hooks (useAuth)
│   │   └── utils/         # Utility functions
│   ├── package.json       # Node.js dependencies
│   └── vite.config.js     # Vite configuration
└── README.md              # This file
```

Now you're ready to explore the full-stack authentication system! 🎉
