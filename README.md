# Dash Data Display Based on STM32 MCU

This SW shall output the collected data to the LCD controller via I2C/UART/CAN protocol- dependent on LCD display.


## Gathered Signals from MS II are: 

- Engine RPM
- Manifold air temperature
- Manifold air pressure
- Final ignition spark advance
- Battery voltage
- Oil Temperature from ADC GPIO
- Oil Pressure from ADC GPIO 

## Gathered Signals from Sensors directly are: 
- Vehicle Speed Signal 
- Oil Pressure 
- Oil Temperature


## Data that will be available on Display is : 

### Page one
- Engine RPM 
- Vehicle Speed 
- Calculated mileage 
- Trip Computer
### Page two 
- Oil Temperature 
- Oil Pressure 
- Manifold Air Temperature
- Manifold Air Pressure
- Battery voltage 

## Requirements 
- Requirements are available in(SRS document) ./Design/Requirements/SW_REQUIREMENT_SPECIFICATION_DOCUMENT.docx
## Architecture
- Architecture Diagrams are available in /Design/ArchitectureDiagrams/
