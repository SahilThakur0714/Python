# WAP to check if a list contains a palimdrome of elements

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("list1 is palimdrome")
else:
    print("list1 is not palimdrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("list2 ispalimdrome")
else:
    print("list2 is not palimdrome")