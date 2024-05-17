import re

with open('price.txt', 'r') as file:
    data = file.read()
prices = re.findall(r'\d+\s*(?:руб(?:лей)?\.?)?\s*\d+\s*(?:коп(?:еек)?\.?)?', data)

for price in prices:
    print(price)
    
count = len(prices)
print(f"Всего найдено {count} цен.")
