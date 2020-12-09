import datefinder
import winsound
import datetime
from plyer import notification

def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat) 
    stringA = str(mat) 
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA) 
    minuteA = timeA[3:-3]
    minuteA = int(minuteA) 
    

    while True:
        if hourA == datetime.datetime.now().hour:
            if minuteA == datetime.datetime.now().minute:
                print("Alarm is ringing") 
                winsound.PlaySound("./alarm.mp3",winsound.SND_LOOP)

            elif minuteA < datetime.datetime.now().minute:
                notification.notify(
                title = f"Alarm has rangup at {hourA} : {minuteA}", 
                message = "The alarm has been rang up.",
                app_icon = None,
                timeout = 50,  
            )
                break 

# alarm("Set alarm at 1:57 pm") 