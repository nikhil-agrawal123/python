import json

x = {}
with open('Q6.json', 'r') as f:
    contacts = json.load(f)
x = contacts    

def new_entry(contacts):
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    if name not in contacts.keys():
        contacts[name] = {
        'address': address,
        'phone': phone,
        'email': email
    }
    else:
        x = contacts[name]
        del contacts[name]
        contacts[name] = [x, {
        'address': address,
        'phone': phone,
        'email': email
        }]

def delete_entry(contacts):
    name = input("Enter name: ")
    if name in contacts:
        if type(contacts[name]) == dict:
            del contacts[name]
        else:
            print("Multiple entries found")
            for i in range(len(contacts[name])):
                print(i+1, contacts[name][i])
            choice = int(input("Enter choice: "))
            del contacts[name][choice-1]
            if len(contacts[name]) == 1:
                contacts[name] = contacts[name][0]
    else:
        print("Name not found")

def partial_name(contacts):
    name = input("Enter partial name: ")
    for key in contacts:
        if name in key:
            if type(contacts[key]) == dict:
                print(key, contacts[key])
            else:
                for i in range(len(contacts[key])):
                    print(key, contacts[key][i])

def search_entry_other_way(contacts):
    print("Search by address, phone or email")
    ty = input("Enter type of search: ")
    
    if ty == 'address':
        address = input("Enter address: ")
        for key in contacts:
            if type(contacts[key]) == dict:
                if address == contacts[key]['address']:
                    print(key, contacts[key])
            else:
                for i in range(len(contacts[key])):
                    if address == contacts[key][i]['address']:
                        print(key, contacts[key][i])
    elif ty == 'phone':
        phone = input("Enter phone number: ")
        for key in contacts:
            if type(contacts[key]) == dict:
                if phone == contacts[key]['phone']:
                    print(key, contacts[key])
            else:
                for i in range(len(contacts[key])):
                    if phone == contacts[key][i]['phone']:
                        print(key, contacts[key][i])
    elif ty == 'email':
        email = input("Enter email: ")
        for key in contacts:
            if type(contacts[key]) == dict:
                if email == contacts[key]['email']:
                    print(key, contacts[key])
            else:
                for i in range(len(contacts[key])):
                    if email == contacts[key][i]['email']:
                        print(key, contacts[key][i])
    else:
        print("Invalid type")

def main(contacts):
    while True:
        print("1. New entry")
        print("2. Delete entry")
        print("3. Partial name search")
        print("4. Search entry other way")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            new_entry(contacts)
        elif choice == '2':
            delete_entry(contacts)
        elif choice == '3':
            partial_name(contacts)
        elif choice == '4':
            search_entry_other_way(contacts)
        elif choice == '5':
            for i in contacts:
                print(i, contacts[i])
            with open('Q6.json', 'w') as f:
                json.dump(contacts, f,indent=4)
            break
        else:
            print("Invalid choice")

main(x)

def test():
    assert delete_entry({'a': {'address': 'a', 'phone': '1', 'email': 'a'}, 'b': {'address': 'b', 'phone': '2', 'email': 'b'}}) == None

test()