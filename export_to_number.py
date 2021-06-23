import argparse
from os import write
from sys import exit
from types import ModuleType
try:
    from tkinter import filedialog,Tk
    tkinter_installed = True
except ModuleNotFoundError:
    tkinter_installed = False
    print("If you are using a graphical enviorment, concider installing tkinter.")
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

def main():
    #parsing arguement
    parser = argparse.ArgumentParser(description="Prints the contents of a binairy")
    parser.add_argument("load_path", nargs='?', help="Gives the file to show the contents of right from the command line. ", type=str)
    parser.add_argument("save_path", nargs='?', help="Gives the file to show the contents of right from the command line. ", type=str)

    args = parser.parse_args()
    path = args.load_path
    write_location = args.save_path
    if tkinter_installed:
        dummy = Tk()
        Tk.withdraw(dummy)
    #prompt filename if neceserry
    if path == None:
        if tkinter_installed:
            path = filedialog.askopenfilename("Open a file to make intro a single number")
        else:
            exit("Please supply a file through the CLI if tkinter is not installed. ")
    if path == "":
        exit("There is no file to open")
    try:
        with open(path, "rb") as file:
            content = file.read()
        to_write = parse_file(content)
        # add a save dialog here later
        while True:
            if tkinter_installed:
                write_location = filedialog.asksaveasfilename()
            if write_location == "":
                print("You canceled the prompt, do you really want to discard the file?")
                if input("y/N>").lower().startswith("y"):
                    exit(0)
            else:
                break
        with open(write_location, "w") as file:
            file.write(str(to_write))

    except FileNotFoundError:
        exit(f"The file {path} does not exitst")
    except Exception as e:
        import traceback
        handle_error(e, traceback.format_exc())


if __name__ == "__main__":
    main()