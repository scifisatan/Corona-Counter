# Required python modules
import requests
from bs4 import BeautifulSoup


# Global Variables
j = 0


# gives numbers based on given link
def stats(link):
    i = 0
    ok = ["Total number of cases: ", "Deaths: ", "Recovred: "]
    statistics = ""
    result = requests.get(link).content
    soup = BeautifulSoup(result, "html.parser")
    numbers = soup.findAll(id, "maincounter-number")
    while i < 3:
        statistics = statistics + (ok[i] + numbers[i].text.strip() + "\n")
        i += 1
    return statistics


# Determines the required link on the basis of user input
while j == 0:
    j = 1
    choice = input("Which stats do you want to see?\n1)World\n2)Country\n")
    if choice == "1":
        url = "http://www.worldometers.info/coronavirus/"
    elif choice == "2":
        country = input("Enter Country: ").lower()
        url = "http://www.worldometers.info/coronavirus/country/" + country
    else:
        j = 0


print("\n" + stats(url))
