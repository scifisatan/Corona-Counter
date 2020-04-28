import http.client
import sys

country = input("Enter country: ")
conn = http.client.HTTPSConnection("covid-19-coronavirus-statistics.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "82165ec616mshce45ef7984e1025p1f2a8djsn6ab4cd3e54fa"
    }

conn.request("GET", f"/v1/stats?country={country}", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

Confirmed_Cases = str(data[data.find("confirmed")+11:data.find(",",data.find("confirmed"))])
Deaths = str(data[data.find("deaths")+8:data.find(",", data.find("deaths"))])
Recovered = str(data[data.find("recovered")+11:data.find("}", data.find("recovered"))])
Last_Updated = str(data[data.find("lastUpdate")+13:data.find(",", data.find("lastUpdate"))])

print("Total Cases: "+Confirmed_Cases)
print("Total Deaths: "+Deaths)
print("Total Recovered: "+Recovered)
print("Last updated on \"" + Last_Updated)
sys.exit()
