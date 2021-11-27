
import cryptocode
import random as rand


def try_me():
    print("Welcome in decoding program")
    batch_708 = ['Lisa', 'Brigita', 'Regina', 'Mike', 'Claire', 'Ben1', 'Ben2']
    name = rand.choice(batch_708)
    encoded_name = cryptocode.encrypt(name, "cryptocode is amazing")
    return f" This is your classmate encoded name: {encoded_name}"
    
    
