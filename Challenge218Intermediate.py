import random
from collections import defaultdict

LaBeouf = ["Do it! Just do it!", "Don't let your dreams be dreams.", "Yesterday you said tomorrow. So just do it!",
           "Make your dreams come true. Just do it.", "If you're tired of starting over, stop giving up.",
           "YES YOU CAN! JUST DO IT! ", "Nothing is impossible...", "DO IT! JUST DO IT!", "What are you waiting for?!"]

class To_Do(object):
    def __init__(self):
        self.DO_IT_JUST_DO_IT = defaultdict(list)

    def add_item(self, task, *categories):
        for category in categories:
            self.DO_IT_JUST_DO_IT[category].append(task)

    def view_list(self, *categories):
        for category in categories:
            print "------{0}------".format(category.upper())
            for number, thing in enumerate(self.DO_IT_JUST_DO_IT[category], start = 1):
                print "{0}) {1}\n{2}".format(number, thing, random.choice(LaBeouf))

    def delete_item(self, item):
        for category in self.DO_IT_JUST_DO_IT:
            if item in self.DO_IT_JUST_DO_IT[category]:
                print "\nYOU DID IT! I knew you could {0}!\n".format(item.lower())
                self.DO_IT_JUST_DO_IT[category].remove(item)
            else:
                print "\nYOU DIDN'T HAVE THAT ON YOUR LIST! {0}".format(random.choice(LaBeouf))

    def modify_item(self, item, new_item):
        for category in self.DO_IT_JUST_DO_IT:
            if item in self.DO_IT_JUST_DO_IT[category]:
                self.DO_IT_JUST_DO_IT[category].remove(item)
                self.DO_IT_JUST_DO_IT[category].append(new_item)


