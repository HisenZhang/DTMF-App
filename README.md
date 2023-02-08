# DTMF & HT Demo

This repository contains scripts demonstrate the idea presented in the [slides](https://docs.google.com/presentation/d/16PgaLe9n_umzwc4KC0pZJrMLSsOOJjpf2uFMVxoyk9M/).

- `demo_pwd.py` simulates a HT entering password. Inputs other than "5288" will be rejected.
- `demo_dynamic.py` enhances safety by adopting time-variant password.
- `demo_automobile.py` uses your HT as a car key (with plenty of cool features).
- `demo_ascii.py` interprets input as ASCII characters. Yes, you can "text" on HTs.
- `demo_image.py` transmits image in PPM format. Find your output image in `output/` subdirectory.

The serial port expect characters sent from arduino with MT8870. Here's a [sample program](https://electropeak.com/learn/interfacing-mt8870-dtmf-decoder-module-with-arduino/) for your reference. It can be easily modified for out purpose.

## Install Dependencies

```bash
pip install pyserial
```

## Configure

For demonstration purpose, the default input are files. Depending on your situation, you may want to read data from the serial port or a file.

In source code, uncomment the code and modify parameters for connection initialization:

```py
conn = DriverFactory.newConnection("file")
print("Connection: " + conn.init(FILE) + "\n=========\n")
# conn = DriverFactory.newConnection("serial")
# print("Connection: " + conn.init(PORT) + "\n=========\n")

# modify parameters below
FILE = "test/ascii.txt" 
PORT = "COM3"
```

## Run

You need **python3** to run demo xxx:

``` bash
python demo_xxx.py
```