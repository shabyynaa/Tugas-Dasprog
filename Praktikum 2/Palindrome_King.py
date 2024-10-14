# input string
string = input()
N = len(string)

# identifikasi apakah palidrome
if string == string[::-1]:
    print("Palindrome King!")
else:
    print("Bukan King!")