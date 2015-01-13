#!/bin/sh
R CMD Rserve --RS-source startup.R
sudo python server.py
