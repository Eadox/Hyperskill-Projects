import os.path
from os import path, getcwd, chdir, listdir, stat, remove, rmdir, mkdir
from shutil import copy, move, rmtree

# run the user's program in our generated folders
chdir('module/root_folder')

print("Input the command\n")
while True:
    command = input()
    # Print working directory
    if command == 'pwd':
        print(getcwd())

    # Change directory
    elif command[:3] == 'cd ':
        try:
            chdir(command[3:])
            print(getcwd().rsplit(sep='\\')[-1])
        except FileNotFoundError:
            print("Invalid command")

    # Quit program
    elif command == 'quit':
        break

    # List directory
    elif command[:2] == 'ls':
        folders = [x for x in listdir() if '.' not in x]
        print(*folders, sep='\n')
        files = [x for x in listdir() if '.' in x]

        # List with size
        if command[3:] == '-l':
            for file in files:
                print(f"{file} {stat(file).st_size}")

        # List with size (human read-able)
        elif command[3:] == '-lh':
            for file in files:
                file_size = stat(file).st_size
                units = ['B', 'KB', 'MB', 'GB']
                unit_index = 0
                while file_size >= 1024:
                    file_size //= 1024
                    unit_index += 1
                print(f"{file} {file_size}{units[unit_index]}")

        else:
            print(*files, sep='\n')

    # Remove file or directory
    elif command[:3] == 'rm ':
        command_path = command[3:]
        # Bulk remove files with extension
        if command_path[0] == '.':
            file_list = [x for x in listdir() if x[-len(command_path):] == command_path]
            if file_list:
                for file in file_list:
                    remove(file)
            else:
                print(f"File extension {command_path} not found in this directory")
        # Remove single file or directory
        elif path.exists(command_path):
            if '.' in command_path:
                remove(command_path)
            else:
                try:
                    rmdir(command_path)
                except OSError:
                    rmtree(command_path)
        else:
            print("No such file or directory")
    elif command[:2] == 'rm':
        print("Specify the file or directory")

    # Move file or directory
    elif command[:3] == 'mv ':
        command_args = command[3:]
        if ' ' not in command_args:
            print("Specify the current name of the file or directory and the new location and/or name")
        else:
            name_old, name_new = command_args.split(' ')
            # Check if destination is a directory and source is file
            if '.' not in name_new and '.' in name_old and name_old[0] != '.':
                name_new += '/' + path.basename(name_old)
            if name_old[0] == '.':
                file_list = [x for x in listdir() if x[-len(name_old):] == name_old]
                for file in file_list:
                    if path.exists(name_new + '/' + file):
                        while True:
                            confirm = input(f"{file} already exists in this directory. Replace? (y/n)")
                            if confirm == 'y':
                                move(file, name_new + '/' + file)
                                break
                            elif confirm == 'n':
                                break
                    else:
                        move(file, name_new + '/' + file)
                else:
                    print(f"File extension {name_old} not found in this directory")
            elif not path.exists(name_old):
                print("No such file or directory")
            elif path.exists(name_new):
                print("The file or directory already exists")
            else:
                move(name_old, name_new)
    elif command[:2] == 'mv':
        print("Specify the current name of the file or directory and the new location and/or name")

    # Make new directory
    elif command[:6] == 'mkdir ':
        command_path = command[6:]
        if '\\' not in command_path:
            command_path = getcwd() + '/' + command_path
        if command_path.rsplit('/')[-1] in listdir():
            print("The directory already exists")
        else:
            mkdir(command_path)
    elif command[:5] == 'mkdir':
        print("Specify the name of the directory to be made")

    # Copies a file
    elif command[:3] == 'cp ':
        command_args = command[3:].split(' ')
        if len(command_args) != 2:
            print("Specify the current name of the file or directory and the new location and/or name")
        else:
            name_old, name_new = command_args
            if name_new == '..':
                name_new = os.path.split(getcwd())[0]
            if name_old[0] == '.':
                file_list = [x for x in listdir() if x[-len(name_old):] == name_old]
                for file in file_list:
                    if path.exists(name_new + '/' + file):
                        while True:
                            confirm = input(f"{file} already exists in this directory. Replace? (y/n)")
                            if confirm == 'y':
                                copy(file, name_new + '/' + file)
                                break
                            elif confirm =='n':
                                break
                    else:
                        copy(file, name_new + '/' + file)
                else:
                    print(f"File extension {name_old} not found in this directory")
            elif not path.exists(name_old):
                print("No such file or directory")
            elif path.exists(name_new):
                print(f"{path.basename(name_old)} already exists in this directory")
            else:
                copy(name_old, name_new)
    elif command[:2] == 'cp':
        print("Specify the file")

    # Input not a command, prompt again.
    else:
        print("Invalid command")
