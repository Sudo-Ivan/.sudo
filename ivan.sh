#!/bin/sh

figlet -f standard "Ivan Ryan"

#print the date
date

# print about myself
echo "I am cool"
sleep 1
echo "I am former military"
sleep 1
echo "I am a programmer"
sleep 2

# would you like to know more?
echo "Would you like to know more?"
sleep 1
echo "Yes or No"
sleep 1

# if yes then print more
read response
if [ "$response" = "Yes" ]; then
  echo "I am a programmer"
  sleep 1
  echo "I am a programmer"
  sleep 1
  echo "I am a programmer"
  sleep 2
elif [ "$response" = "No" ]; then
  echo "Goodbye"
  sleep 1
  exit
else
  echo "Invalid response. Goodbye."
  sleep 1
  exit
fi
