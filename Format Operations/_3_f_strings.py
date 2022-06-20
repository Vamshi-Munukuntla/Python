"""
3. f-strings (String Interpolation)

* Python 3
* f"....String.....{}"

"""

x = 2
y = 3
multiplication = x*y
print(f'{x} multiplied by {y} equals to {multiplication}')

# more pythonic
print(f"{x} * {y} = {x*y}")

# list
info = ['Klark kent', 'Metropolis', 'Daily Planet']

print(f'{info[0]} lives in {info[1]} and work at {info[2]}')

