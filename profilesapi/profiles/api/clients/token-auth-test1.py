import requests


def client():
    """
    A client function that sends a POST request to authenticate a user
    with given credentials.

    The API endpoint is assumed to be a local development server, and 
    the function handles potential errors during the request and response processing.
    """
    # User credentials for authentication
    credentials = {"username": "pirate", "email": "pirate@example.com",
                   "password": "1234"}  # Corrected key name "em" to "email"

    try:
        # Send a POST request to the specified API endpoint with user credentials
        response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
        response.raise_for_status()  # Raise an exception for HTTP error responses

        print("Status code:", response.status_code)  # Log the HTTP status code of the response

        try:
            # Try to parse the response content as JSON
            response_json = response.json()
            print("Response:", response_json)  # Log the parsed JSON response
        except ValueError:
            print("Failed to parse JSON response.")  # Log error if response cannot be parsed
    except requests.exceptions.RequestException as e:
        # Log any request-related errors (e.g., connection issues, timeouts)
        print("An error occurred:", e)


if __name__ == "__main__":
    client()  # Run the client function when the script is executed
