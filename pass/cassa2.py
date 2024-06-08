class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def add_product(name, price):
    new_product = Product(name, price)
    products.append(new_product)
    def calculate_change(purchase_amount, coins):
    combinations = []
    for coin in coins:
        if coin <= purchase_amount:
            combinations.append((coin, purchase_amount - coin))
    min_coins = min(combinations, key=lambda x: x[0])
    return min_coins[0]
  coin_count = {1: 0, 5: 0, 10: 0, 15: 0, 20: 0}
  purchase_amount = 50
coins = [1, 5, 7, 10, 15]
change = calculate_change(purchase_amount, coins)
print("Сдача:", change)
