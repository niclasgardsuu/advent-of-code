with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')


class Monkey:
    def __init__(self, string) -> None:
        string = string.split('\n')[1:]

        self.items = []
        for item in map(lambda x: int(x.strip().replace(',','')),string[0].strip().split()[2:]):
            self.items = [item] + self.items

        operations = string[1].split()[-2:]
        self.operation = operations[0]
        self.increment = operations[1]

        self.test = int(string[2].split()[-1])

        self.true_throw = int(string[3].split()[-1])
        self.false_throw = int(string[4].split()[-1])

        self.business = 0

    def get_test(self):
        return self.test

    def get_business(self):
        return self.business

    def print(self):
        for item in self.items:
            print(item)
        print(self.operation, self.increment)
        print("divisible: ", self.test)
        print("to: ", self.true_throw, " else-to: ", self.false_throw)
        print()

    def add_item(self, item):
        self.items = [item] + self.items

    def throw(self,monkeys):
        item = self.items.pop()
        if item % self.test == 0:
            monkeys[self.true_throw].add_item(item)
        else:
            monkeys[self.false_throw].add_item(item)

    def update_wl(self, div = False):
        if len(self.items) > 0:
            if self.increment.isnumeric():
                inc = int(self.increment)
            else:
                inc = self.items[-1]

            if self.operation == '+':
                self.items[-1] = self.items[-1] + inc
            elif self.operation == '*':
                self.items[-1] = self.items[-1] * inc
            if div:
                self.items[-1] = int(self.items[-1] / 3)
            self.business += 1
            return True
        return False

    def reset_wl(self,scd):
        for i in range(len(self.items)):
            self.items[i] = self.items[i] % scd


def p(monkeys):
    for m in monkeys:
        m.print()


monkeys = []
business = []
lcm = 1
for row in rows:
    monkeys.append(Monkey(row))
    business.append(0)
    lcm *= monkeys[-1].get_test()
for i in range(20):
    for m in monkeys:
        while m.update_wl(div = True):
            m.throw(monkeys)
    for m in monkeys:
        m.reset_wl(lcm)
bs = list(map(lambda m: m.get_business(), monkeys))
bs.sort(reverse = True)
print(bs[:2])

monkeys = []
business = []
lcm = 1
for row in rows:
    monkeys.append(Monkey(row))
    business.append(0)
    lcm *= monkeys[-1].get_test()
for i in range(10000):
    for m in monkeys:
        while m.update_wl():
            m.throw(monkeys)
    for m in monkeys:
        m.reset_wl(lcm)
bs = list(map(lambda m: m.get_business(), monkeys))
bs.sort(reverse = True)
print(bs[:2])