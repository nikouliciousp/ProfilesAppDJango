import requests


def client():
    """
    A simple client function to fetch and display the logged-in
    user's profile data from an API endpoint using an Authorization token.
    """
    # Replace <KEY> with your actual API token obtained from logging in
    token = "fc24de07d1929205f2ec9523a713b9f7d821e87b"

    # Construct headers with Authorization token
    headers = {"Authorization": f"Token {token}"}

    # Send GET request to the API endpoint for profiles
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the JSON response
        response_data = response.json()

        if response_data:  # If data is returned
            print("\nUser Profile:")
            for profile in response_data:  # Iterate over profiles if there are multiple
                for key, value in profile.items():
                    print(f"{key}: {value}")
        else:
            print("No profile data found for the user.")
    else:
        # Print failure details
        print(f"Failed to fetch data: {response.status_code}, {response.reason}")


if __name__ == "__main__":
    client()
