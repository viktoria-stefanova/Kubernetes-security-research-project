from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Hardcoded API key 
VALID_API_KEY = "sk_prod_a7f3c9d2e1b4a8f6c2d9e3a1b7f4c8d2"

# Load customer data from JSON file (mounted from ConfigMap)
def load_customer_data():
    """Load customer data from mounted ConfigMap"""
    try:
        with open('/data/customers.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading customer data: {e}")
        return {"customers": [], "api_key": ""}

# Load data at startup
customer_data = load_customer_data()

@app.route('/')
def home():
    return jsonify({
        "service": "Customer Data API",
        "version": "2.1.4",
        "status": "healthy",
        "endpoints": [
            "/api/health",
            "/api/customers",
            "/api/customer/<id>"
        ]
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "data_loaded": len(customer_data.get('customers', [])) > 0})

@app.route('/api/customers')
def get_customers():
    """Get all customers - requires valid API key"""
    auth_header = request.headers.get('Authorization')
    
    # Check if API key is provided and valid
    if not auth_header:
        return jsonify({
            "error": "Missing API key",
            "hint": "Include Authorization header with Bearer token"
        }), 401
    
    # Extract the key from "Bearer <key>" format
    if not auth_header.startswith('Bearer '):
        return jsonify({"error": "Invalid authorization format. Use: Bearer <api_key>"}), 401
    
    provided_key = auth_header[7:]  # Remove "Bearer " prefix
    
    # Validate API key (hardcoded check - the vulnerability!)
    if provided_key != VALID_API_KEY:
        return jsonify({"error": "Invalid API key"}), 403
    
    # If valid, return customer data
    return jsonify({
        "customers": customer_data.get('customers', []),
        "count": len(customer_data.get('customers', []))
    })

@app.route('/api/customer/<customer_id>')
def get_customer(customer_id):
    """Get specific customer by ID - requires valid API key"""
    auth_header = request.headers.get('Authorization')
    
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Missing or invalid authorization"}), 401
    
    provided_key = auth_header[7:]
    
    if provided_key != VALID_API_KEY:
        return jsonify({"error": "Invalid API key"}), 403
    
    # Search for customer
    for customer in customer_data.get('customers', []):
        if customer['id'] == customer_id:
            return jsonify(customer)
    
    return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    print("Starting Customer API server...")
    print(f"Loaded {len(customer_data.get('customers', []))} customers")
    print("Server ready on port 8080")
    # Run with threaded=True and use_reloader=False for stability in containers
    app.run(host='0.0.0.0', port=8080, threaded=True, use_reloader=False)