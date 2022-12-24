#!/bin/sh

figlet -f standard "Get My Weather Bot Automatic Installation"

# print the date
date

# update and install python3
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Clone the repo
git clone https://github.com/Sudo-Ivan/GetMyWeather.git
cd GetMyWeather

# create a virtual environment for bot
python3 -m venv env
source env/bin/activate

# install bot dependencies
pip3 install -r requirements.txt

# set environment variables
echo "Enter the bot token:"
read token
echo "Enter the bot owner's ID:"
read owner
echo "Enter the application ID:"
read application_id
echo "Enter 'true' if you want to sync commands globally, or 'false' if not:"
read sync_commands_globally
echo "Enter your OpenWeatherMap API key:"
read OWM_API_KEY

export token=$token
export owner=$owner
export application_id=$application_id
export sync_commands_globally=$sync_commands_globally
export OWM_API_KEY=$OWM_API_KEY

echo "To stop the bot, use the 'CTRL + C' keyboard shortcut in the terminal window where the bot is running. Alternatively, you can use the 'kill' command to stop the bot by specifying the process ID of the bot. For example: 'kill <process ID>"

#start the bot in the background
nohup python3 bot.py &

#display a message indicating that the bot has been started
echo "Get My Weather Bot has been started in the background."
