from operator import truediv


word1 = input()
word2 = input()
word1, word2 = list(word1), list(word2)
word1.sort()
word2.sort()

same = True

for i in range(len(word1)):
    if word1[i] != word2[i]:
        same = False
        break

output = {0:"Not anagrams", 1:"Anagrams"}
print(output[same])