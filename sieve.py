#Sieve of eratosthenes v1.0
def sieve(the_list):
    counting_list = list(range(1, 5000))
    new_list = []
    for num in the_list:

        if num % 2 != 0:
            new_list.append(num)  # Appends the even numbers to new list

    new_list.insert(0, 2)  # Adds two to begging of the list
    i = 1
    j = 0
    while i < len(new_list):
        while j < len(new_list):
            rez = new_list[i] * counting_list[j]  # rez = 3*1
            if j == 0:
                j += 1
                continue
            if rez in new_list:
                index = new_list.index(rez)
                new_list.pop(index)
                j += 1
            # if rez > new_list[-1]
            else:
                j += 1
                continue  # ADD : if j > last item in new_list list STOP
        i += 1
        j = 0
    return new_list

the_list = list(range(2, 10000))  # 10_000_001 for future ref
print(sieve(the_list))

#TODO: Refactor the code
#TODO: Make it run faster, it takes ages to get primes from 10,000 numbers.

# list comprehension