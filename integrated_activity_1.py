"""
HW 08. Mancher’s Algorithm
Arturo Utrilla Hernández A01174331
Ximena Silva Bárcena A01785518
Rodrigo Martínez Vallejo A00573055
November 6th 2025
Analysis and Design of Advanced Algorithms (Gpo 651)
Professor Salvador E. Venegas-Andraca
"""

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

#FILES
transmission_files = ["transmission1.txt","transmission2.txt"]
malicious_codes = ["mcode1.txt","mcode2.txt","mcode3.txt"]

#PART 1: FINDING MALICIOUS CODE PATTERN

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

def kmp_algorithm(main_string, pattern):
    i = 0
    j = 0
    m = len(pattern)
    n = len(main_string)
    prefix_array = longest_prefix_suffix(pattern)
    loc_array = []
    while i < n:
        i += 1
        j += 1
        if j == m:
            loc_array.append(i-j)
            j = prefix_array[j-1]
        elif i < n and pattern[j] != main_string[i]:
            if j != 0:
                j = prefix_array[j-1]
    return loc_array
'''
print("PART 1")
for transmission in transmission_files:
    with open(transmission, "r") as transmission_file:
        content = transmission_file.readline().strip()
        for malicious_code in malicious_codes:
            with open(malicious_code, "r") as malicious_file:
                result = kmp_algorithm(content, malicious_file.readline().strip())
                print(f"File {transmission}: {result != []} {result} for malicious code in file {malicious_code}")
'''

#PART 2: LONGEST PALINDROME IN TRANSMISSIONS

def manachers_algorithm():
    pass

#PART 3: LONGEST COMMON SUBSTRING BETWEEN BOTH TRANSMISSIONS

class State:
    def __init__(self):
        self.len = 0
        self.link = -1
        self.next = {}


class SuffixAutomaton:
    def __init__(self, maxlen=100000):
        self.st = [State() for _ in range(maxlen * 2)]
        self.sz = 1
    
    def sa_extend(self, c):
        cur = self.sz
        self.sz += 1
        self.st[cur].len = self.st[self.last].len + 1
        
        p = self.last
        while p != -1 and c not in self.st[p].next:
            self.st[p].next[c] = cur
            p = self.st[p].link
        
        if p == -1:
            self.st[cur].link = 0
        else:
            q = self.st[p].next[c]
            if self.st[p].len + 1 == self.st[q].len:
                self.st[cur].link = q
            else:
                clone = self.sz
                self.sz += 1
                self.st[clone].len = self.st[p].len + 1
                self.st[clone].next = self.st[q].next.copy()
                self.st[clone].link = self.st[q].link
                
                while p != -1 and self.st[p].next.get(c) == q:
                    self.st[p].next[c] = clone
                    p = self.st[p].link
                
                self.st[q].link = clone
                self.st[cur].link = clone
        
        self.last = cur

    def build(self, s):
        for ch in s:
            self.sa_extend(ch)

def longest_common_substring():
    pass


'''
trail = Suffix_Automaton()
print(trail.st)
'''