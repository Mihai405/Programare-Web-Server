from .views import CartItemView , OrderView , AdminOrderView

routes = [
    (r'shop/items',CartItemView),
    (r'shop/orders',OrderView),
    (r'shop/admin/orders',AdminOrderView),
]