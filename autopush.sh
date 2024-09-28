#!/bin/bash

format_name() {
    echo "$1" | sed 's/ //; s/ /_/g; s/$/.py/'
}

read -p "Enter the problem name: " problem_name

formatted_name=$(format_name "$problem_name")

nano "$formatted_name"

read -p "Do you want to push to GitHub? (y/n): " push_choice

if [ "$push_choice" == "y" ]; then
    git add .
    git commit -m "$(date +%d)/$(date +%m)/$(date +%y)"
    git push origin main
else
    echo "File name: $formatted_name"
    echo "Exiting script"
fi
