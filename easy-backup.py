#!/usr/bin/python3
# Norbert van Adrichem / 2019 / www.norbert.in
import argparse
import shutil
import os
import time

version = "0.1"
parser = argparse.ArgumentParser()
current_backup = ""
current_folder = ""

def parser_setup():
    parser.add_argument("source", help="The directory that contains the files to be backupped")
    parser.add_argument("destination", help="The destination of the backups. Dated directories will be created in this folder")
    parser.add_argument("--no-rotation", help="Turn off backup rotation", action="store_true")
    parser.add_argument("--max-backups", help="Defines the maximum number of backups to be stored in the destination", type=int, default=5)
    parser.add_argument("--prepend", help="Defines a different string to prepend to individual backups", default='ezback')

def validate():
    options = parser.parse_args()
    if not (os.path.isdir(options.source)):
        print("The source provided is not a directory or does not exist")
        exit()
    if not (os.path.isdir(options.destination)):
        print("Please enter a valid destination directory")
        exit()
    if not (os.path.isabs(options.destination)):
        options.destination = os.getcwd()+"/"+options.destination
    if not (os.path.isabs(options.source)):
        options.source = os.getcwd()+"/"+options.source
    return options
    
def create_new_current(options):
    global current_backup, current_folder
    current_backup = options.prepend+"-"+str(round(time.time()))
    current_folder = options.destination.rstrip("/")+"/"+current_backup

def execute_backup(options):
    print("Backup initiated...")
    print(current_folder)
    shutil.copytree(options.source, current_folder)
    print("New state saved")

def rotate_backups(options):
    if (options.no_rotation == False):
        all_directories = os.listdir(options.destination.rstrip("/"))
        relevant_directories = []
        for directory in all_directories:
            if (directory.startswith(options.prepend)):
                relevant_directories.append(directory)
        relevant_directories.sort(reverse=True)
        relevant_directories = relevant_directories[options.max_backups:]
        for remove_directory in relevant_directories:
            if (remove_directory != ""):
                shutil.rmtree(options.destination.rstrip("/")+"/"+remove_directory)

def main():
    print("Starting EasyBackup v"+version)
    parser_setup()
    options = validate()
    create_new_current(options)
    execute_backup(options)
    rotate_backups(options)
    print("Done.")

if __name__ == '__main__':
    main()
