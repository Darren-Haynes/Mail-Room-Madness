"""Mailroom app for donation center.

Takes user input for donations, allows user to
add names and donations to a dictionary of previous donors
and lets them generate an 'email' to thank the donor for
the donation.


"""

DONORS = {'joe': [40], 'sara': [20, 40, 10], 'nick': [400, 200, 800]}


def show_menu():
    """Display menu for user input."""
    choice = input("""Please choose from the following:\n
        Send a 'Thank You' note - 1\n
        Create a Report.        - 2\n
        Exit                    - 3\n""")
    if choice == '1':
        thank_you()
        return True
    elif choice == '2':
        create_report()
        return True
    elif choice == '3':
        print("Goodbye.")
        exit_program()
        return True
    else:
        print("Please choose a valid option.")
        show_menu()
