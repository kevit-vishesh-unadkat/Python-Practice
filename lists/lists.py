# smart cart application
# with the use of functions , switch statment , conditional Statement ,
# and main purpose behinde this activity is to use python list concept
# with the real world case


# create a data

cart=[
    {
        "id":101,
        "name":"Laptop",
        "price":75000,
        "quantity":1
    },
    {
        "id":102,
        "name":"TV",
        "price":50000,
        "quantity":5
    },
    {
        "id":103,
        "name":"Phone",
        "price":25000,
        "quantity":20
    }
]
def display_product(product, index=None):
    """
    Display one product.
    """

    if index is not None:
        print(
            f"{index}. "
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"Qty: {product['quantity']}"
        )
    else:
        print(
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"Qty: {product['quantity']}"
        )

# 1 . View the Cart items

def view_cart_item():
    """
    this function is use to show all the 
    item witch present inside the cart.
    and in this function i saw the concept like
    len 
    if condition
    for loop
    enumerate
    """

    if not cart:
        print("There is no any item in your cart")
        return 
    else:
        print(f"total products:{len(cart)}")
        print()

    # for index,product in enumerate(cart,start=1):
    #     display_product(product,index)

view_cart_item()


# 2. add to product into a cart

def add_cart_item():
    """
    this function is use to add items into 
    the cart 
    so for this function i used a append method of lists
    """

    product={
        "id":104,
        "name":"Tablet",
        "price":20000,
        "quantity":50
    }

    cart.append(product)

    print(f"added product to the cart :  {product['name']}")
    print(f"added product item quantity : {product['quantity']}")
    print(f"added product item price : {product['price']}")


add_cart_item()  


# 3. add more than one item to the cart list

def add_more_cart_item():
    """
    this function is used for to add more 
    then one item to the cart 
    so for implement this cincept 
    i used extend method in list
    """

    products =[
        {
            "id":105,
            "name":"webcam",
            "price":3000,
            "quantity":30
        },
        {
            "id":106,
            "name":"USB hub",
            "price":2000,
            "quantity":10
        }
    ]

    cart.extend(products)

    print(f"added multiple product : {products}")

add_more_cart_item()    



# 4 . undo last item to the cart

def remove_last_item():
    """
    this function is used for remove the last item 
    to the cart 
    so for this i used pop() method of python list
    """

    if not cart:
        print("there is no item present in cart")

    else:

        removed_item=cart.pop()

        print(f"remove last product item to the cart is : {removed_item['name']}")    

remove_last_item()     

# 5. remove product from the task.
def remove_product():
    """
    this function is to remove a product from the cart
    to implement this functinality use remove mathod of 
    lists class
    """

    if not cart:
        print("There is no any item in cart")

    product_name=input("enter product name you want to remove : ").strip()

    found_product=None

    for product in cart:
        if product["name"].lower()==product_name.lower():
            found_product=product
            break

    if found_product is not None:
        cart.remove(found_product)
        print(
            f"{found_product['name']} "
            f"removed from cart."
        )
    else:
        print("product not found")

remove_product()

# 6. view recent products

def view_recent_product():
    """
    this function is to show only recent top 
    three product from the cart
    """
    if not cart:
        print("cart is empty")

    recent_product=cart[-3:]

    print("last three product")

    for index , product in enumerate(
        recent_product,
        start=1
    ):
        display_product(product,index)

view_recent_product()


# search product

def search_product():
    """
    this function is used to search a product
    and it will provide  funcinality to user to search a product 
    in cart
    """

    if not cart:
        print("cart is empty")

    product_name=input(
        "enter a product name to search  :"
    ).strip()

    product_exist=any(
        product["name"].lower()==product_name.lower()
        for product in cart
    )

    if product_exist:
        print("product exist in your cart")
    else:
        print("product not exist in your cart")

search_product()


# count product


# reverse list

def reverse_list():
    """
    this function is used to reverse a list
    for this use reverse method of the list
    """

    if not cart:
        print("your cart is empty")
    cart.reverse()

    print("cart order reversed")


reverse_list()


# Copy Cart
def copy_cart():
    """
    this functinon is used to copy a cart 
    for this use copy method
    """

    if not cart:
        print("your cart is empty")

    backup_cart=cart.copy()

    print("print copied successfully")

    print("\nOriginal Cart:")

    for product in cart:
        display_product(product)

    print("\nCopyCart")

    for product in backup_cart:
        display_product(product)

copy_cart()


#validate cart

def validate_cart():
    """
    validate the cart 
    using (all) inbuilt function concept
    """

    if not cart:
        print("your cart is empty")

    valid=all(
        product['quantity']>0
        for product in cart
    )

    if valid:
        print("cart is valid")

    else:
        print("cart contain invalid quantities")

validate_cart()


# calculate a cart total

def calculate_total():
    """
    this function is used to calculate total 
    price of cart
    """

    if not cart:
        print("your cart is empty")

    total_price=sum(
        product['price']*product['quantity']
        for product in cart
    )

    print(f"Cart Total :{total_price}")

calculate_total()