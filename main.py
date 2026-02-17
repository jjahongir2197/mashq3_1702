class Finance:
    def __init__(self):
        self.income = []
        self.expense = []

    def add_income(self, amount):
        self.income.append(amount)

    def add_expense(self, amount):
        self.expense.append(amount)

    def report(self):
        print("Daromad:", sum(self.income))
        print("Xarajat:", sum(self.expense))
        print("Qoldiq:", sum(self.income) - sum(self.expense))

def run():
    f = Finance()

    while True:
        print("\n1. Daromad\n2. Xarajat\n3. Hisobot\n4. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            f.add_income(int(input("Summa: ")))
        elif c == "2":
            f.add_expense(int(input("Summa: ")))
        elif c == "3":
            f.report()
        else:
            break

run()
