# Smith-Waterman algorithm for local alignment

# Input : 
* seq1, seq2 : 2 strings containing the sequences to align

* subst_matrix : the substitution matrix bewteen alphabet characters, fromatted as a list of list

* gap : the gap is linear and defined as gap = gapA + gap_number * gapB, where gapA, and gapB are 2 numbers given as arguments and gap_number is the length of the gap continuous gap. The user needs to input only gapA and gapB.

* alphabet : a list containing all the characters used in this alphabet

# Output : 
a tuple containing :
  - the first aligned sequence, with gaps inserted if any
  - the second aligned sequence, with gaps inserted if any
  - the score of the alignment

# /!\ 
This implementation only returns one best alignment, if several exist !
