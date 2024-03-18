import pandas as pd
import requests

# Function to get data from the API
def get_data_from_api(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

# Function to display information for a selected team
def display_team_info(team_name, teams_data):
    for team in teams_data:
        if team['name'] == team_name:
            print(f"Information for {team_name}:")
            for key, value in team.items():
                print(f"{key}: {value}")
            break
    else:
        print(f"Team {team_name} not found in Premier League data.")

# Your API Token and Endpoint
api_token = 'f9ef4f66672b4ec48c33308fc38ef88e'
headers = {'X-Auth-Token': api_token}
api_url = 'https://api.football-data.org/v2/competitions/PL/teams'

# Make API Call
data = get_data_from_api(api_url, headers)

# Checking if data is retrieved successfully
if data:
    teams_data = data.get('teams', [])
    # Convert list of teams to DataFrame for easier handling (optional)
    df = pd.DataFrame(teams_data)
    
    # Ask user to enter a team name
    user_input = input("Enter a Premier League team name to see information: ")
    display_team_info(user_input, teams_data)
else:
    print("No data to display.")
