import requests
import msvcrt
import time
import os
from colorama import init, Fore

# Initialize colorama
init()

def check_username_availability(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The username '{Fore.RED}{username}{Fore.RESET}' is not available."
    else:
        return f"The username '{Fore.GREEN}{username}{Fore.RESET}' is available."

# Animated intro frames
intro_frames = [
    "██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗",
    "██║    ██║██╔════╝██║     ██╔═══██╗██╔══██╗████╗ ████║",
    "██║ █╗ ██║███████╗██║     ██║   ██║██████╔╝██╔████╔██║",
    "██║███╗██║╚════██║██║     ██║   ██║██╔══██╗██║╚██╔╝██║",
    "╚███╔███╔╝███████║███████╗╚██████╔╝██████╔╝██║ ╚═╝ ██║",
    " ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝",
    "",
    "          P R E S E N T S",
    "",
    "",
    "",  # Add more empty lines here if needed
]

# Clear the console screen
os.system("cls" if os.name == "nt" else "clear")

# Display the animated intro
frame_height = len(intro_frames)
for i in range(frame_height):
    os.system("cls" if os.name == "nt" else "clear")
    for j in range(i + 1):
        print(intro_frames[j])
    time.sleep(0.1)  # Adjust the delay to control animation speed

# Display instruction
print("Make sure to create a text file named 'usernames.txt' in this folder.")
input("Press Enter to continue...")

# Ask for confirmation
print("Not all names are accurately checked. Press 'Y' to confirm.")
confirmation_key = msvcrt.getch()
if confirmation_key not in [b'y', b'Y']:
    print("Operation cancelled.")
else:
    # Get the path to the script's folder
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # Read usernames from the text file in the script's folder
    usernames_to_check = []
    usernames_file_path = os.path.join(script_folder, "usernames.txt")
    with open(usernames_file_path, "r") as file:
        usernames_to_check = file.read().splitlines()

    # Check username availability and write to files
    available_usernames = []
    unavailable_usernames = []

    for username in usernames_to_check:
        result = check_username_availability(username)
        print(result)  # Print the result as it's checked
        if "is available" in result:
            available_usernames.append(username)
        else:
            unavailable_usernames.append(username)

    # Write available usernames to a file
    with open("available_usernames.txt", "w") as file:
        for username in available_usernames:
            file.write(username + "\n")

    # Write unavailable usernames to a file
    with open("unavailable_usernames.txt", "w") as file:
        for username in unavailable_usernames:
            file.write(username + "\n")

    print("Available usernames saved to available_usernames.txt")
    print("Unavailable usernames saved to unavailable_usernames.txt")

print("Press any key to close the program...")
msvcrt.getch()  # Wait for a key press
