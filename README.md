# Two-Tier Flask Application 🚀

A simple two-tier web application built with Flask (Python) and SQLite database. This project demonstrates a complete DevOps pipeline with Docker containerization and Jenkins CI/CD automation.

## 📋 Table of Contents
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)

## 🏗️ Architecture

This is a **two-tier architecture** application:

```
┌─────────────────────────────────────┐
│         Frontend (Tier 1)           │
│   HTML Form + JavaScript (AJAX)     │
└──────────────┬──────────────────────┘
               │
               │ HTTP/JSON
               │
┌──────────────▼──────────────────────┐
│         Backend (Tier 2)            │
│   Flask REST API + SQLite Database  │
└─────────────────────────────────────┘
```

## ✨ Features

- ✅ **User Registration Form** - Simple HTML form to capture user data
- ✅ **REST API** - Flask-based RESTful API endpoints
- ✅ **Database Integration** - SQLite database for data persistence
- ✅ **AJAX Communication** - Asynchronous form submission without page reload
- ✅ **Error Handling** - Comprehensive error handling and validation
- ✅ **Docker Support** - Containerized application for easy deployment
- ✅ **CI/CD Pipeline** - Automated Jenkins pipeline for build and deployment
- ✅ **Email Validation** - Prevents duplicate email entries

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Programming language
- **Flask 3.0.0** - Web framework
- **SQLite3** - Lightweight database

### Frontend
- **HTML5** - Markup
- **JavaScript (ES6)** - Client-side logic
- **Fetch API** - AJAX requests

### DevOps
- **Docker** - Containerization
- **Jenkins** - CI/CD automation
- **Git/GitHub** - Version control

## 📁 Project Structure

```
two-tier-application/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── Jenkinsfile           # Jenkins pipeline configuration
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # Frontend HTML form
│
└── database.db           # SQLite database (auto-generated)
```

## 📦 Prerequisites

Before running this application, ensure you have:

- **Python 3.8+** installed
- **pip** (Python package manager)
- **Docker** (optional, for containerized deployment)
- **Jenkins** (optional, for CI/CD pipeline)
- **Git** for version control

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/tuheen27/two-tier-application.git
cd two-tier-application
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 💻 Usage

### Access the Application
1. Open your browser and navigate to: `http://localhost:5000`
2. Fill in the registration form:
   - **Name** (required)
   - **Email** (required, must be unique)
   - **Phone** (optional)
3. Click **Submit**
4. View success/error message

### View All Users
Access the API endpoint to view all registered users:
```bash
curl http://localhost:5000/users
```

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t two-tier-app:latest .
```

### Run Docker Container
```bash
docker run -d -p 5000:5000 --name flask-app two-tier-app:latest
```

### Access the Application
```
http://localhost:5000
```

### Stop and Remove Container
```bash
docker stop flask-app
docker rm flask-app
```

## 🔄 CI/CD Pipeline

This project includes a **Jenkins pipeline** that automates:

### Pipeline Stages:
1. **Checkout Code** - Clones repository from GitHub
2. **Build Docker Image** - Creates Docker image
3. **Login to Docker Hub** - Authenticates with Docker credentials
4. **Push to Docker Hub** - Pushes image to `tuheen27/jenkinsfile:latest`

### Setup Jenkins Pipeline:
1. Create a new Pipeline project in Jenkins
2. Configure GitHub repository URL
3. Add Docker Hub credentials (ID: `DOCKER`)
4. Use `Jenkinsfile` from repository
5. Run the pipeline

### Docker Hub Image
```bash
docker pull tuheen27/jenkinsfile:latest
docker run -d -p 5000:5000 tuheen27/jenkinsfile:latest
```

## 🔌 API Endpoints

### 1. Home Page
```
GET /
Returns: HTML registration form
```

### 2. Submit User Data
```
POST /submit
Content-Type: application/json

Request Body:
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}

Success Response (201):
{
  "success": true,
  "message": "Data saved successfully",
  "id": 1
}

Error Response (400):
{
  "success": false,
  "message": "Name and email are required"
}

Error Response (409):
{
  "success": false,
  "message": "Email already exists"
}
```

### 3. Get All Users
```
GET /users

Response (200):
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "1234567890",
      "created_at": "2025-11-07 10:30:00"
    }
  ]
}
```

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Columns:**
- `id` - Auto-increment primary key
- `name` - User's full name (required)
- `email` - Unique email address (required)
- `phone` - Phone number (optional)
- `created_at` - Timestamp of record creation

## 🧪 Testing

### Test API with cURL

**Submit a user:**
```bash
curl -X POST http://localhost:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","phone":"1234567890"}'
```

**Get all users:**
```bash
curl http://localhost:5000/users
```

## 🔧 Configuration

### Application Settings
Edit `app.py` to modify:
- **Host:** Default `0.0.0.0` (all interfaces)
- **Port:** Default `5000`
- **Debug Mode:** Set to `False` for production
- **Database Path:** Default `database.db`

### Docker Configuration
Edit `Dockerfile` to customize:
- Base image
- Working directory
- Port exposure
- Startup command

## 📝 Environment Variables

Currently, the application uses default configurations. For production deployment, consider using environment variables:

```bash
export FLASK_ENV=production
export DATABASE_PATH=/data/database.db
export PORT=5000
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 👤 Author

**Tuheen**
- GitHub: [@tuheen27](https://github.com/tuheen27)
- Repository: [two-tier-application](https://github.com/tuheen27/DevOps-Project-Two-Tier-Flask-App.git)
