UgCS DDC
=========

UgCS DDC (Drone Dance Controller) is software designed for drone shows, allowing flight path planning as well as control of dozens of drones simultaneously in a synchronized manner.

This repository contains guidelines for building and setting up the drones, adding and setting up RTK GPS units, WiFi and LED modules.

Description
-----------

UgCS DDC requires the custom Pixhawk firmware due to special flight mode and commands it uses. Pixhawk hardware or copies thereof can be used. These autopilots are widely available and available for purchase from most drone spare part dealers.

Drones can be used with standard GPS units, but to ensure flight precision that is necessary for drone shows, we recommend using RTK GPS units.

For establishing reliable communication between multiple drones, we suggest using WiFi modules onboard drones rather than standard telemetry data links.
For drone show purposes, drones can be equipped with LED modules or other show elements that can be controlled via PWM servo signal.

- [**Animation_generator**](./Animation_generator) contains drone dance trajectory generation User Guide.

- [**Animation_samples**](./Animation_samples) contains animation samples.

- [**Datalink**](./Datalink) contains information regarding setting up WiFi modules which enable simultaneous communication between the drones and the ground station

- [**DDC**](./DDC) contains manuals regarding the setup and use of UgCS DDC software and running SITL User Guide.

- [**Drone**](./Drone) contains guidelines for drone assembly, including the mounting and setup of RTK GPS system

- [**LED**](./LED) contains the schematics and bill of materials for building LED modules that are used in drone shows

- [**PCB-KiCad**](./PCB-KiCad) contains PCB source project files for [KiCad EDA](http://kicad-pcb.org/)



System requirements
-------------------

System requirements for UgCS DDC are the same as system requirements for UgCS:

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

If you have any questions about this project, feel free to reach out to us at <support@ugcs.com>
