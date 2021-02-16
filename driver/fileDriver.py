'''
Author: HisenZhang <zhangz29@rpi.edu>
Date: 2020-12-26 00:02:22
LastEditors: HisenZhang <zhangz29@rpi.edu>
LastEditTime: 2020-12-26 00:47:10
Description: file content
'''

from driver.common import Driver
import time


class FileDriver(Driver):

    def __init__(self):
        super().__init__()
        self.CHUNK_SIZE = 4096
        pass

    def init(self, filename="input.txt") -> str:
        self.filename = filename
        self.f_ = None
        try:
            self.f_ = open(filename, "r")
            return filename
        except IOError:
            print("File IO failure")
            return "FAILED"

    def monitor(self,
                terminator="*"):
        buffer = self.f_.readline()
        if buffer:
            DTMFString = buffer.partition(terminator)[0].strip()
        else:
            return
        time.sleep(1)
        self.exec(DTMFString)

    def __del__(self):
        if self.f_ != None:
            self.f_.close()
