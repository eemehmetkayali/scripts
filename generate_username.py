#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Generate usernames from a list of names and surnames.')
parser.add_argument('file_path', metavar='file_path', type=str, help='The path to the file containing the list of names and surnames')
parser.add_argument('-v', '--verbose', action='store_true', help='Display additional information while generating usernames')
parser.add_argument('-l', '--lowercase', action='store_true', help='Generate usernames in all lowercase')
args = parser.parse_args()

usernames = []

try:
    with open(args.file_path, "r") as file:
        for line in file:
            name, surname = line.strip().split(" ")
            if args.verbose:
                print("Generating Usernames for {0} {1}".format(name, surname))
            if args.lowercase:
                username1 = name[0].lower() + surname.lower()
                username2 = name[0].lower() + "." + surname.lower()
                username3 = name.lower() + surname.lower()
                username4 = name.lower() + "." + surname.lower()
            else:
                username1 = name[0] + surname.lower()
                username2 = name[0] + "." + surname
                username3 = name.lower() + surname.lower()
                username4 = name.lower() + "." + surname.lower()
            usernames.extend([username1, username2, username3, username4])
except FileNotFoundError:
    print("Error: File not found.")

if len(usernames) > 0:
    print("Generated usernames:")
    print("\n".join(usernames))
else:
    print("No usernames were generated.")
