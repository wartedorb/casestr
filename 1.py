str = input()
def realcount(a, s):
    n = 0
    for i in range(len(s)):
        n += a.count(s[i])
    return(n)
pass
s = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
print(realcount(str, s))
