"""
try:
    ...
    ........
    .....
except Ex1:
    ......
    ..........
except Ex2:
    .............
    ..........
    .................
    ....
else:
    ......
    ..........
    .........
finally:
    No matter what happens with the code, if it contains error or not,
    Finally block will execute.

"""

# Ex:
#
#
# def division(x, y):
#     try:
#         print("x:", int(x))
#         print("y:", int(y))
#     except ValueError as e:
#         print("Value Error", e)
#     except ZeroDivisionError as e:
#         print("Error:", e)
#     else:
#         result = x / y
#         print("Result:", result)
#     finally:
#         print('Finally block is executed')
#
#
# division(4,'dsxw')

# Ex:
# Without using Else block.


# def division(x, y):
#     try:
#         print("x:", int(x))
#         print("y:", int(y))
#         result = x / y
#         print("Result:", result)
#     except ValueError as e:
#         print("Value Error", e)
#     except ZeroDivisionError as e:
#         print("Error:", e)
#     finally:
#         print('Finally block is executed')
#
#
# division(4,'dsxw')


# Ex:
# Close the file in finally block

def open_file(path):
    try:
        file = open(path)
    except Exception as e:
        print(e)
    else:
        print(file.read())
    finally:
        try:
            file.close()
            print('Closing the File...')
        except:
            pass


open_file('Series.txt')

