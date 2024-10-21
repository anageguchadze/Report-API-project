# Reporting API

## Overview

The Reporting API is a RESTful web service built using Django and Django Rest Framework. It provides endpoints for managing users with different roles (Administrator, Courier, Office Worker) and for creating and managing reports. This API is designed for applications that require user role management and reporting functionalities.

## Features

- **Custom User Model**: A custom user model with roles (Administrator, Courier, Office Worker) to manage access control.
- **Role-based Permissions**: Fine-grained permissions allowing only specific roles to perform actions such as creating or deleting reports.
- **Report Management**: Create, read, update, and delete reports with associated metadata.

## Technologies Used

- Django
- Django Rest Framework
- Python 3.x
- SQLite (or any other database of your choice)
- Django Admin for managing models

## Installation

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- pip (Python package installer).

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Report-API-project
