import xmlrpc.client
import datetime;

def Main():
    while(True):
        action = Menu() #1
        if (action == 0):
            break
        else:
            DoSomething(action)
            #break


def Menu():
    
    print()
    print("0: Stop")
    print("1: Add note")
    print("2: Get notes")
    choice = int(input("Your choice: " ))
    return choice

def DoSomething(choice):
    topic = input("Enter topic: " ) #"Hello"
    if (choice == 1):
        note = input("Enter notename: " ) #"Hi"
        text = input("Enter text: " ) #"This is a text"
        ct = datetime.datetime.now()
        ct = ct.strftime("%m/%d/%y - %H:%M:%S")
        with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
            print("%s" % (proxy.makeNote(topic, note, text, ct)))
    elif (choice == 2):
        with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
            print("Notes: \n%s" % (proxy.getTopic(topic)))
            
    elif (choice != 0):
        print("Not a choice")

Main()

'''
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))
    '''