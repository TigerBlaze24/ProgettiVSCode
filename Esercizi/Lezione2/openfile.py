reader= open ("alice.txt") #1
print(reader)

try:    #2
    reader.readline()
    print("sono nella try")   
    raise Exception("eccezzione")   
  
except Exception:   
    print("sono nella try") 

finally:    
    print(reader)   
    reader.close()  
    print("sono nella finally") 


with open("lettura alice.txt") as reader:   #3
    reader.readline()
#esempi per aprire i file
     