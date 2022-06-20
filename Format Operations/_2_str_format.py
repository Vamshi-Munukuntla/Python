"""
2 - String Format

str.format()
formatting with {}
"""

# without indexing

hi = 'Hi there {} {}.'
print(hi.format('Bruce', 'Wayne'))

# with indexing
hell = 'Hi {2}{3} aka {0}{1}'
print(hell.format('Bat', 'man', 'Bruce', 'Wayne'))

# Parameter names
text = '{n} comes from {s}'
source = text.format(n = 'Python',s = 'Monty Python and Holy Grail')
print(source)
