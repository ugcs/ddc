UgCS DDC
=========

UgCS DDC (Drone Dance Controller) is software designed for drone shows, allowing flight path planning as well as control of dozens of drones simultaneously in a synchronized manner.

This repository contains guidelines for building and setting up the drones, adding and setting up RTK GPS units, WiFi and LED modules.

Description
-----------

UgCS DDC requires MAVLink – compatible autopilot running ArduCopter firmware. Pixhawk or copies thereof can be used. These autopilots are widely available and available for purchase from most drone spare part dealers.

Drones can be used with standard GPS units, but to ensure flight precision that is necessary for drone shows, we recommend using RTK GPS units.

For establishing reliable communication between multiple drones, we suggest using WiFi modules onboard drones rather than standard telemetry data links.
For drone show purposes, drones can be equipped with LED modules or other show elements that can be controlled via PWM servo signal.

- [**DDC**](./DDC) contains manuals regarding the setup and use of UgCS DDC software

- [**Drone**](./Drone) contains guidelines for drone assembly, including the mounting and setup of RTK GPS system

- [**LED**](./LED) contains the schematics and bill of materials for building LED modules that are used in drone shows

- [**WiFi**](./WiFi) contains information regarding setting up WiFi modules which enable simultaneous communication between the drones and the ground station

System requirements
-------------------

System requirements for UgCS DDC are the same as system requirements for UgCS:

- *Operating system:* Windows 7 with SP1 or later; Windows 8; Windows 10
- *CPU:* Core 2 Duo or Athlon X2 at 2.4 GHz or better
- *Memory:* Minimum 2 GB of RAM, Recommended: 4 GB of RAM or more
- *Hard drive:* 2 GB of free space
- *Graphics hardware:* Graphics card with DirectX 9 support (shader model 2.0). Any card made since 2004 should work.
- *Network:* TCP/IPv4 network stack
- *Screen resolution:* Minimum supported screen resolution: 1024x768

Further information
-------------------

This repository is maintained by SPH Engineering, developers of UgCS ground control software for drones.

If you have any questions about this project, feel free to reach out to us at <support@ugcs.com>
