"""Mailroom app for donation center.

Takes user input for donations, allows user to
add names and donations to a dictionary of previous donors
and lets them generate an 'email' to thank the donor for
the donation.


"""

DONORS = {'Joe Colling': [40],
          'Sara Williams': [20, 40, 10],
          'Nick Clause': [400, 200, 800],
          'Jenny Smith': [10000, 8000, 900],
          'Darryl Biggins': [100, 150, 100, 100, 150]}


def update_donor_info(name, donation):
    if name in DONORS:
        DONORS[name].append(int(donation))
    else:
        DONORS[name] = [int(donation)]


def input_name():
    return input("\nPlease type a full name: ").title()


def enter_donation():
    return input("Please input donors donation amount: ")


def thank_you():
    name = input_name()
    while name.lower() == 'list':
        print_donor_list()
        name = input_name()
    donation = enter_donation()
    update_donor_info(name, donation)
    print("""\nDear {0},
Thank you for your generous ${1:.2f} donation\n\n""".format(name, float(donation)))
    #show_menu()


def print_report(input_list):
    print("\n\n\n***********************************************************************")
    print("Donors listed by greatest donations".upper())
    print("{0}         {1}    {2}    {3}".format("NAME", "AVG. DONATION", "TOTAL DONATION", "NUM DONATIONS"))
    for donor in input_list:
        name = donor[0]
        total = sum(donor[1])
        number = len(donor[1])
        average = total / number
        print("{0:10s}    {1:10.2f}    {2:15.2f}    {3:10d}".format(name, float(average), float(total), number))
    print("**********************************************************************\n\n\n\n")

def print_donor_list():
    for donor in DONORS:
        print (donor)

def create_report():
    sorted_by_total = sorted(
        DONORS.items(), key=lambda donor: sum(donor[1]), reverse=True)
    print_report(sorted_by_total)
    #mailroom_main()

def exit_program():
    KeyboardInterrupt()

def mailroom_main():
    """Logic for the mailroom program."""
    choice = 0
    while choice != '3':
        choice = show_menu()
        if choice == '1':
            thank_you()
        elif choice == '2':
            create_report()
        elif choice == '3':
            break
        else:
            print("Please choose a valid option.")
            #mailroom_main()

    print("Goodbye.")
    exit_program()

def show_menu():
    """Display menu for user input."""
    return input("""Please choose from the following:\n
        Send a 'Thank You' note - 1\n
        Create a Report.        - 2\n
        Exit                    - 3\n""")

if __name__ == '__main__':
    mailroom_main()
