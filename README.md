Access Control API

A Django-based RESTful API for logging and managing door access events. Each access attempt is recorded with a card ID, door name, access status (granted/denied), and timestamp. The project is fully Dockerized for quick deployment and scalability.

Features

Record and manage access logs for multiple doors

Track access status (granted/denied) per card

Full CRUD API endpoints

Filter access logs by card_id

Automatic event logging to system_events.log on create and delete

Ready-to-use with Docker & Docker Compose

🛠️ Tech Stack

Backend: Python 3.12, Django 4.x, Django REST Framework (DRF)

Database: SQLite (default, easily switchable to PostgreSQL)

Containerization: Docker, Docker Compose


Project Structure
access_control_api/
├── access_control_api/        # Django project settings
├── access_control/            # Main app
│   ├── models.py              # AccessLog model
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   ├── signals.py             # Create/Delete signals
│   └── tests.py               # Unit tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

⚙️ Installation
🔹 Local Setup
# Clone repo
git clone https://github.com/MH-Rokon/access_control_api.git
cd access_control_api

# Create & activate virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver


 API available at: http://127.0.0.1:8000

🔹 Docker Setup
# Build and start containers
docker compose build
docker compose up -d

# Check running containers
docker ps


 API available at: http://localhost:8000

 API Endpoints
Method	Endpoint	Description	Query Params
GET	/api/logs/	List all access logs	card_id (optional)
GET	/api/logs/<id>/	Retrieve log by ID	-
POST	/api/logs/	Create new access log	-
PUT	/api/logs/<id>/	Update existing log	-
DELETE	/api/logs/<id>/	Delete log by ID	-

Filtering Example:

GET /api/logs/?card_id=C1001

Logging

All create and delete actions are automatically written to system_events.log:

[2025-09-23 10:35:15] - CREATE: Access log created for card C1001. Status: GRANTED.
[2025-09-23 10:38:00] - DELETE: Access log (ID: 4) for card C1002 was deleted.


Ensure system_events.log has write permissions inside Docker container.

Testing

Run the test suite:

python manage.py test


Covers:

Create, update, delete operations

Filtering by card_id

Read-only validation for timestamp

🔄 Development Workflow

Use the dev branch for ongoing work

Merge into main only when stable

Ensure commits are small and descriptive