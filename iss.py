#!/usr/bin/env python

__author__ = 'Tiree help from  Howard the coach.'

import json
import turtle
import requests
import time


def getastronauts():

    # A first JSON request to retrieve the name of all the astronauts currently in space.
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    result = json.loads(response.text)
    print("There are currently " +
          str(result["number"]) + " astronauts in space:")
    print("")

    people = result["people"]

    for p in people:
        print(p["name"] + " on board of " + p["craft"])


def isslocation():
    # Display information on world map using Python Turtle
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    # Load the world map picture
    screen.bgpic("map.gif")

    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()
    indylocation()

    while True:
        # A JSON request to retrieve the current longitude and latitude of the IIS space station (real time)
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        result = json.loads(response.text)

        # Let's extract the required information
        location = result["iss_position"]
        lat = float(location["latitude"])
        lon = float(location["longitude"])

        # Output informationon screen
        print("\nLatitude: " + str(lat))
        print("Longitude: " + str(lon))

        # Plot the ISS on the map
        iss.goto(lon, lat)
        # refresh position every 5 seconds
        time.sleep(5)


def indylocation():
    indy = turtle.Turtle()
    indy.shape("circle")
    indy.turtlesize(.5, .5, .5)
    indy.color("blue")
    indy.penup()
    indy.goto(-86.159536, 39.778117)
    payload = {"lat": 39.778117, "lon": -86.159536}
    response = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=payload)
    result = json.loads(response.text)
    next_time = time.ctime(result["response"][0]["risetime"])
    indy.write(next_time)

def main():
    getastronauts()
    isslocation()


if __name__ == '__main__':
    main()
