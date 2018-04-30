from database import Database
import threading
import time
import sys
def run_job():
	print("run job {} time_sleep : {}".format(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
	run_job()

