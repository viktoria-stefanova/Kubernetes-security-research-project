from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# Simple HTML template for internal dashboard
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Internal Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        .status { color: #28a745; font-weight: bold; }
        .info { margin: 20px 0; padding: 15px; background: #e9ecef; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Internal Tools Dashboard</h1>
        <p class="status">Status: Running</p>
        <div class="info">
            <h3>Available Tools:</h3>
            <ul>
                <li>System Monitoring</li>
                <li>Log Viewer</li>
                <li>Configuration Management</li>
            </ul>
        </div>
        <p><small>Version 1.2.3 | Environment: Staging</small></p>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/status')
def status():
    """API status endpoint"""
    return jsonify({
        "service": "Internal Dashboard",
        "status": "running",
        "version": "1.2.3",
        "environment": "staging"
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    print("Starting Internal Dashboard...")
    print("Service running on port 5000")
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)