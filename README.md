# Two-Tier Flask Application 🚀

A simple two-tier web application built with Flask (Python) and MongoDB (running from a Docker container). This project demonstrates a complete DevOps pipeline with Docker containerization and Jenkins CI/CD automation.

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
│   Flask REST API + MongoDB          │
└─────────────────────────────────────┘
```

## ✨ Features

- ✅ **User Registration Form** - Simple HTML form to capture user data
- ✅ **REST API** - Flask-based RESTful API endpoints
- ✅ **Database Integration** - MongoDB collection for data persistence
- ✅ **AJAX Communication** - Asynchronous form submission without page reload
- ✅ **Error Handling** - Comprehensive error handling and validation
- ✅ **Docker Support** - Containerized application for easy deployment
- ✅ **CI/CD Pipeline** - Automated Jenkins pipeline for build and deployment
- ✅ **Email Validation** - Prevents duplicate email entries

## 🛠️ Technology Stack

### Backend
- **Python 3.11** - Programming language
- **Flask 3.0.0** - Web framework
- **PyMongo 4.8.0** - MongoDB driver for Python
- **MongoDB 7.0** - Document database with authentication

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
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose orchestration
├── Jenkinsfile            # Jenkins pipeline configuration
├── README.md              # Project documentation
├── .env                   # MongoDB connection settings
│
└── templates/
    └── index.html         # Frontend HTML form
```

## 📦 Prerequisites

Before running this application, ensure you have:

- **Python 3.11+** installed
- **pip** (Python package manager)
- **Docker & Docker Compose** for containerized deployment
- **MongoDB** (running locally or in Docker with authentication)
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

## 🍃 MongoDB Setup

### Option 1: Use Existing MongoDB (Recommended)
If you have MongoDB running with authentication:

```bash
# Check if MongoDB is running
docker ps --filter "name=mongo"

# Update .env file with your MongoDB credentials
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USERNAME=admin
MONGO_PASSWORD=password123
MONGO_AUTH_SOURCE=admin
```

### Option 2: Start New MongoDB Container

```bash
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:7.0
```

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

### Using Docker Compose (Recommended)

**Build and start all services:**
```bash
docker-compose up -d --build
```

**View logs:**
```bash
docker-compose logs -f flask_app
```

**Stop services:**
```bash
docker-compose down
```

**Check status:**
```bash
docker-compose ps
```

### Manual Docker Commands

**Build image:**
```bash
docker build -t flask-mongo-app:latest .
```

**Run container (connects to existing MongoDB):**
```bash
docker run -d \
  -p 5000:5000 \
  --name flask_application \
  --add-host=host.docker.internal:host-gateway \
  -e MONGO_HOST=host.docker.internal \
  -e MONGO_PORT=27017 \
  -e MONGO_USERNAME=admin \
  -e MONGO_PASSWORD=password123 \
  -e MONGO_AUTH_SOURCE=admin \
  flask-mongo-app:latest
```

### Access the Application
- **Main App:** http://localhost:5000
- **Health Check:** http://localhost:5000/health
- **Users API:** http://localhost:5000/users

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
      "id": "507f1f77bcf86cd799439011",
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "1234567890",
      "created_at": "2025-11-07T10:30:00.000000"
    }
  ]
}
```

### 4. Health Check
```
GET /health

Response (200):
{
  "status": "healthy",
  "database": "flask_app",
  "host": "localhost",
  "port": 27017
}
```

## 🗄️ Data Model (MongoDB)

Each document in the `users` collection looks like:

```json
{
  "_id": ObjectId,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "created_at": ISODate("2025-11-07T10:30:00Z")
}
```

- `_id`: MongoDB ObjectId (converted to string in API responses)
- `name`: User's full name (required)
- `email`: Unique email address (enforced by an index)
- `phone`: Optional phone number
- `created_at`: UTC timestamp generated by the server

## 🧪 Testing

### Test API with cURL

**Health check:**
```bash
curl http://localhost:5000/health
```

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

### Test with Browser
1. Open http://localhost:5000
2. Fill the form and submit
3. Check http://localhost:5000/users to see all entries

## 🔧 Configuration

### Application Settings
Edit `app.py` to modify:
- **Host:** Default `0.0.0.0` (all interfaces)
- **Port:** Default `5000`
- **Debug Mode:** Set to `False` for production
- **Mongo Defaults:** `MONGO_URI` or `MONGO_HOST`/`MONGO_PORT` plus `MONGO_USERNAME`, `MONGO_PASSWORD`, `MONGO_AUTH_SOURCE`, `MONGO_DB_NAME`, `MONGO_COLLECTION_NAME`

### Docker Configuration
Edit `Dockerfile` to customize:
- Base image
- Working directory
- Port exposure
- Startup command

## 📝 Environment Variables

The application reads configuration from `.env` file or environment variables:

**MongoDB Connection:**
```bash
MONGO_HOST=localhost              # MongoDB host
MONGO_PORT=27017                  # MongoDB port
MONGO_USERNAME=admin              # MongoDB username
MONGO_PASSWORD=password123        # MongoDB password
MONGO_AUTH_SOURCE=admin           # Authentication database
MONGO_DB_NAME=flask_app           # Target database name
MONGO_COLLECTION_NAME=users       # Collection name
```

**For Docker deployment:**
```bash
# Use host.docker.internal to connect to host MongoDB from container
MONGO_HOST=host.docker.internal
MONGO_PORT=27017
MONGO_USERNAME=admin
MONGO_PASSWORD=password123
MONGO_AUTH_SOURCE=admin
MONGO_DB_NAME=flask_app
MONGO_COLLECTION_NAME=users
```

**Defaults:** The application includes sensible defaults for local development with authenticated MongoDB.

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
