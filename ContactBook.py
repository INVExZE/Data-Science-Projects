'''                       Contact Book
Topics Covered: Lists and Tuples, Dictionaries, File Handling

Description: Create a simple contact book that allows users to add, delete, and search for
contacts. Store contact information in a dictionary and save/load it from a file.'''


while True:
    q = input('Press - Add (a), Search (s), Delete (d) or Quit (q) : ')

    if q == 'a':
        with open('contact.txt', 'a') as f:
            name = input('Name: ')
            phone = input('Phone: ')
            f.writelines((name,' : ',phone, '\n'))

    
    elif q == 's':
        with open('contact.txt','r') as f:
            search = input('Search: ')
            for i in f:
                if search in i:
                    print(i)

    elif q == 'd':
        def delete(name):

            with open('contact.txt') as f:
                data = f.readlines()
            

            if (name == data):
                f.write(name)
                # del data[name]
            else:
                print("The Name doesn't exist.")

        delete_name = input("Enter the Name : ")
        delete(delete_name)

        
