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



append_to_file('Christy')
append_to_file('John')


def read_from_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())


read_from_file('names.txt')
print(f'Welcome to this ceremony, {name}')

welcome_guest()

from pypdf import PdfWriter, PdfReader

def write_to_pdf():
    file_name = 'Assignment on Functions & Modules.pdf'
    
    reader = PdfReader(file_name)
    
    writer = PdfWriter()
    writer.add_page(reader.pages[1])
    
    with open('names.pdf', 'wb') as file:
        writer.write(file)

write_to_pdf()