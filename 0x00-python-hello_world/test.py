def main():
    for num in range(1, 101):
        if (num % 3 == 0) & (num % 5 == 0):
            print(f"FizzBuzz", end=" ")
        elif (num % 3 == 0):
            print(f"Fizz", end=" ")
        elif (num % 5 == 0):
            print(f"Buzz", end=" ")
        else: 
            print(f"{num}", end=" ")


if __name__ == "__main__":
    main()
