# Desription

LogHawk is a Python-based log monitoring tool developed as part 
of the Lighthouse Labs Bootcamp Project. It monitors various system 
logs (application, system, authorization, and access logs) for suspicious 
activities and potential security threats. When suspicious logs are 
detected, they are recorded in a comprehensive log file (comp_log.txt) 
for further analysis.

# ⚠️ Thr Purpose Of This Script

This scrit is intended simply as an idea of how one can Monitor Log FIles. It's NOT for Use 
in a Security Environment!

# Features

✅ Real-time monitoring of multiple log types

✅ Customizable detection rules for suspicious activities

✅ Automated alert generation

✅ CRON job integration for periodic execution

✅ Comprehensive log recording for security analysis

# Installation 💻

Ensure Python 3.x is installed

Command: python3 --version

Install Python 3.X

Command: sudo apt-get install python3

# Usage

Running the script directly

Command: python3 log_hawk_proj.py

# Setting Up A Cron Job 

Automated execution every 10 minutes.

Command: */10 * * * * /usr/bin/python3 (path to the script file)/log_hawk_proj.py

# Customization

Inside the def main() function add the path to your Access log file, Application file, Auth log file and System Log file.

def main():

ACCESS LOG PATH

access_path = "/media/sf_shared/access.log"

APPLICATION LOG PATH

app_path = "/media/sf_shared/app.log"

AUTHENTICATION LOG PATH

auth_path = "/media/sf_shared/auth.log"

SYSTEM LOG PATH

system_path = "/media/sf_shared/system.log"

# Dependancies

✅Python 3.x

✅Standard Python libraries (re, os, datetime)

# License 📝

# 🛑Use the Script at your own Risk!🛑 Dsec
