import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "lvsOjYfGPm8KHqpvRUVwvNMOnAO8dTNf"

while True:
   orig = input("Lugar de inicio: ")
   if orig == "quit" or orig == "q":
    break
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
    break
   url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
   json_data = requests.get(url).json()
   print("URL: " + (url))
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
    print("API status:" + str(json_status) + " = Successful route call. \n")
    print("=============================================")
    print("Direcciones desde " + (orig) + " a " + (dest))
    print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
    print("Kilómetros: " + str ("{:.2f}" .format((json_data ["route"] ["distance"]) *1.61)))
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")