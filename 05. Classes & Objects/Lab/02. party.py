class Party:
    def __init__(self):
        self.party_people = []


party = Party()


current_person = input()

while current_person != "End":
    party.party_people.append(current_person)

    current_person = input()

print(f"Going: {', '.join(party.party_people)}")
print(f"Total: {len(party.party_people)}")
