


class PersonManager:
    menu_options = [
        "Exit",
        "Insert data",
        "Calc person weight",
        "Calc document",
        "Calc is adult",
        "Calc sex percent",
        "Calc weight percent",
        "Calc age percent",
        "Get data",
    ]
    EXIT_OPT_POS = 0
    INSERT_DATA_OPT_POS = 1

    def __init__(self, config, logger):
        self.MIN_REQ_MENU_OPTIONS = [self.INSERT_DATA_OPT_POS, self.EXIT_OPT_POS]
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
        for idx, opt in enumerate(self.menu_options):
            is_print_for_filled_data = self.__idx > 0
            if is_print_for_filled_data: print(f'{idx}) ', opt)
            elif idx in self.MIN_REQ_MENU_OPTIONS: print(f'{idx}) ', opt)
