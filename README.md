Baseball-Integer-Program
========================

A tool to generate a draft team using integer programming

baseball.mod
------------
This is where the IP is modelled. It is written using the AMPL language.

generate_data_file.py
---------------------
This file contains one function, *generate_data_file(input, output)*. It takes the contents of *input*, which is assumed to be a .csv, and creates an AMPL data file called *baseball.dat*.

make_team.py
------------
This script facilitates the making of a draft team in 1 command with the input (and possibly output) file specified in the command line. It calls *generate_file_data*, then makes an external call to *glpsol*. The output is written to a file.
