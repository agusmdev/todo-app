#!/bin/bash -e
# 
# Hacer setup para desarrollo local

# Configure Git task
IFS= read -r -p "Enter task name (e.g. John Doe): " name
IFS= read -r -p "Enter task e-mail (e.g. john.dow@gmail.com): " email

git config task.name "$name"
git config task.email "$email"

# Give execution permissions to commands
chmod +x commands/*
