str = input()
def realcount(a, s):
    n = 0
    for i in range(len(s)):
        n += a.count(s[i])
    return(n)
pass
s = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']
print(realcount(str, s))
