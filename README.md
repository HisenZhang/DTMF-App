# DTMF & HT Demo

This repository contains scripts demonstrate the idea presented in the [slides](https://docs.google.com/presentation/d/16PgaLe9n_umzwc4KC0pZJrMLSsOOJjpf2uFMVxoyk9M/).

- `demo_pwd.py` simulates a HT entering password. Inputs other than "5288" will be rejected.
    ```text
    You entered: 5288
    Access granted.
    You entered: 588
    Access denied.
    You entered: 4321
    Access denied.
    ```
- `demo_dynamic.py` enhances safety by adopting time-variant password.
- `demo_automobile.py` uses your HT as a car key (with plenty of cool features).
    ```text
    You entered: 0
    Opeartion code: 0 Action: lock
    Parameter:
    Car is LOCKED now.
    You entered: 1
    Opeartion code: 1 Action: unlock
    Parameter:
    Car is UNLOCKED now.
    You entered: 4
    Opeartion code: 4 Action: panic
    Parameter:
    *** Alarm sets off ***
    You entered: 9
    Undefined operation
    You entered: 2#D0
    Opeartion code: 2 Action: window_control
    Parameter: D0
    Rear Right window(s) now DOWN
    You entered: 2#01
    Opeartion code: 2 Action: window_control
    Parameter: 01
    ALL window(s) now UP
    ```
- `demo_ascii.py` interprets input as ASCII characters. Yes, you can "text" on HTs.
    ```text
    You entered:  41 42 43 44
    Translates to: ABCD
    You entered:  48 65 6c 6c 6f 20 77 6f 72 6c 64 21
    Translates to: Hello world!
    You entered:  44 45 20 4b 44 32 54 41 49
    Translates to: DE KD2TAI
    You entered:  0a 59 38 38 62 20 20 20 20 20 20 20 20 20 2f 20 20 2f 7e 7e 38 38 62 20 2c 64 38 38 7e 7e 5c 20 20 7e 7e 7e 7e 64 38 38 50 20 0a 20 59 38 38 62 20 20 20 20 20 20 20 2f 20 20 7c 20 20 20 38 38 38 20 38 38 38 38 20 20 20 20 20 20 20 20 64 38 38 50 20 20 0a 20 20 59 38 38 62 20 20 65 20 20 2f 20 20 20 60 20 20 64 38 38 50 20 60 59 38 38 62 20 20 20 20 20 20 64 38 38 50 20 20 20 0a 20 20 20 59 38 38 62 64 38 62 2f 20 20 20 20 20 20 64 38 38 50 20 20 20 60 59 38 38 62 2c 20 20 20 64 38 38 50 20 20 20 20 0a 20 20 20 20 59 38 38 59 38 59 20 20 20 20 20 20 64 38 38 50 20 20 20 20 20 20 38 38 38 38 20 20 64 38 38 50 20 20 20 20 20 0a 20 20 20 20 20 59 20 20 59 20 20 20 20 20 20 64 38 38 50 5f 5f 5f 20 5c 5f 5f 38 38 50 27 20 64 38 38 50 5f 5f 5f 5f 20 20 20 20 20
    Translates to:
    Y88b         /  /~~88b ,d88~~\  ~~~~d88P
     Y88b       /  |   888 8888        d88P
      Y88b  e  /   `  d88P `Y88b      d88P
       Y88bd8b/      d88P   `Y88b,   d88P
        Y88Y8Y      d88P      8888  d88P
        Y  Y      d88P___ \__88P' d88P____
    ```

- `demo_image.py` transmits image in PPM format. Find your output image in `output/` subdirectory.
    ```text
    You entered:  50 31 20 33 20 32 0a 31 20 30 20 31 20 30 20 31 20 30
    Translates to: P1 3 2
    1 0 1 0 1 0
    You entered:  50 33 20 34 20 34 20 31 35 0a 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 31 35 20 30 20 31 35 0a 30 20 30 20 30 20 30 20 31 35 20 37 20 30 20 30 20 30 20 30 20 30 20 30 0a 30 20 30 20 30 20 30 20 30 20 30 20 30 20 31 35 20 37 20 30 20 30 20 30 0a 31 35 20 30 20 31 35 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30 20 30
    Translates to: P3 4 4 15
    0 0 0 0 0 0 0 0 0 15 0 15
    0 0 0 0 15 7 0 0 0 0 0 0
    0 0 0 0 0 0 0 15 7 0 0 0
    15 0 15 0 0 0 0 0 0 0 0 0
    ```

## Install Dependencies

```bash
pip install pyserial
```

## Configure

For demonstration purpose, the default input are files. Depending on your situation, you may want to read data from the serial port or a file.

The serial port input expect characters sent from arduino with MT8870. Here's a [sample program](https://electropeak.com/learn/interfacing-mt8870-dtmf-decoder-module-with-arduino/) for your reference. It can be easily modified for out purpose.

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