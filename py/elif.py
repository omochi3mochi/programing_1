year = int(input('西暦:'))

''' 後ろが短くて忘れられやすい
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('うるう年')
        else:
            print('平年')
    else:
        print('うるう年')
else:
    print('平年')
'''
'''　後ろが長い
if year % 4 != 0:
    print('平年')
else:
    if year % 400 == 0:
        print('うるう年')
    else:
        if  year % 100 == 0:
            print('平年')
        else:
            print('うるう年')
'''
''' elifを使う
if year % 4 != 0:
    print('平年')
elif year % 400 == 0:
    print('うるう年')
elif year % 100 == 0:
    print('平年')
else:
'''
###比較演算子
if year % 400 == 0 or \
   year % 4 == 0 and year % 100 != 0:
    print('うるう年')
else:
    print('平年')