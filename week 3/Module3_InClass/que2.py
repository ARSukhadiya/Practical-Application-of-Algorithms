def validate_parentheses(input_s):
    opening_bkts = []

    for i in range(len(input_s)):

        if input_s[i] in "({[":
            opening_bkts.append(input_s[i])

        else:
            if (input_s[i] in ")]}") and (ord(input_s[i])-2 == ord(opening_bkts.pop())):
                continue
            else:
                return False
    
    return True

input_s = "()[]{}"
print(validate_parentheses(input_s))
