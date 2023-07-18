import copy
monkeys = []

class Item:
    def __init__(self, worry):
        self.worries = []
        self.tests = [17, 19, 7, 11, 13, 3, 5, 2]
        for test in self.tests:
            self.worries.append(worry % test)

    def add_worry(self, worry):
        for i, test in enumerate(self.tests):
            self.worries[i] = (self.worries[i] + worry) % test


    def mult_worry(self, worry):
        for i, test in enumerate(self.tests):
            self.worries[i] = (self.worries[i] * worry) % test


    def square_worry(self):
        for i, test in enumerate(self.tests):
            self.worries[i] = (self.worries[i] ** 2) % test

    def get_test(self, number):
        if number == 'seventeen':
            return self.worries[0]
        elif number == 'nineteen':
            return self.worries[1]
        elif number == 'seven':
            return self.worries[2]
        elif number == 'eleven':
            return self.worries[3]
        elif number == 'thirteen':
            return self.worries[4]
        elif number == 'three':
            return self.worries[5]
        elif number == 'five':
            return self.worries[6]
        elif number == 'two':
            return self.worries[7]

class Monkey:
    inspected = 0
    
    def __init__(self, items, operation, number, test, true, false):
        self.items = items
        self.operation = operation
        self.number = number
        self.test = test
        self.true = true
        self.false = false

    def inspect(self):
        if len(self.items) > 0:
            item = self.items.pop(0)
            if self.operation == '+':
                item.add_worry(self.number)
            elif self.operation == '*':
                item.mult_worry(self.number)
            elif self.operation == '**':
                item.square_worry()
            #worry //= 3
            self.inspected += 1
            return item
        else:
            return None

    def take_turn(self):
        for i in range(len(self.items)):
            item = self.inspect()
            if item.get_test(self.test) == 0:
                self.throw(item, monkeys[self.true])
            else:
                self.throw(item, monkeys[self.false])
    
    def throw(self, item, monkey):
        monkey.catch(item)

    def catch(self, item):
        self.items.append(item)



monkeys.append(Monkey([Item(83), Item(97), Item(95), Item(67)], '*', 19, 'seventeen', 2, 7))

monkeys.append(Monkey([Item(71), Item(70), Item(79), Item(88), Item(56), Item(70)], '+', 2, 'nineteen', 7, 0))

monkeys.append(Monkey([Item(98), Item(51), Item(51), Item(63), Item(80), Item(85), Item(84), Item(95)], '+', 7, 'seven', 4, 3))

monkeys.append(Monkey([Item(77), Item(90), Item(82), Item(80), Item(79)], '+', 1, 'eleven', 6, 4))

monkeys.append(Monkey([Item(68)], '*', 5, 'thirteen', 6, 5))

monkeys.append(Monkey([Item(60), Item(94)], '+', 5, 'three', 1, 0))

monkeys.append(Monkey([Item(81), Item(51), Item(85)], '**', 0, 'five', 5, 1))

monkeys.append(Monkey([Item(98), Item(81), Item(63), Item(65), Item(84), Item(71), Item(84)], '+', 3, 'two', 2, 3))


##monkeys.append(Monkey([79, 98], operationTimes, 19, 23, 2, 3))
##
##monkeys.append(Monkey([54, 65, 75, 74], operationPlus, 6, 19, 2, 0))
##
##monkeys.append(Monkey([79, 60, 97], operationSquared, 1, 13, 1, 3))
##
##monkeys.append(Monkey([74], operationPlus, 3, 17, 0, 1))


def take_round():
    for i in range(len(monkeys)):
        #print('Monke', i)
        monkeys[i].take_turn()


for i in range(10_000):
    take_round()

inspected = []
for monkey in monkeys:
    inspected.append(monkey.inspected)

a = inspected.pop(inspected.index(max(inspected)))
b = max(inspected)

print(a,b, a*b)

