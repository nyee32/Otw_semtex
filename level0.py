#!/bin/python

e = open("executable", "wb")

with open ("data", "rb") as f:
        other = True
        byte = f.read(1)
        while byte != "":
                if other:
                        e.write(byte)
                        other = False
                else:
                        other = True

                byte = f.read(1)
