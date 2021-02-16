def lock(param):
    print("Car is LOCKED now.")

def unlock(param):
    print("Car is UNLOCKED now.")

window_code = {
    "0":"ALL",
    "A":"Front Left",
    "B":"Front Right",
    "C":"Rear Left",
    "D":"Rear Right"
}
movement = ["DOWN","UP"]

def window_control(param):
    print(window_code[param[0]] + " window(s) now " + movement[int(param[1])])

def panic(param):
    print("*** Alarm sets off ***")

menu = {
    "0":("lock",lock),
    "1":("unlock",unlock),
    "2":("window_control",window_control),
    "4":("panic",panic)
}

def on_monitor(DTMFString: str) -> None:

    opcode,_,param = DTMFString.partition("#")
    print("You entered: " + DTMFString)
    if opcode not in menu:
        print("Undefined operation")
        return
    print("Opeartion code: " + opcode + " Action: " + menu[opcode][0])
    print("Parameter: " + param)
    menu[opcode][1](param)
