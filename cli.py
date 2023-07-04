# Python Script to handle the command line input and output

import requests
import sys
import yaml

# API endpoint for the project information
API_ENDPOINT = "https://api.example.com/projects/"

def get_project_info(project_name):
    # Making a GET request to the API endpoint with the project name as a parameter
    response = requests.get(API_ENDPOINT + project_name)
    
    # Checking  the response status code
    if response.status_code == 200:
        project_info = response.json()
        return project_info
    else:
        return None

def main():
    if len(sys.argv) < 3:
        print("Please provide a project name.")
        return

    if sys.argv[1] != "landscape":
        print("Invalid command.")
        return

    project_name = sys.argv[2]
    project_info = get_project_info(project_name)

    if project_info is None:
        print("Project not found.")
    else:
        print(f"Category: {project_info['category_name']}")
        print(f"Subcategory: {project_info['subcategory_name']}")
        print("Item Details:")
        for key, value in project_info['item_details'].items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
