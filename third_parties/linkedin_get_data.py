import requests
import os
from dotenv import load_dotenv

def get_linkedin_data():
    load_dotenv()
    api_key = os.environ.get('PROXYCURL_API_KEY')  # Safely get the environment variable
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': 'https://www.linkedin.com/in/creighton-friend-s117',
    }

    # Make the API request
    response = requests.get(api_endpoint, params=params, headers=headers)

    # Ensure the request was successful
    if response.status_code == 200:
        # Define the filename
        filename = "linkedin_response_creightonfriend.py"

        # Open the file in write mode ('w')
        with open(filename, 'w') as file:
            # Write the content of 'response.text' to the file
            file.write(response.text)  # Use response.text to get the response content as a string

        print(f"API response has been written to {filename}")
    else:
        print(f"Failed to get data from API. Status code: {response.status_code}")

# Call the function to execute the code
get_linkedin_data()
