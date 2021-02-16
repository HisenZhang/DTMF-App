import codecs
import time

def on_monitor(DTMFString: str) -> None:
    print("You entered: ", ' '.join(
        [(DTMFString[i:i+2]) for i in range(0, len(DTMFString), 2)]
    )) # GROUP BY BYTES
    DTMFString = DTMFString.replace("*","E").replace("#","F")
    try: 
        ASCIIString = codecs.decode(DTMFString, "hex").decode("ascii")
        print("Translates to: " + ASCIIString)
        with open("output/image"+str(int(time.time()))+".ppm",'w+') as f:
            f.write(ASCIIString)        
    except:
        print("Bad encoding.")