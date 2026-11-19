def reserve_inventory(products, order):
    for item in order["items"]:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product is not None:
            product["stock"] -= item["quantity"]


def restock_product(products, product_id, amount):
    if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
        return None

    for product in products:
        if product["id"] == product_id:
            product["stock"] += amount
            return product
    return None