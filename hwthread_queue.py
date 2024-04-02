from multiprocessing import Pool
import time
import sys

sys.set_int_max_str_digits(4300000)
def thread_function(name):
	
	a = 300**3000000
	if __name__ == '__main__':
		start_time = time.time()
		with Pool(processes=3) as executor:
			
			executor.map(thread_function,range(3))
			duration = time.time() - start_time
			print(duration,'Legolegolego')



def q_function(name):
	a =300**3000000

	
	
	
	if __name__=='__main__':
		start_time = time.time()
		
		for i in range(3):
			q_function()
			print(a)
			print('queue')
			duration == time.time() - start_time
			print(duration, 'queue')


thread_function('name')

q_function('name')
		

