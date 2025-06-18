#!/usr/bin/env python3
"""
Test vulnerable application for Rapid Shield testing.
This app intentionally contains security vulnerabilities for testing purposes.
"""

import os
import sys
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerability 1: Command injection
@app.route('/run_command')
def run_command():
    cmd = request.args.get('cmd', 'ls')
    # VULNERABLE: Direct command execution without sanitization
    result = os.system(cmd)
    return f"Command executed: {cmd}, Result: {result}"

# Vulnerability 2: SQL injection potential
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # VULNERABLE: String concatenation for SQL (simulated)
    sql = f"SELECT * FROM users WHERE name = '{query}'"
    return f"Executing SQL: {sql}"

# Vulnerability 3: Template injection
@app.route('/render')
def render():
    template = request.args.get('template', 'Hello World')
    # VULNERABLE: Direct template rendering
    return render_template_string(template)

# Vulnerability 4: Hardcoded secret
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # VULNERABLE: Command injection via sys.argv
        os.system(sys.argv[1])
    app.run(debug=True, host='0.0.0.0')