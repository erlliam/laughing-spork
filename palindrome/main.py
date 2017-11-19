def reverse(s):
    str = ""
    for i in s:
        print(i)
        print(s)
        str = i + str
    return str

print(reverse("duck"))
