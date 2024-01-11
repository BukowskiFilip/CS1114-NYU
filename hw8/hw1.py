from pprint import pprint


def get_nucleotide_frequencies(nucleotides):
    dict1 = {}
    Junk = {}
    VALID_SEQUENCE = ['A', 'C', 'G', 'T']
    sequence_capitalize = nucleotides.upper()
    junk_counter = 0

    for i in sequence_capitalize:
        if i in VALID_SEQUENCE:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1
        else:
            if i in dict1:
                Junk[i] = Junk[i] + 1
                junk_counter += 1
            else:
                Junk[i] = 1
                junk_counter += 1

    dict1['Junk'] = Junk

    return dict1, junk_counter


def main():
    frequencies, junk_count = get_nucleotide_frequencies(nucleotides="ACTGTCaCGRFRTNfsHYCgggTCGACCSGTGTCACGT")
    pprint(frequencies)
    print(f"Number of junk nucleotides: {junk_count}.")


main()
