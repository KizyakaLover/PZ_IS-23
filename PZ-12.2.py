import string

stroke = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

lowercase_chars = [let for let in stroke if let in string.ascii_lowercase]

print('Символы нижнего регистра:',' '.join(lowercase_chars))
