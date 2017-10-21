"""Mailroom app for donation center.

Takes user input for donations, allows user to
add names and donations to a dictionary of previous donors
and lets them generate an 'email' to thank the donor for
the donation.


"""

DONORS = {'Joe': [40], 'Sara': [20, 40, 10], 'Nick': [400, 200, 800]}


def update_donor_info(name, donation):
    if name in DONORS:
        DONORS[name].append(donation)
    else:
        DONORS[name] = [donation]


def input_name():
    return  input("\nPlease type a full name: ").title()


def enter_donation():
    return input("Please input donors donation amount: ")


def thank_you():
    name = input_name()
    donation = enter_donation()
    update_donor_info(name, donation)
    print("""Dear {},
Thank you for your generous ${} donation""".format(name, donation))
    show_menu()


def print_report(input_list):
    print("Donors listed by greatest donations".upper())
    for donor in input_list:
        name = donor[0]
        total = sum(donor[1])
        number = len(donor[1])
        average = total / number
    print(name, average, total, number)

def create_report():
    sorted_by_total = sorted(
        DONORS.items(), key=lambda donor: sum(donor[1]), reverse=True)
    print_report(sorted_by_total)

def mailroom_main():
    """Logic for the mailroom program."""
    choice = show_menu()
    if choice == '1':
        thank_you()
    elif choice == '2':
        create_report()
    elif choice == '3':
        print("Goodbye.")
        exit_program()
    else:
        print("Please choose a valid option.")
        mailroom_main()


def show_menu():
    """Display menu for user input."""
    return input("""Please choose from the following:\n
        Send a 'Thank You' note - 1\n
        Create a Report.        - 2\n
        Exit                    - 3\n""")

if __name__ == '__main__':
    mailroom_main()
