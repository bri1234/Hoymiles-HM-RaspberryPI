# Python code to query status information from Hoymiles HM inverters using a Raspberry PI

This Python code should work with: Hoymiles HM-300, HM-350, HM-400, HM-600, HM-700, HM-800, HM-1200 and HM-1500 inverters.

(Only HM-600 is tested!)

## Hardware

You need:

- nRF24L01+ radio module (+!)
- Raspberry PI

## Pin connections

| RPI Pin | RPI Signal              | nRF24 Pin | nRF24 Signal |
| ------- | ----------------------- | --------- | ------------ |
| 17      | +3.3V                   | 2         | +3.3V        |
| 18      | GPIO 24 (Output)        | 3         | CE (Input)   |
| 19      | MOSI, GPIO 10 (Output)  | 6         | MOSI         |
| 20      | GND                     | 1         | GND          |
| 21      | MISO, GPIO 9 (Input)    | 7         | MISO         |
| (22)    | GPIO 25 (Input)         | (8)       | IRQ          |
| 23      | SCLK, GPIO 11 (Output)  | 5         | SCLK         |
| 24      | CS0, GPIO 8 (Output)    | 4         | CSN          |

- connection from Raspberry PI pin 22 to nRF24L01+ IRQ pin 8 is not necessary
- nRF24L01+ CE pin 3 can be connected to an other Raspberry PI GPIO pin 

## Python software modules

This Python code needs the **pyrf24** module for communication.
Install the module with the following line:

python -m pip install pyrf24

(see https://github.com/nRF24/pyRF24)

## Usage

```python
from HoymilesHmDtu import HoymilesHmDtu

CSn = 0
CE = 24

hm = HoymilesHmDtu("1141xxxxxxxx", CSn, CE)

hm.InitializeCommunication()
success, info = hm.QueryInverterInfo()

print(f"success: {success}")
HoymilesHmDtu.PrintInverterInfo(info)
```


