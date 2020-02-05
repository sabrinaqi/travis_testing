def subtract(a, b):
    answer = a - b
    return answer


def interface():
    a = input("Type a number: ")
    b = input("Type another number: ")
    a = float(a)
    b = float(b)
    answer = subtract(a,b)
    print("The difference between {} and {} is {}".format(a, b, answer))

if __name__ == "__main__":
		interface()