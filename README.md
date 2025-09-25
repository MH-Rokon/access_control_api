Access Control API

Access Control API is a Django-based RESTful service for logging and managing door access events. Each access attempt is tracked with card ID, door name, status (granted/denied), and timestamp. The project is fully Dockerized for quick deployment and easy scalability.

Key Features

Record and manage access logs for multiple doors.

Track access status (granted or denied) for each card.

Filter access logs by card ID.

Full CRUD API endpoints for access logs.

Automatic logging of create and delete actions to system_events.log.

Easy deployment using Docker and Docker Compose.

Technology Stack

Backend: Python 3.12, Django 4.x, Django REST Framework (DRF)

Database: SQLite (default; can switch to PostgreSQL)

Containerization: Docker, Docker Compose

Project Structure
access_control_api/
├── access_control_api/        # Django project settings
├── logs/                      # Django app
│   ├── models.py              # AccessLog model
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API viewsets
│   ├── signals.py             # Logging signals
│   └── tests.py               # Unit tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

Installation
1. Local Setup

Clone the repository:

git clone <repo_url>
cd access_control_api


Create and activate a virtual environment:

python -m venv env
source env/bin/activate


Install dependencies:

pip install -r requirements.txt


Apply database migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


The API will be accessible at: http://127.0.0.1:8000/

2. Docker Setup

Build the Docker image and start containers:

sudo docker compose build
sudo docker compose up -d


Check running containers:

sudo docker ps


The API will be accessible at: http://localhost:8000/

API Endpoints
Method	Endpoint	Description	Query Params
GET	/api/logs/	List all access logs	card_id optional
GET	/api/logs/<id>/	Get log details by ID	-
POST	/api/logs/	Create a new access log	-
PUT	/api/logs/<id>/	Update an existing log	-
DELETE	/api/logs/<id>/	Delete a log	-

Filtering Example:

GET /api/logs/?card_id=C1001

Logging

All create and delete actions are automatically appended to system_events.log with timestamps:

[YYYY-MM-DD HH:MM:SS] - CREATE: Access log created for card C1001. Status: GRANTED.
[YYYY-MM-DD HH:MM:SS] - DELETE: Access log (ID: 4) for card C1002 was deleted.


Ensure the log file has write permissions inside the Docker container.

Testing

Run unit tests with:

python manage.py test


Tests cover:

Create, update, delete operations

Filtering logs by card ID

Validation for read-only timestamp field

Notes

Make sure your Docker container has access to the system_events.log file.

The timestamp field is read-only and cannot be updated via the API.

Use the development branch for ongoing work and merge into main when stable.