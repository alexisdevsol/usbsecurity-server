# How

usbsecurity-server is the server program to control access to USB ports.

# Installation

pip3 install usbsecurity-server

# Usage

Is a console program and runs like a fiend. To get it running open a terminal and run the following command:

$ usbsecurity-server

## Local

By default the application runs in local mode using the localhost, or the ip address 127.0.0.1 and port 8888. These parameters are user configurable.

## Server

In administration environments it would be good to have a single server that manages all permissions on the network.
You can configure the application to serve from any IP address and port just install it on the server machine and configure it:

usbsecurity-server --host _ip_address_ --port _port_

You have a single server to manage access permissions to the USB ports of the computers in your network.

### Admin

The application is administered through the browser by accessing the URL:

http[s]://_host_:_port_/admin

user: admin; pass: usbsecurity

_Users can change the password at any time._

# Help

$ usbsecurity-server -h | --help

