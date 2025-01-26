# ProfilesAPI

ProfilesAPI is a Django-based RESTful API designed to handle user profiles and their statuses. It provides user authentication, profile management, and a simple system for tracking user statuses. Built on Django REST Framework (DRF), it ensures scalability, security, and ease of integration.

---

## 🌟 Features

- **Authentication**: Registration, login, logout, and token-based authentication via `dj-rest-auth`.
- **Profile Management**: Retrieve a list of user profiles or access specific profiles using ID.
- **Profile Status Updates**: Add, update, and retrieve statuses for user profiles.
- **Automatic Profile Creation**: A user profile is automatically created when a new user is registered.
- **Secure Permissions**: Enforces strict permissions for users managing profiles and statuses.
- **Extensible Design**: Built with DRF to ensure scalability and flexibility.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/profilesAPI.git
cd profilesAPI
```

### 2. Setup a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations and Run the Development Server

```bash
python manage.py migrate
python manage.py runserver
```

- The API will run at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

---

## 🔑 Authentication

### Register a New User

Create a new user by sending a `POST` request to:
```
POST /api/rest-auth/registration/
``` 

#### Example Payload:
```json
{
  "username": "new_user",
  "email": "new_user@example.com",
  "password1": "strongpassword",
  "password2": "strongpassword"
}
```

### Login to Obtain a Token

Log in with your credentials by sending a `POST` request to:
```
POST /api/rest-auth/login/
``` 

#### Example Payload:
```json
{
  "username": "new_user",
  "password": "strongpassword"
}
```

#### Response:
If successful, you will receive an authentication token:

```json
{
  "key": "your_auth_token"
}
```

Use this token in the `Authorization` header of your requests:

```http
Authorization: Token your_auth_token
```

---

## 🔗 API Endpoints

### Profiles

- **List All Profiles**:  
  `GET /api/profiles/`

- **Retrieve a Specific Profile**:  
  `GET /api/profiles/<id>/`

### Profile Status

- **List All Profile Statuses**:  
  `GET /api/profile-status/`

- **Create a New Profile Status** (requires authentication):  
  `POST /api/profile-status/`

- **Retrieve a Specific Profile Status**:  
  `GET /api/profile-status/<id>/`

- **Update a Profile Status** (requires permission):  
  `PUT /api/profile-status/<id>/`

- **Delete a Profile Status** (requires permission):  
  `DELETE /api/profile-status/<id>/`

---

## 🌐 Example Usage

### Retrieve All Profiles

Use the following `curl` command to fetch all user profiles:

```bash
curl -H "Authorization: Token your_auth_token" http://127.0.0.1:8000/api/profiles/
```

### Create a Profile Status

To add a new status for the logged-in user’s profile:

#### Endpoint:
```
POST /api/profile-status/
``` 

#### Example Payload:
```json
{
  "status_content": "Hello, this is my first status!"
}
```

---

## 🛠️ Development Notes

### Automatic Profile Creation

Whenever a new user is registered, a profile is automatically created using Django signals. This is handled by the `signals.py` file in the `profiles` app.

### Email Backend

For development purposes, all email operations (such as registration confirmation emails) are configured to use the console. In `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

You can update this email backend to use a service like **SendGrid**, **Gmail SMTP**, or others for production.

### Authentication Configurations

The application uses **SessionAuthentication** and **TokenAuthentication** for secure API access.

---

## 📑 Future Improvements

Here are some planned features for future versions:

1. **Pagination**: Implement pagination to handle large datasets of profiles and statuses.
2. **Enhanced Validation**: Add more advanced validations for registration and profile updates.
3. **Admin Dashboard**: Provide an admin-friendly interface for managing user profiles and statuses.
4. **Password Policy**: Strengthen password validation policies (e.g., enforce complexity rules).
5. **Social Login**: Integrate social authentication (e.g., Google, Facebook).

---

## 🛡️ Permissions Overview

The system uses custom permissions (`permissions.py`) to enforce secure access:

- **Profiles**:
  - Users can only update their *own* profile unless they are staff/admin.
  - Read permissions are open to everyone.

- **Profile Statuses**:
  - Users can only update or delete their *own* statuses unless they are staff/admin.
  - Read permissions are open to everyone.

---

## 🧪 Testing the API

You can test the API using different Python scripts included in the project:

### Register and Test User Authentication
- File: `token-auth-test1.py`  
  This script performs registration and login testing.

### Test Authorized Profile Access
- File: `token-auth-test2.py`  
  Retrieves profiles using token-based authentication.

### Test Profile Status Creation
- File: `token-auth-test3.py`  
  Sends requests to create profile statuses.

To run any of these scripts, simply execute them with Python:

```bash
python token-auth-test1.py
```

---

### 🎉 **Happy coding with ProfilesAPI!**  
Feel free to extend, customize, and improve it to fit your specific use case.
```