import gspread
from google.oauth2.service_account import Credentials

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
        select_champion = str(input("\nSelect a champion:\n").capitalize())
        # Check if the name was entered properly
       
        try:            
            if select_champion in available_champions:
                return select_champion
            else:
                print("Please enter a correct champion name.\n")
                return user_selected_champion()
        except ValueError as e:
            print(f"Sorry there seems to have been an error: {e.strerror}")

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
                    print(f"\nThe best build for {selected_champion} is:\n")
                    for items in list:
                        print(items)
                    return False
    except ValueError as e:
        print(f"Please accept our sincerest apolgoies it seems there has been an error, {e.errno} that says {e.strerror}. Restart the program and select another champion.")
    
    print("Please try again and enter the correct champion name this time\n.")
    return user_selected_champion()
   

def ask_user_for_recommendations():
    """
    This function allows the user to submit any recommendations that they have.
    """
    show_user_recommended_builds = SHEET.worksheet("user-recommendations").get_all_data()
    user_choice = str(input("\n Would you like to view recommended builds from other players?\n").lower())

    if user_choice == "yes":
        if not show_user_recommended_builds:
            print("Unfortunetly the list is empty. Be the first one the recommend a build for others to use!")
        else:
            print("Here is the player recommended builds.")
            print(show_user_recommended_builds)
    else:
        print("Not to worry. You still have an option of recommending your own build.")
    


def main():
    selected_champion = user_selected_champion()
    send_user_item_build(selected_champion)
    ask_user_for_recommendations()

main()
