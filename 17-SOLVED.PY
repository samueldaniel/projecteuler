"""http://projecteuler.net/problem=17"""

words = [{0:'ten',
          1:'eleven',
          2:'twelve',
          3:'thirteen',
          4:'fourteen',
          5:'fifteen',
          6:'sixteen',
          7:'seventeen',
          8:'eighteen',
          9:'nineteen'},
        {0:'',
         1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine'},
        {0:'',
        1:'',
            2:'twenty',
         3:'thirty',
            4:'forty',
            5:'fifty',
            6:'sixty',
            7:'seventy',
            8:'eighty',
            9:'ninety'},
        {0:'hundred'},
        {0:'thousand'}]

def numberToWord(number):
    word = ''
    place = 0

    if number == 1000:
        word = words[1][1] + words[4][0] + word
    else:
        # GRAB RIGHT-TWO DIGITS
        digit = number % 10
        number /= 10
        if number == 0:
            word = words[1][digit] + word
        else:
            nextdigit = number % 10
            number /= 10
            if nextdigit == 1:
                word = words[0][digit] + word
                place += 3
                if number != 0:
                    word = 'and' + word
            else:
                word = words[1][digit] + word
                word = words[2][nextdigit] + word
                place += 3
                if number != 0 and (nextdigit != 0 or digit != 0):
                    word = 'and' + word
            if number != 0: # GRAB THIRD DIGIT
                digit = number % 10
                number /= 10
                word = words[1][digit] + words[place][0] + word

    return word

nums = ''
for num in range(1,1001):
    print numberToWord(num)
    nums = nums + numberToWord(num)

print len(nums)
