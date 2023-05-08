spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = []
# Slicing the complete list will perform a "deep" copy:
spam2 = spam[:]

spam.append('dog')

print('spam', spam)
print('spam2', spam2)