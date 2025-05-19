hour = int(input('時：'))
min = int(input('分：'))

if hour < 12:
    print(f'現在{hour}：{min} a.m.')

else :
    print(f'現在{hour -12}：{min} p.m.')