

class Contact:
    _name_author = ''
    _quotes = []
    def __init__(self, name, quote):
        self._name_author = name
        self._quotes.append(quote)

    def get_name(self):
        return self._name_author

    def update_name(self, name):
        self._name_author = name

    def get_quote(self, num_quot):
        return self._quotes[num_quot]

    def get_quotes(self):
        if len(self._quotes)>0:
            id = 1
            for quote in self._quotes:
                print(str(id)+' : '+quote+'\n')
                id += 1
        else:
            print('No hay citas disponibles')

    def add_quote(self, quote):
        self._quotes.append(quote)

    def update_quot(self, num_quot, new_quot):
        self._quotes[num_quot] = new_quot

    def delete_quote(self, num_quot):
        del self._quotes[num_quot-1]

    def count_quotes(self):
        return print('Number of quotes :' + str(len(self._quotes)))


if __name__ == '__main__':
    Contact_example = Contact('pepito', 'Hi, I am here')
    print('The name of author is:', Contact_example.get_name())
    print('The name of author is:', Contact_example.get_quote(0))
    quote = str(input('Ingrese la cita del autor: '))
    Contact_example.add_quote(quote)
    Contact_example.get_quotes()
    Contact_example.count_quotes()































