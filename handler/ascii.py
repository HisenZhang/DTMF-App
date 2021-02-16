import codecs

def on_monitor(DTMFString: str) -> None:
    print("You entered: ", ' '.join(
        [(DTMFString[i:i+2]) for i in range(0, len(DTMFString), 2)]
    )) # GROUP BY BYTES
    DTMFString = DTMFString.replace("*","E").replace("#","F")
    try: 
        print("Translates to: " + codecs.decode(DTMFString, "hex").decode("ascii"))
    except:
        print("Bad encoding.")