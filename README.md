pifacedigital-scratch-handler
=============================

Allows Scratch to control PiFace Digital through MESH.

Depends on [pifacedigitalio](https://github.com/piface/pifacedigitalio).

Usage
=====
First you must [enable Mesh in
Scratch](http://wiki.scratch.mit.edu/wiki/Mesh#Mesh_by_Modification_of_Scratch).

The shift-click the *Share* menu-item and select *Host Mesh*.

Now run the scratch\_handler: 

    $ python3 scratch_handler.py

Use the **-e** flag to use the scratch\_handler with the PiFace Digital Emulator
instead of PiFace Digital (if you have it installed).

Scratch
-------
The handler will make available inputs 1 through 8 via the sensor values. If
you want to control PiFace Digital's outputs you must create a variable for
each pin named like so:

    piface-output1
    piface-output2
    piface-output3
    piface-output4
    piface-output5
    piface-output6
    piface-output7
    piface-output8
