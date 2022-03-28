import enum

#Question3-2B enum class
class Module(enum.Enum):
    CSC1006 = 1
    CSC1007 = 2
    CSC1008 = 3
    CSC1009 = 4

#Question3-2B
def Question3Function2B(module):
    if (module == Module.CSC1006):
        print("Mathematics 2")
    elif (module == Module.CSC1007):
        print("Operating Systems")
    elif (module == Module.CSC1008):
        print("Data Structures and Algorithms")
    elif (module == Module.CSC1009):
        print("Object Oriented Programming")

    print("After switch")

#Question3-2C
def Question3Function2C():
    for i in range(102,66,-1):
        resultOfMod = int(i) % 2
        if(resultOfMod != 0):
            print("Value of x : " + str(i))


Question3Function2B(Module.CSC1009)
Question3Function2C()