def ourFD(func):
    def retFunc():
        print('******************')
        func()
        print('@@@@@@@@@@@@@@@@@@')
    return(retFunc)

# def sayHi():
#     print('Hello')

# sayHi = ourFD(sayHi)
# sayHi()

@ourFD
def sayHi():
    print('Hello')

sayHi()