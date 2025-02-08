def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm, including numbers.

    Parameters:
    text (str): The input message to be processed.
    shift (int): The number of positions to shift each character.

    Returns:
    str: The processed message after encryption or decryption.
    """
    result = []
    for char in text:
        if char.isupper():
            # Process uppercase letters (shift mod 26)
            shifted = (ord(char) - ord('A') + shift) % 26
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            # Process lowercase letters (shift mod 26)
            shifted = (ord(char) - ord('a') + shift) % 26
            result.append(chr(shifted + ord('a')))
        elif char.isdigit():
            # Process digits (shift mod 10)
            shifted = (ord(char) - ord('0') + shift) % 10
            result.append(chr(shifted + ord('0')))
        else:
            # Leave non-alphabetic and non-digit characters unchanged
            result.append(char)
    return ''.join(result)

def main():
    """Main function to handle user input and execute the cipher."""
    # Get user input for message
    message = input("Enter your message: ")

    # Validate and get shift value
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")

    # Validate and get mode (Encrypt/Decrypt)
    while True:
        mode = input("Choose mode - Encrypt (E) or Decrypt (D): ").strip().upper()
        if mode in ('E', 'D'):
            break
        print("Invalid mode. Please enter 'E' for Encrypt or 'D' for Decrypt.")

    # Adjust shift for decryption
    if mode == 'D':
        shift = -shift

    # Process the message
    processed_text = caesar_cipher(message, shift)
    print("\nResult:")
    print(processed_text)

if __name__ == "__main__":
    main()