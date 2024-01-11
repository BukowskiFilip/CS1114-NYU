def is_haiku(is_haiku):

    comma_counter_1 = 0
    comma_counter_2 = 0
    comma_counter_3 = 0
    haiku = True

    split_haiku = is_haiku.split('/')

    for i in range(len(split_haiku[0])):
        if split_haiku[0][i] == ",":
            comma_counter_1 += 1
    for x in range(len(split_haiku[1])):
        if split_haiku[1][x] == ",":
            comma_counter_2 += 1
    for y in range(len(split_haiku[2])):
        if split_haiku[2][y] == ",":
            comma_counter_3 += 1

    if comma_counter_1 == 4 and comma_counter_2 == 6 and comma_counter_3 == 4:
        return haiku

    elif comma_counter_1 != 4:

        print(f"WARNING: The first line is not 5 syllables long.")
        return haiku == False

    elif comma_counter_2 != 6:

        print(f"WARNING: The second line is not 7 syllables long.")
        return haiku == False

    else:
        print(f"WARNING: The third line is not 5 syllables long.")
        return haiku == False

def haiku_string_praiser(haiku_string):
    if(is_haiku(haiku_string)) == True:
        answer = []
        list_of_lines = haiku_string.split('/')
        for i in range(len(list_of_lines)):
            list_of_lines_split = list_of_lines[i].split(',')
            list_of_lines_joined = "".join(list_of_lines_split)

            answer.append(list_of_lines_joined)
        return "\n".join(answer)
    return ""

def main():
    #check for 2nd problem
    #print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing, at, the, moon")) # prints â€˜Trueâ€™
    #print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing")) # prints â€˜Falseâ€™

    #check for 3rd problem
    #haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing, at, the, moon"
    #formatted_haiku = haiku_string_praiser(haiku_string)
    #print(formatted_haiku)
main()

