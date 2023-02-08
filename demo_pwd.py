from driver.common import DriverFactory
from handler import pwd

FILE = "test/pwd.txt"
PORT = "COM3"

conn = DriverFactory.newConnection("file")
print("Connection: " + conn.init(FILE) + "\n=========\n")
# conn = DriverFactory.newConnection("serial")
# print("Connection: " + conn.init(PORT) + "\n=========\n")

conn.handlers = pwd.on_monitor
   
while True:
    conn.monitor()
