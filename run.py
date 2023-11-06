import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('LeagueOfLegends_ChampionBuildLibrary')

def user_selected_champion():
    """
    This function gets the user inputed champion 
    and passes it on to be processed.
    """

    available_champions = SHEET.worksheet("champions-builds").get_all_values()[0]
    print("Welcome to the most advanced never before seen League of Legends champion build selector.")
    print("Available champions to choose from are:\n")
    
    for champion in available_champions:
        print(champion)
        
    select_champion = str(input("\nSelect a champion: "))

    return select_champion

user_selected_champion()