![alt text](https://github.com/ugcs/ddc/DroneShowSoftware_Logo.png "Drone Show Software")

Drone Show Software
=========

Drone Show Software is software designed for drone shows, allowing flight path planning as well as control of dozens of drones simultaneously in a synchronized manner.

This repository contains guidelines for building and setting up the drones, WiFi and LED modules as well as adding and setting up RTK GPS units.

Description
-----------

Drone Show Software requires a custom Pixhawk firmware due to special flight mode and commands it uses. Pixhawk hardware or copies thereof can be used. These autopilots are widely available and available for purchase from most drone part dealers.

Drones can be used with standard GPS units, but to ensure flight precision that is necessary for drone shows, we recommend using RTK GPS units.

For establishing reliable communication between multiple drones, we suggest using 5GHz WiFi modules onboard drones rather than standard (433MHz) telemetry data links.
For drone show purposes, drones can be equipped with LED modules or other show elements that can be controlled via PWM servo signal.

- [**Drone_hardware**](./Drone_hardware) contains all the information for assembling, manufacturing and configuring drones, WiFi modules and LED payloads.

 - [**3D_Printing**](./3D_Printing) contains STL files for 3D printing GPS and Flight controller cases.
 
 - [**Airborne 5GHz WiFi**](./Airborne_5GHz_WiFi) contains guidelines and schematics to assemble Airborne 5GHz WiFi modules.

 - [**Fireball LED payload**](./Fireball_LED_payload) contains guidelines and schematics to assemble Fireball LED payloads.

 - [**PCB-KiCad**](./PCB-KiCad) contains PCB source project files for [KiCad EDA](http://kicad-pcb.org/)

- [**Software_tools**](./Software_tools) contains all the necessary software tools to cofigure the drones and run the show.

 - [**DDC_ConfigTool**](./Software_tools/DDC_ConfigTool) this tool is used to easily upload fimrmware and do accelerometer and compass calibration on many drones.
 
 - [**Radio_updater**](./Software_tools/Radio_updater) used to upload 433MHz radio firmware to secondary channel telemetry data links.

 - [**RTK_Tool**](./Software_tools/RTK_Tool) used to broadcast RTK GPS corrections to the drones.

 - [**SITL_simulation**](./Software_tools/SITL_simulation) is used to perform simulated drone show flights.

- [**Animation_samples**](./Animation_samples) contains animation samples.




System requirements
-------------------

System requirements for Drone Show Software:

- *Operating system:* Windows 7 with SP1 or later; Windows 8; Windows 10.
- *CPU:* Intel Core i7 or better.
- *Memory:* Minimum 8 GB of RAM or more.
- *Hard drive:* SSD 120GB. Recommended 256GB or more.
- *Graphics hardware:* Graphics card with DirectX 9 support (shader model 2.0). Any card made since 2004 should work.
- *Network:* TCP/IPv4 network stack, WiFi or Ethernet. Recommended Ethernet.
- *Screen resolution:* FullHD screen.

Licence
-------

All contents except third party ones are licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Further information
-------------------

This repository is maintained by SPH Engineering, developers of UgCS ground control software for drones.

If you have any questions about this project, feel free to reach out to us at <support@ugcs.com>.
