from multiprocessing import Pool
import time

def q_function(x):
	for i in range(x):
		start_time = time.time()
		a =3**300
		finish_time = time.time()
		duration = finish_time - start_time
		print(int(duration*1000000), 'queue')
q_function(3)

