from multiprocessing import Pool
import time



def thread_function(name):	
	a = 3**300
	if __name__ == '__main__':
		start_time = time.time()
		with Pool(processes=3) as executor:	
			executor.map(thread_function,range(3))
			duration = time.time() - start_time
			print(duration*10000000,'Legolegolego')

thread_function('name')


		

