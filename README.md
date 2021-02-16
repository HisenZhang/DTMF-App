# DTMF App Demo

## Dependencies

```bash
pip install pyserial
```

## Configure

Depending on your situation, you may want to read data from serial port or a file. You need to configure it before running the demo.

In source code:

```py
conn = DriverFactory.newConnection("file")
print("Connection: " + conn.init(FILE) + "\n=========\n")
# conn = DriverFactory.newConnection("serial")
# print("Connection: " + conn.init(PORT) + "\n=========\n")
```

Uncomment the code and modify the parameter for connection initialization:

```py
FILE = "test/ascii.txt" # modify to fit your situation
PORT = "COM3"
```

## Run

You need **python3** to run demo xxx:

``` bash
python demo_xxx.py
```