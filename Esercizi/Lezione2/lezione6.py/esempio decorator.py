def get_time(func):    
    def wrapper(): 
        import time 
        import random 

        start= time.time()  
        func()  
        end= time.time()    
        elapsed_time= end - start   
        print(f"{elapsed_time=}")  

    return wrapper 
@get_time
def say_hello()   -> None:  
    print(f"hello, Mary")   

say_hello=get_time(say_hello)  

say_hello()

