pifacedigital-scratch-handler
=============================

Allows Scratch to control PiFace Digital through MESH.

Install
=======

Download the latest release of the scratch handler from
[here](https://github.com/piface/pifacedigital-scratch-handler/releases) and
install with:

    $ sudo dpkg -i python3-pifacedigital-scratch-handler_2.0.1-1_all.deb

You may also need to install [pifacedigitalio](https://github.com/piface/pifacedigitalio) first.

Use
===
First you must [enable Mesh in
Scratch](http://wiki.scratch.mit.edu/wiki/Mesh#Mesh_by_Modification_of_Scratch).

The shift-click the *Share* menu-item and select *Host Mesh*.

Now run the scratch handler:

    $ pifacedigital-scratch-handler

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

Here is an [image](http://i.imgur.com/2Xpb7k4.png) of a example Scratch program.
