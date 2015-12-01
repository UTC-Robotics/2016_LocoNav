# 2016_LocoNav
Navigation code for the 2016 robot.  Intended for execution on a Raspberry Pi Model 2 B system.  

## Program Structure: 
- main.py 
  - Main program file 
  - All others called, directly or indirectly, from within this file 
- HCSR04.py 
  - Contains the HCSR04 class for initializing each individual HCSR04 sensor 
  - This file is imported and used by Sensors.py. 
- Sensors.py 
  - This file actually does the creating of each HCSR04 object 
  - It is imported within main.py 
  - Each object it creates can then be used within main.py via the form: 'Sensors.ObjName.ObjFunc()' 
- Motors.py 
  - This file is on the to-do list as of 12/1/2015 
  - It should initialize all 4 DC motors similar to how the sensors are done in Sensors.py 
