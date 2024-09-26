total_price = 0
DISCOUNT = 0.1

number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price - total_price * DISCOUNT
print(f"Total price for {number_of_items} items is: ${total_price:.2f}")