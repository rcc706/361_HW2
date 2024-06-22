from threading import Thread
from time import perf_counter

'''''
    # Goes inside of addVect and SubVect
    # Splitting the vector string from the client into separate elements
    arr = sentence.split()
    
    # Adding the default Vector elements to the clients' vector elemnets
    for i in range(3):
        sum[i] = server_default_Vector[i] + int(arr[i])
    
    # Creating the new string vector and sending it to the client
    newVector = str(sum[0]) + " " + str(sum[1]) + " " + str(sum[2])
'''''

def addVect(vector1, vector2):
    vect1Arr = [0, 0, 0]
    vect2Arr = [0, 0, 0]
    totalArr = [0, 0, 0]
    sumVector = ""; 
    
    vect1Arr = vector1.split()
    vect2Arr = vector2.split()
    
    for i in range (3):
        totalArr[i] = int(vect1Arr[i]) + int(vect2Arr[i])
        sumVector += str(totalArr[i]) + " "
    
    print("Sum Vector: " + sumVector)
    
def subVect(vector1, vector2):
    vect1Arr = [0, 0, 0]
    vect2Arr = [0, 0, 0]
    totalArr = [0, 0, 0]
    diffVector = ""; 
    
    vect1Arr = vector1.split()
    vect2Arr = vector2.split()
    
    for i in range (3):
        totalArr[i] = int(vect1Arr[i]) - int(vect2Arr[i])
        diffVector += str(totalArr[i]) + " "
        
    print("Difference Vector: " + diffVector) 
    
def main():
    # asking for user input for the vector
    uiVector1 = input('Input 3 integers (i.e x y z) then press ENTER: ')
    uiVector2 = input('Input 3 integers (i.e x y z) then press ENTER: ')
    
    # create two new threads
    t1 = Thread(target=addVect(uiVector1, uiVector2))
    t2 = Thread(target=subVect(uiVector1, uiVector2))
    
    # start the threads
    t1.start()
    t2.start()
    
    # wait for the threads to complete
    t1.join()
    t2.join()

if __name__ == "__main__":
    start_time = perf_counter()
    
    main()
    
    end_time = perf_counter()
    print(f'It took {end_time - start_time :0.2f} second(s) to complete.')