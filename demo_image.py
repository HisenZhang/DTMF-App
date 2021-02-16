from driver.common import DriverFactory
from handler import image

FILE = "test/image.txt"
PORT = "COM3"

conn = DriverFactory.newConnection("file")
print("Connection: " + conn.init(FILE) + "\n=========\n")
# conn = DriverFactory.newConnection("serial")
# print("Connection: " + conn.init(PORT) + "\n=========\n")

conn.handlers = image.on_monitor
   
while True:
    conn.monitor("#*")
