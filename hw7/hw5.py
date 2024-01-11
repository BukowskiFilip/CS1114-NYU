def get_matryoshka_list(orginal_list):

    if len(orginal_list) == 0:
        return []
    else:
        temp_list = []
        temp_list.append(orginal_list[0])
        repository_list = []

        for i in range(1, len(orginal_list)):
            if orginal_list[i-1] < orginal_list[i]:
                temp_list.append(orginal_list[i])
            else:
                repository_list.append(temp_list)
                temp_list = [orginal_list[i]]

        repository_list.append(temp_list)
        return(repository_list)


def main():
 original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
 matryoshka_list = get_matryoshka_list(original_list)
 print(matryoshka_list)

main()
