'''
Author: HisenZhang <zhangz29@rpi.edu>
Date: 2020-12-23 17:27:16
LastEditors: HisenZhang <zhangz29@rpi.edu>
LastEditTime: 2020-12-26 00:38:56
Description: file content
'''

TOKEN = "5288"

def on_monitor(DTMFString: str) -> None:
    print("You entered: " + DTMFString)
    if DTMFString == TOKEN:
        print("Access granted.")
    else:
        print("Access denied.")
    pass
