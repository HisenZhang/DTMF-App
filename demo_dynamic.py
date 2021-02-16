from driver.common import DriverFactory
from handler import dynamic

FILE = "test/dynamic.txt"
PORT = "COM3"

# conn = DriverFactory.newConnection("file")
# print("Connection: " + conn.init(FILE) + "\n=========\n")
conn = DriverFactory.newConnection("serial")
print("Connection: " + conn.init(PORT) + "\n=========\n")

conn.handlers = dynamic.on_monitor
   
while True:
    conn.monitor()
