def create_file(file_name):

    with open(file_name, 'x') as file:
        pass


# create_file('christy.pdf')

def write_to_file(text):

    with open('names.txt', 'w') as file:
        file.write(text + '\n')

write_to_file('Christy')

write_to_file('Onanse')


def append_to_file(text):
    file = open('names.txt', 'a')
    file.write(text + '\n')

    file.close()

append_to_file('Christy')