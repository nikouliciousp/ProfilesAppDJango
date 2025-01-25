# ProfilesAPI

ProfilesAPI is a Django RESTful API designed to manage user profiles. Packed with features like user authentication, profile viewing, and status updates, it's built on Django REST Framework (DRF) to ensure scalability and simplicity.

---

## 🌟 Features
- **Authentication**: Registration, login, logout, and token-based authentication.
- **Profile Management**: Retrieve all user profiles or fetch specific ones.
- **Profile Status**: Track user profile updates via an integrated status system.
- **Automatic Profile Creation**: A profile is created automatically when a user registers.
- **Scalable & Secure**: Extensible architecture with integrated DRF tools for smooth API development.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/nikouliciousp/profilesAPI.git
cd profilesAPI
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations and Start the Server
```bash
python manage.py migrate
python manage.py runserver
```

Visit the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🔗 API Endpoints

### Authentication
- **Login**: POST `/api/rest-auth/login/`
- **Logout**: POST `/api/rest-auth/logout/`
- **Register**: POST `/api/rest-auth/registration/`

### Profiles
- **List All Profiles**: GET `/api/profiles/`
- **Retrieve Specific Profile**: GET `/api/profiles/<id>/`

---

## 🌐 Example Usage

### Register a New User
```json
# POST to /api/rest-auth/registration/
{
  "username": "testUser",
  "email": "testuser@example.com",
  "password1": "yourpassword",
  "password2": "yourpassword"
}
```

### Retrieve Profiles
1. Obtain a token via the login endpoint.
2. Access the profiles endpoint with the token:
```bash
curl -H "Authorization: Token <YOUR_TOKEN>" http://127.0.0.1:8000/api/profiles/
```

---

## 🛠️ Development Notes
- **Email Setup**: The email backend is set to `console` mode for development. Replace it with a production service like SendGrid or SMTP in production.
- **Authentication Methods**: Supports both `SessionAuthentication` and `TokenAuthentication` for secure API access.

---

## 📑 Future Enhancements
- Add edit and delete functionality to profiles.
- Support pagination for large profile datasets.
- Implement advanced password validation policies.

---

🎉 Happy coding with ProfilesAPI!