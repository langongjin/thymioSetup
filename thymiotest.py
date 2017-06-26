#!/usr/bin/python
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
    for line in open("fo.txt"):
        int deriction = int(line)
        if line == 0:
            left = right  = deriction
        
        if line > 0:
            left = 0.5 * deriction
            right = 2 * deriction
            
        if line < 0:
            left = 2 * deriction
            right = 0.5 * deriction
        
        if line = 1000:
            left = right = deriction
        
        motorspeed = {'left':left, 'right':right}
        # Create Aseba network
        controller = dbus.Interface(bus.get_object('ch.epfl.mobots.Aseba', '/'),
                                    dbus_interface='ch.epfl.mobots.AsebaNetwork')
        controller.SetVariable("thymio-II", "motor.left.target", [motorspeed['left']])
        controller.SetVariable("thymio-II", "motor.right.target", [motorspeed['right']])
        print left, right
    time.sleep(0.1)
