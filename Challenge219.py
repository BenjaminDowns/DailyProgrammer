import random

LaBeouf = ["Do it! Just do it!", "Don't let your dreams be dreams.", "Yesterday you said tomorrow. So just do it!",
           "Make your dreams come true. Just do it.", "If you're tired of starting over, stop giving up.",
           "YES YOU CAN! JUST DO IT! ", "Nothing is impossible...", "DO IT! JUST DO IT!", "What are you waiting for?!"]

class To_Do(object):
    def __init__(self):
        self.DO_IT_JUST_DO_IT = []

    def request_task(self):
        self.add_or_del = raw_input("Do you want to (1) DO IT or have you (2) DONE IT? (type 1 or 2 and press return) ")
        if self.add_or_del == "1":
            self.add_item()
        elif self.add_or_del == "2":
            self.delete_item()

    def add_item(self):
        self.item = raw_input("What will make your dreams come true? ")
        self.DO_IT_JUST_DO_IT.append(self.item)
        self.view_list()
        self.request_task()

    def view_list(self):
        for number, thing in enumerate(self.DO_IT_JUST_DO_IT, start = 1):
            print "{0}) {1}\n{2}".format(number, thing, random.choice(LaBeouf))

    def delete_item(self):
        self.item = raw_input("WHAT DID YOU DO?! ")
        if self.item in self.DO_IT_JUST_DO_IT:
            self.DO_IT_JUST_DO_IT.remove(self.item)
            print "\nYOU DID IT! I knew you could {0}!\n".format(self.item.lower())
            self.request_task()
        else:
            print "\nYOU DIDN'T HAVE THAT ON YOUR LIST! {0}".format(random.choice(LaBeouf))

todo1 = To_Do()
todo1.request_task()