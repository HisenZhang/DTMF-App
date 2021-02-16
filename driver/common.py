'''
Author: HisenZhang <zhangz29@rpi.edu>
Date: 2020-12-23 18:36:34
LastEditors: HisenZhang <zhangz29@rpi.edu>
LastEditTime: 2020-12-25 23:52:04
Description: file content
'''

import os
import importlib


class Driver(object):
    def __init__(self):
        self.handlers_ = []
        pass

    def init(self) -> str:
        pass

    def monitor(self, terminator: str) -> None:
        pass

    def set_handler(self, func):
        if callable(func):
            self.handlers_.append(func)
        else:
            raise TypeError("Handler must be callable")

    def get_handler(self):
        return self.handlers_

    def del_handler(self):
        del self.handlers

    handlers = property(get_handler, set_handler, del_handler)

    def extendHandler(self, funcs) -> None:
        for f in funcs:
            self.set_handler(f)

    def removeHandler(self, func) -> None:
        self.handlers_.remove(func)

    def exec(self, DTMFString: str) -> None:
        if self.handlers_:
            for func in self.handlers_:
                func(DTMFString)
        else:
            return

    def __del__(self):
        pass


class DriverFactory(object):

    @classmethod
    def newConnection(cls, conn: str) -> object:
        moduleName = conn + "Driver"
        className = conn.title() + "Driver"
        try:
            module_ = importlib.import_module("." + moduleName,
                                              package=__package__)
            class_ = getattr(module_, className)
            return class_()
        except ModuleNotFoundError:
            print("Driver not found")
