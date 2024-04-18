a = 2021

def is_year_leap(a):
    if (a % 4 == 0):
        return True
    else:
        return False

new = is_year_leap(a)

print ("год ", a, ":",  new)
