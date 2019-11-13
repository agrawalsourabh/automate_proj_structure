#!/usr/bin/env python
import argparse
import os
from git_repo import Git_Repo


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("proj_name", help="Enter project name")
    parser.add_argument("proj_dir", help="Enter project directory.")

    args = parser.parse_args()

    print("Creating project structure...")
    path = args.proj_dir + '/' + args.proj_name
    makeProj(path, args.proj_name)

    # Creating Git Repo
    my_repo = Git_Repo('agrawalsourabh', 'Sourabh@12345@', args.proj_name)


# ---------- Creating Project Directory ---------------------

def makeProj(folder, file_name):
    file_path = folder + '/' + file_name + '.py'

    # ---------- If project is not present ---------------------
    if not os.path.exists(folder):
        print("Creating project directory....")
        os.makedirs(folder)
        print("Project directory created.")

        print("Creating python file....")
        makeFile(file_path)
        print("Python file created.")


    else:
        print("Project already exists.")


# ---------- Creating Python File empty ---------------------

def makeFile(file_path):
    open(file_path, 'a').close()


if __name__ == '__main__':
    Main()
