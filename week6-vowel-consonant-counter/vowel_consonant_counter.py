vowel_a = []
vowel_e = []
vowel_i = []
vowel_o = []
vowel_u = []
spaces = []
consonants = []

sentence = input("Enter your sentence: ")

for characters in sentence:
    ch = characters.lower()
    if ch == 'a':
        vowel_a.append('a')
    elif ch == 'e':
        vowel_e.append('e')
    elif ch == 'i':
        vowel_i.append('i')
    elif ch == 'o':
        vowel_o.append('o')
    elif ch == 'u':
        vowel_u.append('u')
    elif ch == ' ':
        spaces.append(' ')
    elif ch in 'qwrtypsdfghjklzxcvbnm':
        consonants.append(ch)
    else:
        print("Invalid.")

print("Vowel a:",len(vowel_a))
print("Vowel e:",len(vowel_e))
print("Vowel i:",len(vowel_i))
print("Vowel o:",len(vowel_o))
print("Vowel u:",len(vowel_u))
print("Spaces:",len(spaces))
print("Consonants:",len(consonants))
