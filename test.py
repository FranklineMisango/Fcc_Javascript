name = input()
def ispalindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False

print(ispalindrome(name))