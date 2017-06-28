#!/usr/bin/python
import os
import dbus
import dbus.mainloop.glib
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--system", action="store_true", dest="system", default=False,help="use the system bus instead of the session bus")
(options, args) = parser.parse_args()
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

if options.system:
    bus = dbus.SystemBus()
else:
    bus = dbus.SessionBus()

while True:
    if os.path.getsize("fo.txt"):
        for line in open("fo.txt"):
            ideriction = int(line)
            if deriction == 0:
                left = right  = 100

            if deriction > 0:
                left = 25 + 0.2 * deriction
                right = 50 + 0.4 * deriction

            if deriction < 0:
                left = 50 - 0.4 * deriction
                right = 25 - 0.2 * deriction

            if deriction = 1000:
                left = right = 0

            if deriction = 2000:
                left = 0
                right = 100

            motorspeed = {'left':left, 'right':right}
            # Create Aseba network
            controller = dbus.Interface(bus.get_object('ch.epfl.mobots.Aseba', '/'),
                                        dbus_interface='ch.epfl.mobots.AsebaNetwork')
            controller.SetVariable("thymio-II", "motor.left.target", [motorspeed['left']])
            controller.SetVariable("thymio-II", "motor.right.target", [motorspeed['right']])
            print left, right
    else:
        print "command is NULL"

    time.sleep(0.1)
