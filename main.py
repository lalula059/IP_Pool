from multiprocessing import Process
from logger.log import logger,check_filename
import time
from scheduler import getter,examiner
def get():
    print(2)
def run():
    try:
            getter_er = Process(target=getter)
            check = Process(target=examiner)
            getter_er.start()
            check.start()
            getter_er.join()
            check.join()
    except KeyboardInterrupt as e:
       getter_er.close()
       check.close()
    finally:
        end_time =  time.time()
        logger.info("exit successful!!!!***********************time use {}!!".format(end_time-start_time))

if __name__ == "__main__":
    start_time = time.time()
    check_filename()
    run()
    
