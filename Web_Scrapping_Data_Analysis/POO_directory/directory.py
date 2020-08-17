from contact import Contact

class Directory():

    def __init__(self):
        self._directory = {}

    def add_author(self, name, quote):

        if name in self._directory:
            print('The author already exists, do you want update the author')
        else:
            author = Contact(name, quote)
            self._directory[author.get_name()] = author

    def show_authors(self):

        for author in self._directory.keys():
            print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
            print(author)

    def show_author_quote(self, author):
        quote_id = int(input('Cual cita quiere ver?'))
        return self._directory[author].get_quote(quote_id)

    def show_author_quotes(self, author):
        self._directory[author].get_quotes()
        return self._directory[author].count_quotes()
    def update_info(self, **data):
        self._directory[data['new_name']] = self._directory[data['autor']]
        self._directory[data['new_name']].update_name(data['new_name'])
        self._directory[data['new_name']].update_quot(data['num_quot'], data['new_quot'])

    def delete_quote(self, author):
        id = int(input('Cual cita quiere eliminar?'))
        self._directory[author].delete_quote(id)

    def delete_author(self, author):
        del self._directory[author]

if __name__ == '__main__':

    directory_test = Directory()
    name = str(input('Ingrese el nombre del autor :'))
    quote = str(input('Ingrese la cita :'))
    directory_test.add_author(name, quote)

    directory_test.show_authors()
    directory_test.show_author_quotes(name)
