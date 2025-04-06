#POS PROGRAM
print('------------------------')
print('Best Buy Retail Store')
print('------------------------')
product_cat = {
    'Flour':{'price':75, 'stock':15},
    'Rice':{'price':120, 'stock':20},
    'Chicken':{'price':350, 'stock':10},
    'Sugar':{'price':200, 'stock':20},
    'Egg':{'price':60, 'stock':12},
    'Pork':{'price':450, 'stock':10},
    'Bread':{'price':650, 'stock':6},
    'Salt':{'price':1000, 'stock':12},
    'Cornflakes':{'price':1200, 'stock':12},
    'Milk':{'price':500, 'stock':10},
    'Soap':{'price':200, 'stock':15},
    
}

#display catalog
def display_cat():
    print('------------------------')
    print('Best Buy Retail Store')
    print('------------------------')
    print('Product Catalog:')
    print(f"{'Product Name':<10} {'Price':<10} {'Stock'}" )
    for product, detail in product_cat.items():
        print(f"{product:<10} ${detail['price']:<9} {detail['stock']}")

#check stock availability
def stock_check(product, amount):
    if product_cat[product]['stock'] >= amount:
        return True
    else:
        print(f"Sorry, we do not sufficient stock for {product}. our available stock is: {product_cat[product]['stock']}")
        return False

# update stock after cart add/drop
def stock_update(product, amount, add_drop):
    if add_drop == 'add':
        product_cat[product]['stock'] -= amount
    elif add_drop == 'drop':
        product_cat[product]['stock'] += amount

# shopping cart processes
def add_cart(cart, product, amount):
    
    if product in product_cat and stock_check(product, amount):
        cart.append({'product':product, 'amount': amount, 'price': product_cat[product]['price']})
        stock_update(product, amount, 'add')
        print (f"{amount} {product} (s) added to your cart")
    else:
            print(f'Unable to add to cart.')


# drop item from cart
def drop_cart(cart, product, amount):
    for item in cart:
        if item['product'] == product and item['amount'] >= amount:
            cart.remove(item)
            stock_update(product, amount, 'drop')
            print(f'{amount} {product}(s) was removed from your cart.')
            return
    print(f'Unable to remove {product} from your cart. Please check cart.')

#view items in cart
def view_cart(cart):
    if not cart:
        print('your cart is empty.')
        return
    print(f"{'product name':<10} {'amount':<10} {'unit price':<10} {'total price'}")
    subtotal = 0
    for item in cart:
        total_price = item['amount'] * item['price']
        print(f"{item['product']:<10} {item['amount']:<10} ${item['price']:<9}")
        subtotal += total_price
    return subtotal


# calculate total with tax and discounts
def full_total(subtotal):
    tax = subtotal * 0.15
    sum_total = subtotal + tax
    
    #10% discount on orders over $5000
    if subtotal > 5000:
        discount = sum_total * 0.1
        sum_total -= discount
        print(f"Discount granted: ${discount:.2f}")
    return sum_total, tax

#payment processing
def pay_process(sum_total):
    while True:
        try:
            pay_got = float(input(f"Your Sum Total is: ${sum_total:.2f}\nEnter pay received: $"))
            if pay_got >= sum_total:
                change = pay_got - sum_total
                print(f"Customer change: ${change:.2f}")
                return pay_got, change
            else:
                print('Insufficeint fund, please enter a valid amount:')
        except ValueError:
            print('Invaild input, please enter a valid amount:')

#receipt generator
def receipt(cart, subtotal, tax, sum_total, pay_got, change):
    store_name = 'Best Buy Retail Store'
    print('\n' + '-'*30)
    print(f"{store_name.center(30)}")
    print('Receipt'.center(30))
    print('Thanks for shopping at Best Buy Retail Store'.center(30))
    print('-' * 30)

        


#Main POS function
def main():
    cart = []
    while True:
        print('\nPlease select an option:')
        print('1. Display Product Catalog')
        print('2. Add to cart')
        print('3. Remove from cart')
        print('4. View cart')
        print('5. Checkout')
        print('6. Exit')
        choice = input('Enter your selection: ')


#display catalog selection     
        if choice == '1':
            display_cat()

#add to cart selection    
        elif choice == '2':
            product = input('Enter product name: ').capitalize()
            amount = int(input('Enter amount: '))
            add_cart(cart, product, amount)
            
#remove from cart selection
        elif choice == '3':
            product = input('Enter product name: ').capitalize()
            amount = int(input('Enter amount: '))
            drop_cart(cart, product, amount)
            

#view cart selection
        elif choice == '4':
            subtotal = view_cart(cart)
            if subtotal is not None:
                print(f"Subtotal: ${subtotal:.2f}")
                

#checkout selection
        elif choice == '5':
            subtotal = view_cart(cart)
            if subtotal is not None:
                sum_total, tax = full_total(subtotal)
                pay_got, change = pay_process(sum_total)
                receipt(cart, subtotal, tax, sum_total, pay_got, change)
                cart.clear()
            

#Exit POS
        elif choice == '6':
            print('POS shutting down')
            break
        else:
            print('Invailed input, please try again.')
            


if __name__ == '__main__':
    main()











