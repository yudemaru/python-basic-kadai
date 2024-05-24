def total_price(price,tax):
    
    total = price + (price*tax)
    
    return total
    
result = total_price(1000, 0.1)
print(f"{result}円")
