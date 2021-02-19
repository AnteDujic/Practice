
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.php
# https://www.w3schools.com/python/python_datetime.asp

import datetime

today = datetime.datetime.now()


print (today.strftime("%u"))


if (int ((today.strftime("%u"))) > 5):
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday. :( ")

print (today.strftime("%w"))

if (int ((today.strftime("%w"))) > 5):
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday. :( ")
    
    