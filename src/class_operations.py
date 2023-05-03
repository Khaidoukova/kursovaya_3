class Operation:

    def __init__(self, date, from_param, to_param):
        self.data = date
        self.from_param = None
        self.to_param = None

    def __repr__(self):
        return f'{self.__class__.__name__}(' \
               f'date = {self.date},' \
               f'from = {self.from_param})' \
               f'to = {self.to_param}'

    def date_formatted(self):
        pass
