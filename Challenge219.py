import random

To_Do = []
LaBeouf = ["Do it! Just do it!", "Don\'t let your dreams be dreams.", "Yesterday you said tomorrow. So just do it!",
           "Make your dreams come true. Just do it.", "If you\'re tired of starting over, stop giving up.",
           "YES YOU CAN! JUST DO IT! ", "Nothing is impossible...", "DO IT! JUST DO IT!", "What are you waiting for?!"]

def add_item(item):
    To_Do.append(item)

def viewList():
    for number, thing in enumerate(To_Do, start = 1):
        print "{0}) {1}\n{2}".format(number, thing, random.choice(LaBeouf))

def delete_item(x):
    if x in To_Do:
        To_Do.remove(x)
        print "\nYOU DID IT! I knew you could {0}!\n".format(x.lower())
    else:
        print "\nYOU DIDN'T HAVE THAT ON YOUR LIST! {0}".format(random.choice(LaBeouf))
