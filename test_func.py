def get_vat(price, vat_rate):
    vat = price / 100* vat_rate
    price_no_vat = price - vat
    return price_no_vat
price1 = 200
vat_rate1 = 18
print(get_vat(price1, vat_rate1))
