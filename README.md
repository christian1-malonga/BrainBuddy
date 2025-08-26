# BrainBuddy AI - Student Management System

![BrainBuddy AI](https://img.shields.io/badge/BrainBuddy-AI--Powered%20Education-blueviolet)
![Django](https://img.shields.io/badge/Django-5.2-green)
![React](https://img.shields.io/badge/React-18-blue)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A full-stack AI-powered student management system built with Django REST Framework backend and React frontend. BrainBuddy AI provides a modern, secure platform for student authentication, profile management, and academic tracking.

## 🚀 Live Demo

**Frontend**: http://localhost:5173  
**Backend API**: http://localhost:8000/api  
**Admin Panel**: http://localhost:8000/admin

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [API Documentation](#-api-documentation)
- [Authentication Flow](#-authentication-flow)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## ✨ Features

### Backend (Django REST Framework)
- **Custom Student Model**: Extended Django user model with student-specific fields
- **JWT Authentication**: Secure token-based authentication with refresh capability
- **RESTful API Design**: Clean, consistent API endpoints following REST principles
- **CORS Configuration**: Properly configured for frontend-backend communication
- **Database Abstraction**: SQLite for development (easily switchable to PostgreSQL)
- **Admin Interface**: Django admin for data management

### Frontend (React)
- **Modern UI/UX**: Responsive design with Tailwind CSS
- **Authentication Context**: Global state management for user sessions
- **Protected Routes**: Automatic redirect for unauthenticated users
- **Form Validation**: Real-time input validation with user feedback
- **Error Handling**: Comprehensive error handling and user notifications
- **Component Library**: Reusable UI components (Button, Input, Card, etc.)

### Dashboard Features
- **Personalized Welcome**: Dynamic greeting with user information
- **Statistics Overview**: Visual data representation (mock data)
- **Activity Tracking**: Recent user activity timeline
- **Quick Actions**: Shortcut to common tasks
- **Profile Management**: User profile viewing and editing

## 🏗 Architecture

```
BrainBuddy AI Architecture:
┌─────────────────┐    HTTP Requests    ┌────────────────────┐
│   React Frontend│ ◄─────────────────► │ Django REST API    │
│   (localhost:5173)  JWT Authentication  (localhost:8000)   │
└─────────────────┘                     └────────────────────┘
         │                                          │
         │                                          │
         ▼                                          ▼
┌─────────────────┐                     ┌────────────────────┐
│   Local Storage │                     │   SQLite Database  │
│   (JWT Storage) │                     │   (Django ORM)     │
└─────────────────┘                     └────────────────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.8+ with pip
- Node.js 16+ with npm
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd BrainBuddy-AI
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (optional for admin access)
python manage.py createsuperuser

# Start the Django development server
python manage.py runserver
```

The backend will be available at http://localhost:8000

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install Node.js dependencies
npm install

# Configure environment variables
cp .env.example .env
# Edit .env file with your API URL: VITE_API_URL=http://localhost:8000/api

# Start the React development server
npm run dev
```

The frontend will be available at http://localhost:5173

## 🔑 Authentication & Test Credentials

### Default Test User
A test user is pre-configured for demonstration:

| Field | Value |
|-------|-------|
| Student Number | 12345 |
| Password | testpass123 |
| Name | John Doe |
| Email | test@student.com |
| Faculty | Computer Science |
| Department | Software Engineering |

### Registration
New users can register through the frontend interface. The system validates:
- Unique student number and email
- Password strength requirements
- Faculty/department validity

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new student | No |
| POST | `/api/auth/login/` | Login user | No |
| POST | `/api/auth/token/refresh/` | Refresh JWT token | No |
| GET | `/api/auth/profile/` | Get user profile | Yes |
| PUT | `/api/auth/profile/` | Update user profile | Yes |

### Example API Usage

```bash
# Register a new user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "first_name": "Alice",
    "last_name": "Johnson",
    "student_number": "54321",
    "faculty": "Engineering",
    "department": "Electrical Engineering",
    "password": "securepassword123"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "student_number": "12345",
    "password": "testpass123"
  }'

# Get profile (with JWT token)
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer <your_access_token>"
```

## 🔐 Authentication Flow

1. **Registration**: User submits details → Django creates user → Returns JWT tokens
2. **Login**: User credentials verified → JWT tokens generated → Stored in localStorage
3. **API Requests**: Access token included in Authorization header
4. **Token Refresh**: Before token expiration, frontend automatically requests new token
5. **Logout**: Tokens removed from localStorage

## 📁 Project Structure

```
BrainBuddy-AI/
├── backend/                          # Django backend
│   ├── accounts/                     # Authentication app
│   │   ├── models.py                 # Custom Student model
│   │   ├── serializers.py            # User and token serializers
│   │   ├── views.py                  # API views
│   │   ├── urls.py                   # App URL routes
│   │   └── admin.py                  # Admin configuration
│   ├── school_system/                # Django project
│   │   ├── settings.py               # Project settings
│   │   ├── urls.py                   # Main URL routing
│   │   └── wsgi.py                   # WSGI configuration
│   ├── requirements.txt              # Python dependencies
│   └── manage.py                     # Django management script
├── frontend/                         # React frontend
│   ├── src/
│   │   ├── components/               # Reusable UI components
│   │   │   ├── ui/                   # Basic components (Button, Input, etc.)
│   │   │   ├── layout/               # Layout components
│   │   │   └── auth/                 # Authentication components
│   │   ├── pages/                    # Page components
│   │   │   ├── Auth/                 # Login/Register pages
│   │   │   ├── Dashboard/            # Dashboard pages
│   │   │   └── Error/                # Error pages
│   │   ├── hooks/                    # Custom React hooks
│   │   │   └── useAuth.js            # Authentication context
│   │   ├── utils/                    # Utility functions
│   │   │   ├── api.js                # API communication
│   │   │   └── auth.js               # Authentication helpers
│   │   ├── App.jsx                   # Main App component
│   │   └── main.jsx                  # Application entry point
│   ├── package.json                  # Node.js dependencies
│   ├── vite.config.js                # Vite configuration
│   └── .env                          # Environment variables
└── README.md                         # This file
```

## 🧪 Testing

### Backend Testing
```bash
cd backend
python manage.py test
```

### Frontend Testing
```bash
cd frontend
npm test
```

### Manual Testing
1. **Registration Test**: Create a new user account
2. **Login Test**: Authenticate with test credentials
3. **Profile Access**: Verify profile data retrieval
4. **Protected Route**: Attempt to access dashboard without authentication
5. **Logout Test**: Verify token removal and redirect

## 🚀 Deployment

### Backend Deployment (Example: Heroku)
```bash
# Add PostgreSQL database
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here

# Deploy
git subtree push --prefix backend heroku main
```

### Frontend Deployment (Example: Vercel)
```bash
# Build the project
npm run build

# Deploy to Vercel
npm i -g vercel
vercel --prod
```

### Environment Variables for Production

**Backend (.env)**
```
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-production-database-url
CORS_ALLOWED_ORIGINS=your-frontend-url
```

**Frontend (.env.production)**
```
VITE_API_URL=your-production-api-url
```

## 🤝 Contributing

We welcome contributions to BrainBuddy AI! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React code
- Write tests for new features
- Update documentation accordingly

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check for port conflicts (another service using port 8000)

**Frontend connection errors:**
- Confirm backend is running on port 8000
- Verify API URL in .env file: `VITE_API_URL=http://localhost:8000/api`

**Authentication issues:**
- Check browser console for CORS errors
- Verify JWT tokens are being stored correctly in localStorage

**Database problems:**
- Run migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`

### Getting Help

1. Check the console for error messages
2. Verify all installation steps were completed
3. Ensure all services are running on correct ports
4. Consult the Django and React documentation

If problems persist, please open an issue with:
- Description of the problem
- Steps to reproduce
- Error messages from console
- Your environment (OS, Python version, Node version)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django REST Framework team for the excellent API framework
- React team for the powerful frontend library
- Tailwind CSS for the utility-first CSS framework
- Heroicons for the beautiful icon set

---

**BrainBuddy AI** - Empowering education through AI-powered management solutions.

For questions or support, please contact our development team or open an issue in the repository.
