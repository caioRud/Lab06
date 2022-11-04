# Caio Rudloff
def encoder(nums):  # Encoder method
    encoded_num = ""
    for digit in nums:
        var = int(digit) + 3
        if var > 9:  # regulate numbers being above 9
            var -= 10
        encoded_num += chr(var + 48)
    return encoded_num


def decoder(nums):  # Decoder method
    decoded_num = ""
    for digit in nums:
        var = int(digit) - 3
        if var < 0:
            var += 10  # regulate negative numbers
        decoded_num += chr(var + 48)
    return decoded_num


if __name__ == "__main__":  # main
    while True:

        password = input("Please write your 8-digit password\n")  # menu
        print("\nChoose an option:")
        print("1. Encode password")
        print("2. Decode password")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            print(encoder(password))
        elif choice == 2:
            print(decoder(password))
        else:
            break
