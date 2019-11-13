#!/bin/bash

function create(){
	echo "Creating..."
	pwd=$(pwd)
	cd ~/Workplace/Automation/DailyTasks/project_creation/
	python2 project_creation.py $1 $pwd
	cd $pwd/$1
	mkdir "github_repo"
	cd $pwd/$1/github_repo
	git clone https://github.com/username/$1.git
	cd $pwd/$1
	echo "Your project structure is ready."
}
