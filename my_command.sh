#!/bin/bash

function create(){
	echo "Creating..."

	# contains current working directory
	pwd=$(pwd)

	# navigate to folder that contains our python file
	cd ~/Workplace/Automation/DailyTasks/project_creation/

	# run python file and passes two arguments proj_name and current working directory
	python2 project_creation.py $1 $pwd

  # navigate back to working directory
	cd $pwd/$1

	# create folder inside our project
	mkdir "github_repo"

	# navigate to git_repo folder
	cd $pwd/$1/github_repo

	# Run git commands
	git clone https://github.com/username/$1.git

	# Navigate to working directory
	cd $pwd/$1
	echo "Your project structure is ready."
}
