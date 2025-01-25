import requests


def client():
    """
    Function to send a POST request for user registration.

    This function sends a POST request to register a new user 
    with username, email, and password credentials. It prints 
    the HTTP status code and the response received from the server.
    """

    # User data payload for the registration request
    data = {
        "username": "testUser",  # Username to register
        "email": "testuser@example.com",  # User's email address
        "password1": "cangpass",  # First instance of the password
        "password2": "cangpass"  # Re-entered password to confirm
    }

    try:
        # Sending a POST request to the registration endpoint
        response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

        # Printing the HTTP response status code
        print("Status code:", response.status_code)

        # Parsing the response JSON and printing it
        response_json = response.json()
        print("\nResponse:", response_json)
    except requests.exceptions.RequestException as e:
        # Handling any request exceptions (e.g., connection issues)
        print("An error occurred:", e)


if __name__ == "__main__":
    # Calling the client function to execute the registration request
    client()
