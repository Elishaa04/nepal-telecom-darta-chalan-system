# Nepal Telecom Darta & Chalan Management System

A web-based document management system developed using Django for managing Darta and Chalan records.

## Features

* User Authentication (Login/Logout)
* Role-Based Access Control (Admin/User)
* Darta Management

  * Add
  * Edit
  * Delete
  * Search
* Chalan Management

  * Add
  * Edit
  * Delete
  * Search
* Document Upload & Viewing
* Activity Log Tracking
* User Management
* Excel Export (Darta & Chalan)
* Dashboard Statistics

## Technology Stack

* Python
* Django
* HTML
* CSS
* SQLite
* OpenPyXL

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Project Structure

* records/ → Application logic
* templates/ → Frontend templates
* media/ → Uploaded files
* legalsystem/ → Django project configuration

## Future Enhancements

* PDF Export
* OCR Document Scanner
* Dashboard Charts
* Email Notifications
* PostgreSQL Integration
* Windows Server Deployment

## Author

Elisha
