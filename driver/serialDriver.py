'''
Author: HisenZhang <zhangz29@rpi.edu>
Date: 2020-12-23 17:25:14
LastEditors: HisenZhang <zhangz29@rpi.edu>
LastEditTime: 2020-12-26 00:42:58
Description: file content
'''

import serial
from driver.common import Driver


class SerialDriver(Driver):

    def init(self, port='/dev/ttyUSB0', baudrate=115200) -> str:
        self.ser = None
        try:
            self.ser = serial.Serial(port, baudrate)  # open serial port
            return self.ser.name        # check which port was really used
        except FileNotFoundError as e:
            print("Connection failed: " + str(e))

    def monitor(self,
                terminator="*"):
        terminator = terminator.encode('ascii')
        buffer = bytearray()
        try:
            buffer += self.ser.read_until(terminator)
            # if buffer[-1] != ord(terminator):
            #     raise ValueError("Unexpected terminator")
        except ValueError:
            print("Data incomplete")
        except serial.serialutil.SerialException:
            print("Serial port failure")

        DTMFString = buffer.decode('ascii')[:-len(terminator)]

        self.exec(DTMFString)

    def __del__(self):
        if self.ser:
            self.ser.close()
