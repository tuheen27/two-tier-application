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
- **Python 3.x** - Programming language
- **Flask 3.0.0** - Web framework
- **MongoDB** - Document database (Docker container friendly)

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
└── .env                  # Environment overrides for Mongo settings
```

## 📦 Prerequisites

Before running this application, ensure you have:

- **Python 3.8+** installed
- **pip** (Python package manager)
- **Docker** (optional, for containerized deployment)
- **Jenkins** (optional, for CI/CD pipeline)
- **Git** for version control
- **MongoDB Docker image** (run `docker run -d -p 27017:27017 --name mongo mongo:6.0` or connect to any existing MongoDB instance)

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

Run MongoDB in Docker (default credentials not required for local dev):

```bash
docker run -d \
  --name mongo \
  -p 27017:27017 \
  mongo:6.0
```

> If you run MongoDB in another container network or an authenticated cluster, update the Mongo environment variables accordingly (see [Environment Variables](#-environment-variables)).

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
docker network create two-tier-net
docker run -d --name mongo --network two-tier-net mongo:6.0
docker run -d \
  -p 5000:5000 \
  --name flask-app \
  --network two-tier-net \
  -e MONGO_URI=mongodb://mongo:27017 \
  two-tier-app:latest
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
- **Mongo Defaults:** `MONGO_URI` or `MONGO_HOST`/`MONGO_PORT` plus `MONGO_USERNAME`, `MONGO_PASSWORD`, `MONGO_AUTH_SOURCE`, `MONGO_DB_NAME`, `MONGO_COLLECTION_NAME`

### Docker Configuration
Edit `Dockerfile` to customize:
- Base image
- Working directory
- Port exposure
- Startup command

## 📝 Environment Variables

Currently, the application uses default configurations. Override them with environment variables when deploying:

```bash
export FLASK_ENV=production

# Option 1: provide a full connection string (easiest for Mongo Atlas or auth-enabled Docker images)
export MONGO_URI=mongodb://username:password@mongo:27017/?authSource=admin

# Option 2: clear MONGO_URI and provide discrete connection pieces
unset MONGO_URI
export MONGO_HOST=mongo
export MONGO_PORT=27017
export MONGO_USERNAME=username
export MONGO_PASSWORD=password
export MONGO_AUTH_SOURCE=admin

export MONGO_DB_NAME=flask_app
export MONGO_COLLECTION_NAME=users
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
