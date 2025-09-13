def calculate_total_purchase():
# A customer in a store is purchasing five items.
# Write a program that asks for each item,
    item_price1 = float(input('What is the price of your first purchase?'))
    item_price2 = float(input('What is the price of your second purchase?'))
    item_price3 = float(input('What is the price of your third purchase?'))
    item_price4 = float(input('What is the price of your fourth purchase?'))
    item_price5 = float(input('What is the price of your fifth purchase?'))
# then displays the subtotal of the sale,
    subtotal = item_price1 + item_price2 + item_price3 + item_price4 + item_price5
    print(f'The subtotal is {subtotal}')
# the amount of sales tax, and the total.
    sales_tax = subtotal * .07
    print(f'The sales tax is {sales_tax}')
# Assume the sales tax is 7 percent.
    total = subtotal - sales_tax
    print(f'The total price is {total}')

calculate_total_purchase()