from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
cof1 = Coffee("Espresso")
cof2 = Coffee("Latte")

c1.create_order(cof1, 5.5)
c1.create_order(cof2, 4.0)
c2.create_order(cof1, 6.0)
c2.create_order(cof1, 3.5)

print([c.name for c in c1.coffees()])
print([c.name for c in cof1.customers()])
print(cof1.num_orders())
print(cof1.average_price())
print(Customer.most_aficionado(cof1).name)