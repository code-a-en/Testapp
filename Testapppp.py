#this code for test 
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Define allowed credentials
ALLOWED_IP = '192.100.100.100'
domain = testapp.adf.gov.sa
SECRET_CODE = 'mySecret123test'
ALLOWED_USERS = ['admin', 'user1']

# Authentication decorator
def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        username = request.headers.get('Username')
        secret = request.headers.get('Secret-Code')

        if client_ip != ALLOWED_IP:
            return jsonify({'error': 'Unauthorized IP'}), 403
        if username not in ALLOWED_USERS:
            return jsonify({'error': 'Unauthorized user'}), 403
        if secret != SECRET_CODE:
            return jsonify({'error': 'Invalid secret code'}), 403

        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/data', methods=['GET'])
@authenticate
def get_data():
    return jsonify({'message': 'Access
