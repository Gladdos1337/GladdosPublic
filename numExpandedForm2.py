def expanded_form(num):
    i = 0
    j = 1
    whole_number = int(num) # Whole number
    text = f"{whole_number}"
    if whole_number == 0: # If first value of num == 0
        text = text[1:]
    num = str(num)[str(num).find("."):]
    num = str(num).replace(".", "")
    ten_list = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000] # Fix this
    z = (len(str(whole_number)) - 1)



    # if whole_number > 9:# Left side, before "."
    #     text = ""
    #     text = f"{(int(whole_number)) // (ten_list[z]) * (ten_list[z])}"
    #     while whole_number > 9:
    #         while whole_number > 9:
    #             if text != "":
    #                 text+= " + "
    #             text += f"{(int(whole_number)) // (ten_list[z]) * (ten_list[z])} "
    #             whole_number = str(whole_number)[1:]
    #             whole_number = int(whole_number)
    #             z += 1
    #         whole_number = whole_number / ten_list[z]

    ### ^^^THIS WHOLE THING IS GARBAGE, BURN IT ^^^####
           

    counter = len(num)
    while i < counter: #Right side, after "."
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

num = 134.34
print(expanded_form(num))


#TODO : #left_side, right_side = str(num).split('.') REFACTOR