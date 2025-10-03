# Data Base Lab 4

## Description
This is a simple Flask project with a REST API for demonstrating basic operations using a Python dictionary `todos`. 
The API allows retrieving and adding items without requiring an external database.

## Features
- Retrieve all todos. 
- Add a new todo by ID.
- Simple REST API using Flask and Flask-RESTX.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/nikaakor/data-base-lab-4.git
cd data-base-lab-4

2. Install dependencies:
pip install -r requirements.txt

3. Run the server:
python3 app.py

The server will run on port 5000 by default. Make sure the port is open in your VM or firewall settings for external access.

API Usage
	•	GET /hi — Retrieve all todos
	•	PUT /number/<id> — Add a new todo with the given id

Example: 
curl http://<VM_PUBLIC_IP>:5000/hi
curl -X PUT http://<VM_PUBLIC_IP>:5000/number/1

Notes
	•	The project uses an in-memory dictionary (todos) for simplicity.
	•	No external database connection is required.
	•	The server supports Swagger UI automatically via Flask-RESTX.


