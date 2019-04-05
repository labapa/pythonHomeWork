price = input('가격 입력: ')
discount = input('할인율 입력: ')

price = int(price)
discount = int(discount)
print(price - (price * (discount/100)))
