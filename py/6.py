g = int(input())
et =input()

if et ==('テイクアウト'):
    tax = g * 0.08
    total = g + tax
    
else:
    tax = g * 0.1
    total = g + tax
    
tax = int(tax)
total = int(total)
    
print(tax)
print(total)

    
