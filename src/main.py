#Include control class and instantiate
from GCE_helpers import GCE_control
GCE = GCE_control()

#Kill VM when script ends
import atexit
atexit.register(GCE.kill_vm)

#Use functions to send update emails and save objects as required
#GCE.save_output("anything") #Saves any object as pickle to Cloud Storage
#GCE.send_email_update("I'm fine") #Sends email update based on config data

#Your code here

GCE.send_email_update('Code within Docker Container launched successfully on Google Compute Engine')
GCE.save_output(GCE.gcepy_smtp_config)
