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

    available_champions = SHEET.worksheet("champions-builds").col_values(1)
    print("Welcome to the most advanced never before seen League of Legends champion build selector.")
    print("Available champions to choose from are:\n")
    
    for champion in available_champions:
        print(champion)
    while True:    
        select_champion = str(input("\nSelect a champion: \n"))
        return select_champion
    

def send_user_item_build(selected_champion):
    """
    This function will return to the user the 
    corsponding build that suits their selected champion.
    """

    data = SHEET.worksheet("champions-builds").get_all_values()
    try:
        for list in data:
            for look_for_champion in list:
                if look_for_champion == selected_champion:
                    del list[0]
                    print(f"The best build for {selected_champion} is:\n")
                    for items in list:
                        print(items)
                    return False
    except ValueError:
        print("Please enter a correct champions name.")
    return True




def main():
    selected_champion = user_selected_champion()
    send_user_item_build(selected_champion)

main()