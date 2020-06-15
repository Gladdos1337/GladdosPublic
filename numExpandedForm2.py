#Refactor meh <3
def expanded_form(num):
    i = 0
    j = 1
    h = 0
    whole_number = int(num) # Whole number
    text = ""
    if whole_number == 0: # If first value of num == 0
        text = text[1:]
    num = str(num)[str(num).find("."):]
    num = str(num).replace(".", "")
    ten_list = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000] # Fix this
    z = (len(str(whole_number)) - 1)
    if whole_number > 9:# Left side, before "."
        whole_number = (str(whole_number))
        if text != "":
            text+= " + "
            text += whole_number[0] + (len(whole_number)-1) * "0"
            whole_number = (whole_number[1:])
    elif whole_number != 0:
        text = f"{whole_number}"
    counter = len(num) #Right side, after "."
    while i < counter: 
        if num[i] == "0":
            i+=1
            j+=1
            continue
        if text != "":
            text+= " + "
        text += f"{str(num[i])}/{ten_list[j]}"
        i += 1
        j += 1
    return text

num = 100.34
print(expanded_form(num))
#TODO : #left_side, right_side = str(num).split('.') REFACTOR