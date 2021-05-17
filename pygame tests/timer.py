import threading

global T

def timecounter(count):

    global T 
    
    T = count

    Time = threading.Timer(1.0, countDown, args=None, kwargs=None)
    Time.start()
   

def countDown():

    global T
    T = T - 1

    if T > 0:
        Time = threading.Timer(1.0, countDown, args=None, kwargs=None)
        Time.start()
      


