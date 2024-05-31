import pickle

class Bank:
    def __init__(self, initial_balance, interest_rate):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        return interest

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        return data

# Создаем 3 экземпляра класса Bank
bank1 = Bank(1000, 5)
bank2 = Bank(2000, 3)
bank3 = Bank(1500, 4)

# Сохраняем информацию о банках в файл
save_data([bank1, bank2, bank3], "banks_data.txt")

# Загружаем информацию обратно из файла
loaded_data = load_data("banks_data.txt")

for bank in loaded_data:
    print(f"Initial Balance: {bank.balance}, Interest Rate: {bank.interest_rate}")
    print(f"Interest Earned: {bank.calculate_interest()}")
    print(f"Withdrawn amount: {bank.withdraw(500)}")


