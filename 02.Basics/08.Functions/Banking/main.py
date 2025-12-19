import modules


def main():

    print("Welcome to the Malayora Banking Service!")

    while True:
        print("Press 1 -> Check Balance")
        print("Press 2 -> Make Deposite")
        print("Press 3 -> Make Withdrawal")
        print("Press 4 -> Cancel the process")

        user_input = input("Press here: ")
        if user_input == "1":
            response = modules.show_balance()
            print(f"{response}")
        elif user_input == "2":
            amount = float(input("Enter the deposite amount: "))
            response = modules.make_deposite(amount)
            print(response)

        elif user_input == "3":
            amount = float(input("Enter the withdrawal amount: "))
            response = modules.make_withdrawal(amount)
            print(response)

        elif user_input == "4":
            response = modules.cancel_process()
            print(response)
            break
        else:
            print("Invalid input, Please try again")
            user_input = input("Press here: ")


if __name__ == "__main__":
    main()
