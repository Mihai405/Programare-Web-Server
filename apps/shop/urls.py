from .views import CartItemView , OrderView

routes = [
    (r'shop/items',CartItemView),
    (r'shop/orders',OrderView),
]