


class PersonManager:
    def __init__(self, config, logger):
        self.menu_options = [
            "1) Insert data",
            "2) Calc person weight",
            "3) Calc document",
            "4) Calc is adult",
            "5) Calc sex percent",
            "6) Calc weight percent",
            "7) Calc age percent",
            "8) Get data",
            "0) Exit",
        ]
        self.config = config
        self.logger = logger

        self.__name = []
        self.__age = []
        self.__dni = []
        self.__weight = []
        self.__height = []
        self.__address = []
        self.__sex = []
        self.__imc = []
        self.__age_status = None
        self.__idx = 0

    def print_menu(self):
        for opt in self.menu_options: print(opt)
