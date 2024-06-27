def decorator(func):    
    def wrapper(): 
        import time 

        start= time.time()  
        func()  
        end= time.time()    
        elapsed_time= end - start   
        print(f"{elapsed_time=}")  

    return wrapper 

def say_hello()   -> None:  
    print(f"hello, Mary")   

say_hello=decorator(say_hello)  

say_hello()
