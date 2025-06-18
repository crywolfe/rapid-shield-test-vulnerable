# Vulnerable Test Application

This is a test application with intentional security vulnerabilities for testing the Rapid Shield vulnerability remediation system.

## Known Vulnerabilities

### Dependency Vulnerabilities
- requests 2.25.1 - Known CVEs in older versions
- django 3.1.0 - Security issues in older Django versions  
- pyyaml 5.3.1 - YAML deserialization vulnerabilities
- pillow 8.0.0 - Image processing vulnerabilities
- jinja2 2.11.0 - Template injection vulnerabilities

### Code Vulnerabilities
- Command injection in `/run_command` endpoint
- SQL injection potential in `/search` endpoint
- Template injection in `/render` endpoint
- Hardcoded secrets (API keys, passwords)
- Unsafe command execution via command line arguments

## Usage

This repository is designed for testing security scanning tools and should never be deployed in production.