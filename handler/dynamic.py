import datetime

def on_monitor(DTMFString: str) -> None:
    print("You entered: " + DTMFString)
    t = datetime.datetime.now()
    TOKEN = str(t.hour).zfill(2) + str(t.minute).zfill(2)
    if DTMFString == TOKEN:
        print("Access granted.")
    else:
        print("Access denied.")
    pass
