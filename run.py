#!/usr/bin/env python3
"""
Flask Task Manager - DevOps Portfolio Project
Run the application locally for development
"""
from app import create_app
import os

# Create Flask application
app = create_app()

if __name__ == '__main__':
    # Configuration
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print("=" * 50)
    print("🚀 Flask Task Manager")
    print("=" * 50)
    print(f"📍 Running on: http://localhost:{port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"💡 Press Ctrl+C to stop")
    print("=" * 50)
    
    # Run the application
    app.run(
        host=host,
        port=port,
        debug=debug
    )