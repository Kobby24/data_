import requests
from datetime import datetime
import pywhatkit


MY_LAT = 5.603717
MY_LNG = -0.186964

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.




parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
hour_now = int(time_now.hour)
min_now = int(time_now.minute)


#If the ISS is close to my current position
if iss_latitude >= 46.0 or iss_latitude <= 56.0:
    if iss_longitude >= -5.0 or iss_longitude <= 4.8:
        if sunset <= hour_now <= sunrise:
            pywhatkit.sendwhatmsg("+233592857226",
                                  "Look up the satellite is above you",
                                  hour_now,
                                  min_now)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



