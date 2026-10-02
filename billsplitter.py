from random import choice
party_dict = {}
party_size = int(input("Enter the number of friends joining (including you):\n"))

if party_size < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(party_size):
        party_dict[input()] = 0
    bill_total = int(input("Enter the total bill value:\n"))
    if input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n") == "Yes":
        lucky_person = choice(list(party_dict.keys()))
        party_size -= 1
        print(f"{lucky_person} is the lucky one!")
    else:
        lucky_person = False
        print("No one is going to be lucky")
    bill_split = round((bill_total / party_size), 2)
    for person in party_dict.keys():
        if person != lucky_person:
            party_dict[person] = bill_split
    print(party_dict)
