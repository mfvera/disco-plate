# disco-plate
A quick and dirty regex tester for CO personalized license plates based on [DR 2810](https://dmv.colorado.gov/sites/dmv/files/documents/DR2810.pdf) (06/15/2023).

These tests do not take into account:
* Motorcycle plates
* Call Letter plates
* Plates containing spaces, periods, or dashes
* Profanity or any of the other subjective rules issued by the Colorado DMV
* Rules changed or added after 06/15/2023

## Usage examples
```
./main.py 0xBEEF
```

```
./main.py LIGMA
```