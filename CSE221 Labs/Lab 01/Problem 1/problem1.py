file = open('F:\CODES\Python_VS\CSE221 Labs\Lab 01\Problem 1\input.txt', 'r')

text = file.readlines()
inputs = []

total_input = 0

odd = 0
even = 0
no_parity = 0
palindrome = 0
not_palindrome = 0

for i in text:
    i = i.rstrip('\n')
    inputs.append(i)

    total_input += 1

# print(inputs[2].split(' ')[1])

def parity(num):

    global odd, even, no_parity

    if '.' not in num:
        num = int(num)

        if num%2==0:
            even += 1
            return (f'{num} has even parity')

        else:
            odd += 1
            return (f'{num} has odd parity')
    
    else:
        no_parity += 1
        return f'{num} cannot have a parity'

def isPalindrome(string):

    global palindrome, not_palindrome

    if string is None:
        palindrome += 1
        return f'{string} is not a palindrome'

    N = int(len(string))

    for i in range(int(N/2)):

        if string[i] != string[N-1-i]:
            not_palindrome += 1
            return f'{string} is not a palindrome'

    palindrome += 1
    return f'{string} is a palindrome'

for i in inputs:

    i = i.split(' ')
    output = f'{parity(i[0])} and {isPalindrome(i[1])} \n'

    f = open('F:\CODES\Python_VS\CSE221 Labs\Lab 01\Problem 1\output.txt', 'a')
    f.writelines(output)
    
f.close()

record = f'Percentage of odd parity: {(odd*100)/total_input}%\nPercentage of even parity: {(even*100)/total_input}%\nPercentage of no parity: {(no_parity*100)/total_input}%\nPercentage of palindrome: {(palindrome*100)/total_input}%\nPercentage of non-palindrome: {(not_palindrome*100)/total_input}%'

f = open("F:\\CODES\\Python_VS\\CSE221 Labs\\Lab 01\\Problem 1\\record.txt", 'a')
f.writelines(record)
f.close