# WAF to print the length of a list. ( list is the parameter)
nums = [1, 2, 3, 4, 5]

def list_lenght(a):
    print(len(a))
    return

list_lenght(nums)

# WAF to print the elements of a list in a single line.
#  ( list is the parameter)

def ele_list(list):
    for item in list:
        print(item, end=" ")
    print()

ele_list(nums)

# WAF to find the factorial of n. (n is the parameter)
# print("\n")
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = i*fact
    print(fact)
    # return fact

factorial(5)

# WAF to convert USD to INR.
def convert_currency(usd_val):
    inr_value = usd_val * 85.80
    print(f"${usd_val} = ₨ {inr_value}")
    return

convert_currency(100)