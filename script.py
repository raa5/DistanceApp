import requests
import smtplib
import streamlit as st

# API Key
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()

# Home address input
# home = input("Enter home address\n")
dummy_home = '406 Greenbriar Dr, Normal'

# Work address input
# work = input("Enter work address\n")
dummy_work = '100 Rivian Motorway, Normal'

# Base URL
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'

api_key = 'AIzaSyDfhBriP6OykNGfLxu0uvM20oijDsa5R7o'
# Get response
r = requests.get(url + "origins=" + dummy_home + "&destinations=" + dummy_work + "&key=" + api_key)
# print(r)

# Return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
miles = r.json()["rows"][0]["elements"][0]["distance"]["value"]

# print(r.json())
# Print the total travel time
# print("\nThe total travel time from home to work is = ", time)
print('\n The distance between ' + dummy_home + ' and ' + dummy_work + ' is ' + distance + '\n It will take ' + time)

# Display the result in Streamlit app
st.write(f'\n The distance between {dummy_home} and {dummy_work} is {distance}\n It will take {time}')
