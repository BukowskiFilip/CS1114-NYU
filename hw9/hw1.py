def get_chord_dictionary(chords):

        try:
            file = open(chords,"r")

        except FileNotFoundError:
            return {}

        file.readline()
        dict = {}
        for chords in file:
            chords = chords.strip()
            chords = chords.split(",")

            roots = chords[0]
            chord = chords[1]
            notes = tuple(chords[2].split("-"))
            inner_dict = {chord: notes}

            if roots in dict:
                dict[roots].update(inner_dict)
            else:
                dict[roots] = inner_dict

        file.close()

        return dict

def get_possible_chords(list_of_notes, chords):

        root = list_of_notes[0]
        list = []
        root = chords[root]

        for key in root:
            the_tuple = root[key]
            is_valid = True
            for i in list_of_notes:
                if i not in the_tuple:
                    is_valid = False
            if is_valid:
                list.append(list_of_notes[0] + key)

        return tuple(list)

def get_chord_progression(small_list_of_notes,list_of_notes):

    try:
        file = open(small_list_of_notes, "r")

    except FileNotFoundError:
        return {}

    dict_notes = get_chord_dictionary(list_of_notes)
    list = []

    file.readline()

    for chords in file:
        chords = chords.strip()
        chords = chords.split(",")
        x = get_possible_chords(chords, dict_notes)
        list.append(x)

    file.close()

    return list


def write_progression_file(chords):

    file = open("file_hw9_q1", "w")
    for i in chords:
        temp_str = ''
        for y in i:
            temp_str += (y + ',')
        temp_str = temp_str[:len(temp_str)-1]
        print(temp_str, file=file)

    file.close()

def main():
    chord_progression = get_chord_progression("chord_progression.csv", "chords-normalised.csv")
    write_progression_file(chord_progression)

main()
