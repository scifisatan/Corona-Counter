# Required python modules
import requests
from bs4 import BeautifulSoup
import sys

# Global Variables
choice = 0


# gives numbers based on given link
def stats(link):
    i = 0
    ok = ["Total number of cases: ", "Deaths: ", "Recovered: "]
    statistics = ""
    result = requests.get(link).content
    soup = BeautifulSoup(result, "html.parser")
    numbers = soup.findAll(id, "maincounter-number")
    try:
        while i < 3:
            statistics = statistics + (ok[i] + numbers[i].text.strip() + "\n")
            i += 1
        return statistics
    except IndexError:
        sys.exit("Invalid Input!\nPLease try again!\n")

# Determines the required link on the basis of user input
while choice == 0:
    choice = input("Which stats do you want to see?\n1)World\n2)Country\n")
    if choice == "1":
        url = "http://www.worldometers.info/coronavirus/"
    elif choice == "2":
        country = input("Enter Country: ").lower()
        if country == "usa":
            country == "us"
        if country =="uae":
            country = "united-arab-emirates"
        country = country.replace(" ","-")
        url = "http://www.worldometers.info/coronavirus/country/" + country
    elif choice != "1" and choice != "2":
        print("Invalid Input!!\nPlease try again!\n")
        choice = 0

try:
    print("\n" + stats(url))
except TypeError:
    sys.exit("Invalid Input!\nPLease try again!\n")
