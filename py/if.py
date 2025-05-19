price = int(input('単価；'))
count = int(input('個数：'))

goukei = price * count

if count >= 2:
    goukei *= 0.9
    goukei = int(goukei)
    
print(f'合計金額は{goukei}円')