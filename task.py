"""task.py"""

def plus_two(number):
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Please only integers")


if __name__ == "__main__":
    plus_two(5)
    plus_two(3.5)
    plus_two("abc")
    plus_two([1, 2, 3])
