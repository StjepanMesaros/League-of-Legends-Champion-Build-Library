import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


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
    print(Fore.YELLOW + "Welcome to the most advanced never before seen League of Legends champion build selector.")
    print(Fore.YELLOW + "Available champions to choose from are:\n")
    
    for champion in available_champions:
        print(champion)
    while True:    
        select_champion = str(input(Fore.MAGENTA + "\nSelect a champion:\n").capitalize())
        # Check if the name was entered properly
       
        try:            
            if select_champion in available_champions:
                print(Fore.YELLOW + "Looking for your build...")
                return select_champion
            else:
                print(Fore.YELLOW + "Please enter a correct champion name.\n")
                return user_selected_champion()
        except ValueError as e:
            print(Fore.YELLOW + f"Sorry there seems to have been an error: {e.strerror}")

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
        print(Fore.YELLOW + f"Please accept our sincerest apolgoies it seems there has been an error, {e.errno} that says {e.strerror}. Restart the program and select another champion.")
    
    print(Fore.YELLOW + "Please try again and enter the correct champion name this time\n.")
    return user_selected_champion()
   

def ask_user_to_view_player_recommendations():
    """
    This function allows the user to view any recommendations that players have.
    """
    user_recommended_builds_sheet = SHEET.worksheet("user-recommendations").get_all_values()
    user_choice = str(input(Fore.MAGENTA + "\nWould you like to view recommended builds from other players?\n").lower())

    if user_choice == "yes":
        if not user_recommended_builds_sheet:
            print(Fore.YELLOW + "\nUnfortunetly the list is empty. Be the first one the recommend a build for others to use!")
        else:
            print(Fore.YELLOW + "\nHere is the player recommended builds.")
            for items in user_recommended_builds_sheet:
                print(items)
    else:
        print(Fore.YELLOW + "\nNot to worry. You still have an option of recommending your own build.")
    

def ask_user_to_submit_recommendations():
    """
    This function will ask user to submit any recommendations that they have.
    """
    user_recommended_builds_sheet = SHEET.worksheet("user-recommendations")
    user_choice = str(input(Fore.MAGENTA + "\nWould you like to make a recommendation in builds for other players?\n").lower())

    if user_choice == "yes":
        user_recommended_item_list = []
        champion = str(input(Fore.MAGENTA + "\nWhat champion do you have in mind? \n").capitalize())
        user_recommended_item_list.append(champion)

        first_item = str(input(Fore.MAGENTA + "\nFirst item:\n").capitalize())
        user_recommended_item_list.append(first_item)

        second_item = str(input(Fore.MAGENTA + "\nSecond item: \n").capitalize())
        user_recommended_item_list.append(second_item)

        third_item = str(input(Fore.MAGENTA + "\nThird item: \n").capitalize())
        user_recommended_item_list.append(third_item)

        fourth_item = str(input(Fore.MAGENTA + "\nFourth item: \n").capitalize())
        user_recommended_item_list.append(fourth_item)

        fifth_item = str(input(Fore.MAGENTA + "\nFifth item \n").capitalize())
        user_recommended_item_list.append(fifth_item)

        sixth_item = str(input(Fore.MAGENTA + "\nSixth item: \n").capitalize())
        user_recommended_item_list.append(sixth_item)

        seventh_item = str(input(Fore.MAGENTA + "\nSeventh item: \n").capitalize())
        user_recommended_item_list.append(seventh_item)

        user_recommended_builds_sheet.append_row(user_recommended_item_list)
        print("\nThank you for your contribution!")
    else:
        print("That is alright, maybe next time!")






def main():
    selected_champion = user_selected_champion()
    send_user_item_build(selected_champion)
    ask_user_to_view_player_recommendations()
    ask_user_to_submit_recommendations()

main()
