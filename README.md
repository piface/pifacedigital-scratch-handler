pifacedigital-scratch-handler
=============================

Allows Scratch to control PiFace Digital through MESH.

Install
=======

Make sure you are using the lastest version of Raspbian::

    $ sudo apt-get update
    $ sudo apt-get upgrade

Install `pifacedigital-scratch-handler` (for Python 3 and 2) with the
following command::

    $ sudo apt-get install python3-pifacedigital-scratch-handler

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
