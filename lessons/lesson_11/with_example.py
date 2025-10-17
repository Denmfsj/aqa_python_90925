


# with open("example.txt", "r") as file:  # менеджер контексту
#     content = file.read()
#     print(content)


class FileReadWrite:

    def __init__(self, path_to_file, write=True):
        self.path_to_file = path_to_file

        self.mode = 'r' if write is False else 'w'  # r if write = False, w if write = True
        self.__file_obj = None
        # if write is False:
        #     self.mode = 'r'
        # else:
        #     self.mode = 'w'

    def __enter__(self):
        self.__file_obj = open(self.path_to_file, self.mode)
        return self.__file_obj


    def __exit__(self, exc_type, exc_val, exc_tb):

        # якщо файл був відкритий - то закрий
        if self.__file_obj:
            self.__file_obj.close()


            # додавання в кінець файлу строки \nlast row from __exit__
            f = open(self.path_to_file, 'a')
            f.write('\nlast row from __exit__')
            f.close()

    def do_smth(self):
        pass


with FileReadWrite("example.txt", write=False) as file:  # менеджер контексту
    raise ValueError('asdasd')
    content = file.read()
    print(content)

print('Done')
