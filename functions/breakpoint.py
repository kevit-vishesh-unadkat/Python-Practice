def calculate_cart_total(cart):

    subtotal=0

    for item in cart:
        subtotal+=item["price"]*item["quantity"]

    discount=subtotal*0.10
    tax=subtotal*0.18

    breakpoint()

    finaltotal=subtotal-discount+tax

    return finaltotal

cart=[
    {
        "name":"Laptop",
        "price":70000,
        "quantity":1
    },
    {
        "name":"TV",
        "price":50000,
        "quantity":5
    }
]

total=calculate_cart_total(cart)

print(total)