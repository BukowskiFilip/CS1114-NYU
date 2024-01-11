
user_dna = input("Enter a DNA sequence: ")
user_second_dna = input("Enter a second DNA sequence: ")


if len(user_dna) >= len (user_second_dna):
    larger_string = len(user_dna)
else:
    larger_string = len(user_second_dna)


answer = ""
real_answer = ""
invalid_characters = 0

for i in range(larger_string):
    if i < len(user_dna):
        if user_dna[i] == 'A' or user_dna[i] == 'C' or user_dna[i] == 'T' or user_dna[i] == 'G':
            answer += user_dna[i]
        else:
            invalid_characters += 1
            
    if i < len(user_second_dna):
        if user_second_dna[i] == 'A' or user_second_dna[i] == 'C' or user_second_dna[i] == 'T' or user_second_dna[i] == 'G':
            answer += user_second_dna[i]
        else:
            invalid_characters += 1
            
for v in range(len(answer)):
    if answer[v] == 'A':
        real_answer += 'T'
    if answer[v] == 'C':
        real_answer += 'G'
    if answer[v] == 'T':
        real_answer += 'A'
    if answer[v] == 'G':
        real_answer += 'C'

print("Fused sequence: " + str(real_answer) + " | " + "Invalid characters: " + str(invalid_characters))
