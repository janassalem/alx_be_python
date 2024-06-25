# Filename: multiplication_table.py

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        
        for i in range(1, 11):
            print(f"{number} * {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()