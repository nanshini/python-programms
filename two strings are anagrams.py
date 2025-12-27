s="eat"
r="aae"
def anagram(s,r):
    for char in s:
       if char not in r:
            return "not anagram"
    return "anagram"
print(anagram(s,r))
