"""
Process a JSON file to count nba players by team and save the result.
In output file, each line contains a team ID and the count of players on that team. Note, -2 = inactive, -1 = free agent. I've added the team mapping in the code. 
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed"

# Team mapping for reference

team_id_map = {
    -2: "Inactive",
    -1: "Free Agent",
    0: "Atlanta Hawks",
    1: "Boston Celtics",
    2: "Brooklyn Nets",
    3: "Charlotte Hornets",
    4: "Chicago Bulls",
    5: "Cleveland Cavaliers",
    6: "Dallas Mavericks",
    7: "Denver Nuggets",
    8: "Detroit Pistons",
    9: "Golden State Warriors",
    10: "Houston Rockets",
    11: "Indiana Pacers",
    12: "Los Angeles Clippers",
    13: "Los Angeles Lakers",
    14: "Memphis Grizzlies",
    15: "Miami Heat",
    16: "Milwaukee Bucks",
    17: "Minnesota Timberwolves",
    18: "New Orleans Pelicans",
    19: "New York Knicks",
    20: "Oklahoma City Thunder",
    21: "Orlando Magic",
    22: "Philadelphia 76ers",
    23: "Phoenix Suns",
    24: "Portland Trail Blazers",
    25: "Sacramento Kings",
    26: "San Antonio Spurs",
    27: "Toronto Raptors",
    28: "Utah Jazz",
    29: "Washington Wizards"
}

#####################################
# Define Functions
#####################################


def count_players_by_team(file_path: pathlib.Path) -> dict:
    """Count the number of players on each team from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            roster_data = json.load(file)  
            players_list = roster_data.get("players", [])

            # initialize an empty dictionary to store the counts
            team_counts = {}
            for player in players_list:
                team_id = player.get("tid", "Unknown")
                team_counts[team_id] = team_counts.get(team_id, 0) + 1

            return team_counts
                  
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count players on teams, and save the result."""

    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "nba_roster_25-26.json")

    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "nba_roster_25-26.txt")
    
    team_counts = count_players_by_team(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write("NBA Players by team:\n")
        for team_id, count in team_counts.items():
            team_name = team_id_map.get(team_id, "Unknown")
            file.write(f"{team_name}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")