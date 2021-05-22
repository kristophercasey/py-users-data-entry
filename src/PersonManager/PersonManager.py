from src.Helpers.Helpers import HelperClass


class PersonManager:
    __menu_options = [
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
        # self.__name = []
        # self.__age = []
        # self.__dni = []
        # self.__weight = []
        # self.__height = []
        # self.__address = []
        # self.__sex = []
        self.__imc = []
        self.__idx = 0
        self.__current_opt = None

        self.__name = ['Sergio', 'Cris']
        self.__age = [30, 29]
        self.__dni = ["DNI 1", "DNI 2"]
        self.__weight = [85.1, 70.0]
        self.__height = [1.75, 1.7]
        self.__address = ["adress 1", "adress 2"]
        self.__sex = ['m', 'w']
        self.__idx = 2

        self.config = config
        self.logger = logger

    def print_options(self):
        print("")
        for idx, opt in enumerate(self.__menu_options):
            if self.__is_filled_data(): print(f'{idx}) ', opt)
            elif idx in self.MIN_REQ_MENU_OPTIONS: print(f'{idx}) ', opt)

    def request_option(self):
        self.__current_opt = HelperClass.input_int(
            message = "Insert option: ",
            required_positive = True
        )


    def run_option(self):
        if not self.__is_valid_option():
            print(f'Not valid menu option \'{self.__current_opt}\'')
            return


    def __is_valid_option(self):
        is_correct_opt = self.__is_filled_data() and self.__current_opt < len(self.__menu_options)
        is_minimum_required_options = self.__current_opt in self.MIN_REQ_MENU_OPTIONS
        is_option_in_menu = is_correct_opt or is_minimum_required_options
        if not is_option_in_menu: return False

        return True

    def __is_filled_data(self):
        return self.__idx > 0
