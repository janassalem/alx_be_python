# Filename: pattern_drawing.py

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            for i in range(size):
                for j in range(size):
                    print("*", end="")
                print()  # Move to the next line after printing a row
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()