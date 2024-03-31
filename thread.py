
import time

def get_thread(thread_name):
	time.sleep(1)
	print(f'{thread_name}')


for i in range(5):
	get_thread("yeaaah")
