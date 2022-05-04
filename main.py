
import os
from prettytable import PrettyTable
from app_int import TelevisionApp


def func(id, key, connection):
    optionsDict = {"u": {"d": connection.display_users, "c": connection.create_user,
                         "e": connection.edit_user, "del": connection.delete_user},

                   "p": {"d": connection.display_playlists, "c": connection.create_user,
                         "e": connection.edit_user, "del": connection.delete_user},

                   "e": {"d": connection.display_episodes, "c": connection.create_episode,
                         "e": connection.edit_episode, "del": connection.delete_episode},

                   "r": {"d": connection.display_ratings, "c": connection.create_rating,
                          "e": connection.edit_rating, "del": connection.delete_rating}}

    return optionsDict[id][key]


def UserOptions(key):
    option_table = PrettyTable()
    option_table.field_names = ['Functionality', 'Key']

    if key == "u":
        option_table.add_rows(
            [["Display Users", "D"],
             ["Create Users", "C"],
             ["Edit User", "E"],
             ["Delete User", "DEL"],
             ["Return to main menu", "R"]])

    elif key == "p":
        option_table.add_rows(
            [["Display Playlists", "D"],
             ["Create Playlist", "C"],
             ["Edit Playlist", "E"],
             ["Delete Playlist", "DEL"],
             ["Return to main menu", "R"]])


    elif key == "r":
        option_table.add_rows(
            [["Display Ratings", "D"],
             ["Create Rating", "C"],
             ["Edit Rating", "E"],
             ["Delete Rating", "DEL"],
             ["Return to main menu", "R"]])

    elif key == "e":
        option_table.add_rows(
            [["Display Episodes", "D"],
             ["Create Episode", "C"],
             ["Edit Episode", "E"],
             ["Delete Episode", "DEL"],
             ["Return to main menu", ""]])

    return option_table







def main():
    # user, password = argv[1:]


    option_table = PrettyTable()
    option_table.field_names = ["Options", "Input"]
    option_table.add_rows(
        [["Users", "U"],
         ["Playlists", "P"],
         ["Episodes", "E"],
         ["Ratings", "R"],
         ["Quit", "Q"]])

    # prompt user for information to access the database

    #user = input("Enter username: ")
    #password = input("Enter password:")

    user = 'root'
    password = "f6cb77a13ad6491e"

    # connect to the database
    connection1 = TelevisionApp(user, password)
    connection1.connect()

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    running_main = True
    running_sub = False
    running_whole = True

    possible_main = ["u", "p", "e", "r"]
    func_option = ["d", "c","e", "del", "r"]

    chosen_main = ""
    chosen_sub = ""

    while running_whole:

        while running_main:
            print(option_table)
            user_option = input("Enter key based on options: ").lower().strip()

            if user_option == "q":
                running_main = False
                running_whole = False

            elif user_option in possible_main:
                clearConsole()
                chosen_main = user_option
                running_main = False
                running_sub = True

        while running_sub:
            print(UserOptions(chosen_main))
            option_input = input("Enter option: ").lower().strip()


            if option_input not in func_option:
                print("Enter valid response!")


            if option_input == "r":
                running_sub = False
                running_main = True
            else:
                chosen_sub = option_input
                chosen_func = func(chosen_main, chosen_sub, connection1)
                chosen_func()
                break


if __name__ == "__main__":
    main()
