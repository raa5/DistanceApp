import requests
import streamlit as st

# Read the API Key from the file
# with open("api-key.txt", "r") as api_file:
#     api_key = api_file.read()

# Home address input
home = st.text_input("Enter home address", '406 Greenbriar Dr, Normal')

# Work address input
work = st.text_input("Enter work address", '100 Rivian Motorway, Normal')

api_key = 'AIzaSyDfhBriP6OykNGfLxu0uvM20oijDsa5R7o'

# If the user has entered both addresses, proceed with the API request
if home and work:
    # Base URL
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'

    # Get response
    r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

    # Check if the request was successful
    if r.status_code == 200:
        # Parse the response
        data = r.json()
        # print(data)
        # Check if the response contains the required information
        if data["rows"] and data["rows"][0]["elements"] and data["rows"][0]["elements"][0]["status"] == "OK":
            # Extract travel time and distance
            time = data["rows"][0]["elements"][0]["duration"]["text"]
            distance = data["rows"][0]["elements"][0]["distance"]["text"]

            # Display the result in the Streamlit app
            st.write(f'You want to go between:  \n  {data["origin_addresses"][0]} to  \n {data["destination_addresses"][0]}.')
            st.write(f'The distance is {distance}.')
            st.write(f'It will take {time}.')
        else:
            st.write("Could not retrieve the distance and time. Please check the addresses and try again.")
    else:
        st.write("Error fetching data from Google Maps API.")
