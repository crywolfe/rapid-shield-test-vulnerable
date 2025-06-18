from setuptools import setup, find_packages

setup(
    name="vulnerable-test-app",
    version="1.0.0",
    description="Test application with intentional vulnerabilities",
    packages=find_packages(),
    install_requires=[
        "requests==2.25.1",
        "django==3.1.0", 
        "pyyaml==5.3.1",
        "pillow==8.0.0",
        "urllib3==1.26.4",
        "cryptography==3.2.0",
        "jinja2==2.11.0",
        "werkzeug==1.0.0",
        "flask==1.1.0",
        "sqlalchemy==1.3.0"
    ],
    python_requires=">=3.8",
)