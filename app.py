def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    input_str = input("Enter a string to reverse: ")
    print(f"Reversed: {reverse_string(input_str)}")