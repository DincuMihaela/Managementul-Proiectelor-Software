
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)

counter = 0

eventcount = 0

while(1):

    event = GPIO.input(7)

    if(event):

        eventcount += 1

        event = 0

        time.sleep(1.5)

    time.sleep(1)

    counter += 1

    if(counter==10):

        print(eventcount)

        events.save_value({'value':eventcount})

        counter = 0

        eventcount = 0
