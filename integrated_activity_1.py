"""
HW 08. Mancher’s Algorithm
Arturo Utrilla Hernández A01174331
Ximena Silva Bárcena A01785518
Rodrigo Martínez Vallejo A00573055
November 6th 2025
Analysis and Design of Advanced Algorithms (Gpo 651)
Professor Salvador E. Venegas-Andraca
"""

#TO DOES:
# part 1: look for malicious pattern in transmission
# part 2: look for mirrored code within transmission file, output longest palindrome
# part 3: look for longest common susbtring between both files, output start + end of first file
'''
part 1 
(true | false) if the file transmission1.txt contains the code (sequence of chars) contained in the file mcode1.txt     
(true | false) if the file transmission1.txt contains the code (sequence of chars) contained in the file mcode2.txt 
(true | false) if the file transmission1.txt contains the code (sequence of chars) contained in the file mcode3.txt 
(true | false) if the file transmission2.txt contains the code (sequence of chars) contained in the file mcode1.txt 
(true | false) if the file transmission2.txt contains the code (sequence of chars) contained in the file mcode2.txt 
(true | false) if the file transmission2.txt contains the code (sequence of chars) contained in the file mcode3.txt 
part2 
startPosition endPosition (for transmission1 file) 
startPosition endPosition (for transmission2 file) 
part3 
startPosition endPosition (for longest common substring between stream files) 
'''

def longest_prefix_suffix(pattern):
    len_prefix = len(pattern)
    lps = [0 for _ in range(len_prefix)]
    j = 0
    i = 1
    while i < len_prefix:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_algorithm(transmission, pattern):
    pass