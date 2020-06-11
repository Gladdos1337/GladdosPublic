
def persistence(n):
    total = 1

    while n > 9:
        new_list = [int(i) for i in str(n)]
        for ele in range(0, len(new_list)):
            total*=new_list[ele]
        n = total
        counter+=1
    return counter

n = 39
print(persistence(n))