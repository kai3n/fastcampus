class stack_custom():

    def __len__(self):
        pass

    def __init__(self):
        self.data = []

    def push(self, data):
        try:
            self.st_list.append(data)
        except:
            raise Exception
        else:
            self.__len__ += 1



