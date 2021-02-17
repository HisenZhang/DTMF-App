import datetime

HOUR_OFFSET = -1
MINUTE_OFFSET = +2

def on_monitor(DTMFString: str) -> None:
    print("You entered: " + DTMFString)
    t = datetime.datetime.now()
    TOKEN = str(t.hour + HOUR_OFFSET).zfill(2) + \
            str(t.minute + MINUTE_OFFSET).zfill(2)
    if DTMFString == TOKEN:
        print("Access granted.")
    else:
        print("Access denied.")
    pass
