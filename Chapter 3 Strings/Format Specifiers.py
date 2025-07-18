# Format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# .< = left justify
# .> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator 

price1 = 3.14159
price2 = -987.65
price3 = 12532.34
price4 = 12732.34
price5 = 12454.34
price6 = 12876.34
price7 = 12345.34
price8 = 12345.34
price9 = 1-2543.34
price10 = 12456.34


print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:03}")
print(f"Price 4 is ${price4:.<10}")
print(f"Price 5 is ${price5:>10}")
print(f"Price 6 is ${price6:^}")
print(f"Price 7 is ${price7:+}")
print(f"Price 8 is ${price8:=}")
print(f"Price 9 is ${price9:}")
print(f"Price 10 is ${price10:,}")