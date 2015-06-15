import random

LaBeouf = ["Do it! Just do it!", "Don't let your dreams be dreams.", "Yesterday you said tomorrow. So just do it!",
           "Make your dreams come true. Just do it.", "If you're tired of starting over, stop giving up.",
           "YES YOU CAN! JUST DO IT! ", "Nothing is impossible...", "DO IT! JUST DO IT!", "What are you waiting for?!"]

class To_Do(object):
    def __init__(self):
        self.DO_IT_JUST_DO_IT = []

    def add_item(self, item):
        self.DO_IT_JUST_DO_IT.append(item)

    def view_list(self):
        for number, thing in enumerate(self.DO_IT_JUST_DO_IT, start = 1):
            print "{0}) {1}\n{2}".format(number, thing, random.choice(LaBeouf))

    def delete_item(self, item):
        if item in self.DO_IT_JUST_DO_IT:
            self.DO_IT_JUST_DO_IT.remove(item)
            print "\nYOU DID IT! I knew you could {0}!\n".format(item.lower())
        else:
            print "\nYOU DIDN'T HAVE THAT ON YOUR LIST! {0}".format(random.choice(LaBeouf))


todo1 = To_Do()
todo1.add_item("Take a shower.")
todo1.add_item("Go to work.")
todo1.view_list()
todo1.delete_item("Take a shower.")
todo1.view_list()