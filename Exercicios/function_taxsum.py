def tax_in_item_sum(tax, value):
    return value + (value * tax / 100)


print(tax_in_item_sum(20, 100))