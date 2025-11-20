# simple-notes-app-45001-45010

Backend (Django + DRF) Notes API

- Health: GET /api/health/
- Notes:
  - List: GET /api/notes/
  - Create: POST /api/notes/ { "title": "My note", "content": "..." }
  - Retrieve: GET /api/notes/<id>/
  - Update: PUT /api/notes/<id>/ { "title": "...", "content": "..." }
  - Patch: PATCH /api/notes/<id>/ { "title": "..." } or { "content": "..." }
  - Delete: DELETE /api/notes/<id>/

Run standard Django migrations and optionally seed sample data:
- python manage.py migrate
- python manage.py seed_notes

Swagger docs are available at /docs and Redoc at /redoc.