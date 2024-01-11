def update_frequencies(old_frequencies, new_sequence):
 old_a = old_frequencies[0][1]
 old_c = old_frequencies[1][1]
 old_t = old_frequencies[2][1]
 old_g = old_frequencies[3][1]

 a_counter = 0
 c_counter = 0
 g_counter = 0
 t_counter = 0

 for i in range(len(new_sequence)):
  if new_sequence[i] == "A":
     old_a += 1
     a_counter += 1
  elif new_sequence[i] == "C":
    old_c += 1
    c_counter += 1
  elif new_sequence[i] == "T":
    old_t += 1
    t_counter += 1
  elif new_sequence[i] == "G":
   old_g += 1
   g_counter += 1

 new_frequenices = (f"Number of nucleotides added: A -> {a_counter} | C -> {c_counter} | T -> {t_counter} | G -> {g_counter} \n[('A', {old_a}), ('C', {old_c}), ('T', {old_t}), ('G', {old_g})]")
 return new_frequenices

def main():
 old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
 new_sequence = "ACCCGTTA"
 new_frequencies = update_frequencies(old_frequencies, new_sequence)
 print(new_frequencies)

main()
