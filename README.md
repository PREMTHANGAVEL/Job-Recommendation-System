

markdown
# Job Recommendation System

This is a Django-based backend application that provides a job recommendation system. It allows users to enter their profile information and receive a list of job postings that best match their skills, experience level, and preferences.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [Database Design](#database-design)
- [Recommendation Logic](#recommendation-logic)
- [Error Handling](#error-handling)
- [Testing](#testing)

## Features
- Accepts user profile data to recommend suitable job postings.
- Stores user profiles and job postings in a database.
- Implements a recommendation algorithm to match users with job postings based on skills, experience, and preferences.
- Proper error handling for API requests and database operations.
  
## Technologies Used
- Python 3.10+
- Django 4.2
- Django Rest Framework (DRF)
- SQLite (default, can be replaced with PostgreSQL or MongoDB)
- Git for version control

## Getting Started

### Prerequisites
- Python 3.10+
- Django 4.2
- Git

### Installation
1. Clone the repository:
   bash
   git clone https://github.com/PREMTHANGAVEL/Job-Recommendation-System.git
   
2. Navigate to the project directory:
   bash
   cd Job-Recommendation-System
   
3. Create a virtual environment:
   bash
   python -m venv venv
   
4. Activate the virtual environment:

   - On macOS/Linux:
     bash
     source venv/bin/activate
     
   - On Windows:
     bash
     venv\Scripts\activate
     
5. Install the required dependencies:
   bash
   pip install -r requirements.txt
   
6. Run migrations to set up the database:
   bash
   python manage.py migrate
   
7. Start the development server:
   bash
   python manage.py runserver
   
## Endpoints
### User Profile
- `POST /user-profile/`: Add a user profile with details like name, skills, experience level, and preferences.

### Job Postings
- `POST /job-postings/`: Add a job posting to the database.
- `GET /job-postings/`: Get all job postings available.
  
### Recommendations
- `POST /recommend-jobs/`: Get job recommendations based on a user's profile.

## Database Design

### User Profile Model
- `name`: `CharField(max_length=255)`
- `skills`: `JSONField` - List of skills the user has.
- `experience_level`: `CharField(max_length=100)`
- `preferences`: `JSONField` - Desired roles, locations, job type.

### Job Posting Model
- `title`: `CharField(max_length=255)`
- `skills_required`: `JSONField` - List of skills required for the job.
- `experience_level`: `CharField(max_length=100)`
- `role`: `CharField(max_length=100)`
- `location`: `CharField(max_length=100)`
- `job_type`: `CharField(max_length=50)`

## Recommendation Logic
The recommendation algorithm is based on a rule-based matching system that considers:
1. **Skills**: Matches job postings with the user's skills.
2. **Experience Level**: Matches user experience with job requirements.
3. **Preferences**: Matches desired roles, locations, and job type.

## Error Handling
- Ensures that all required fields are provided in API requests.
- Validates the data types for fields like skills, experience level, and preferences.
- Returns appropriate status codes and error messages for invalid inputs.

## Testing
- Unit tests for the API endpoints are included to validate the behavior of each endpoint.
- Run the tests using:
  bash
  python manage.py test
  

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Prem Thangavel

This `README.md` file includes a summary of your project's features, technologies, installation instructions, database design, endpoints, and other relevant details. Feel free to modify it to better match your project's specifics.
