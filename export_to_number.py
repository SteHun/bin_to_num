import argparse
import os
from sys import exit
from tkinter import filedialog,Tk
from tqdm import tqdm

def handle_error(undetailed_message, detailed_message):
    print(f"A fatal error occured: {undetailed_message}")
    print("\nwould you like to see the detailed error message?")
    if input("y/N>").lower().startswith("y"):
        exit(detailed_message)
    else:
        exit()

def parse_file(file_content):
    result = 0
    for item in tqdm(file_content, desc="parsing content"):
        result *= 256
        result += item
    return result

if __name__ == "__main__":
    #parsing arguement
    parser = argparse.ArgumentParser(description="Prints the contents of a binairy")
    parser.add_argument("path", nargs='?', help="Gives the file to show the contents of right from the command line. ", type=str)
    args = parser.parse_args()
    path = args.path
    
    #prompt filename if neceserry
    if path == None:
        dummy = Tk()
        Tk.withdraw(dummy)
        path = filedialog.askopenfilename()
    if path == "":
        exit("There is no file to open")
    try:
        with open(path, "rb") as file:
            content = file.read()
        to_write = parse_file(content)
        # add a save dialog here later
        with open("output.txt", "w") as file:
            file.write(str(to_write))

    except FileNotFoundError:
        exit(f"The file {path} does not exitst")
    except Exception as e:
        import traceback
        handle_error(e, traceback.format_exc())