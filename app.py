from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient, errors
from dotenv import load_dotenv
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGO_PORT', '27017'))
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'admin')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'password123')
MONGO_AUTH_SOURCE = os.getenv('MONGO_AUTH_SOURCE', 'admin')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'flask_app')
MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'users')

# Create MongoDB client with authentication
try:
    mongo_client = MongoClient(
        host=MONGO_HOST,
        port=MONGO_PORT,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD,
        authSource=MONGO_AUTH_SOURCE,
        serverSelectionTimeoutMS=5000
    )
    # Test connection
    mongo_client.admin.command('ping')
    print(f"✅ Successfully connected to MongoDB at {MONGO_HOST}:{MONGO_PORT}")
    
    mongo_db = mongo_client[MONGO_DB_NAME]
    users_collection = mongo_db[MONGO_COLLECTION_NAME]
    
    # Create unique index on email
    users_collection.create_index('email', unique=True)
    print(f"✅ Database '{MONGO_DB_NAME}' and collection '{MONGO_COLLECTION_NAME}' ready")
    
except errors.PyMongoError as e:
    print(f"❌ MongoDB connection failed: {e}")
    raise

@app.route('/')
def index():
    """Render the index.html page"""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    """Receive data from frontend and store in database"""
    try:
        data = request.get_json() if request.is_json else request.form
        
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        
        if not name or not email:
            return jsonify({'success': False, 'message': 'Name and email are required'}), 400
        
        document = {
            'name': name,
            'email': email,
            'phone': phone,
            'created_at': datetime.utcnow()
        }

        result = users_collection.insert_one(document)

        return jsonify({
            'success': True,
            'message': 'Data saved successfully',
            'id': str(result.inserted_id)
        }), 201

    except errors.DuplicateKeyError:
        return jsonify({'success': False, 'message': 'Email already exists'}), 409
    except errors.PyMongoError as exc:
        return jsonify({'success': False, 'message': f'Database error: {exc}'}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users from database"""
    try:
        users = []
        for doc in users_collection.find().sort('created_at', -1):
            doc['id'] = str(doc.pop('_id'))
            doc['created_at'] = doc['created_at'].isoformat() if isinstance(doc.get('created_at'), datetime) else str(doc.get('created_at', ''))
            users.append(doc)
        return jsonify({'success': True, 'data': users}), 200
    except errors.PyMongoError as exc:
        return jsonify({'success': False, 'message': f'Database error: {exc}'}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify MongoDB connection"""
    try:
        mongo_client.admin.command('ping')
        return jsonify({
            'status': 'healthy',
            'database': MONGO_DB_NAME,
            'host': MONGO_HOST,
            'port': MONGO_PORT
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Flask application...")
    print(f"📊 MongoDB: {MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}")
    print(f"👤 Auth User: {MONGO_USERNAME}")
    app.run(debug=True, host='0.0.0.0', port=5000)