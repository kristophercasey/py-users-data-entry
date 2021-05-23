from src.Helpers.Helpers import HelperClass


class PersonManager:
    __menu_options = [
        "Exit",
        "Insert data",
        "Calc person weight",
        "Calc document",
        "Calc is adult",
        "Calc sex percent",
        "Get data",
    ]
    EXIT_OPT_POS = 0
    INSERT_DATA_OPT_POS = 1

    def __init__(self, config, logger):
        self.MIN_REQ_MENU_OPTIONS = [self.INSERT_DATA_OPT_POS, self.EXIT_OPT_POS]
        self.__name = []
        self.__age = []
        self.__age_status = []
        self.__dni = []
        self.__weight = []
        self.__height = []
        self.__address = []
        self.__sex = []
        self.__imc = []
        self.__idx = 0
        self.__current_opt = None

        self.config = config
        self.logger = logger

    def print_options(self):
        print("")
        for idx, opt in enumerate(self.__menu_options):
            if (self.__idx > 0): print(f'{idx}) ', opt)
            elif idx in self.MIN_REQ_MENU_OPTIONS: print(f'{idx}) ', opt)

    def request_option(self):
        self.__current_opt = HelperClass.input_int(
            message = "Insert option: ",
            required_positive = True
        )
        self.__data = {
            "name": self.__name,
            "age": self.__age,
            "age_s": self.__age_status,
            "dni": self.__dni,
            "weight": self.__weight,
            "height": self.__height,
            "address": self.__address,
            "sex": self.__sex,
            "imc": self.__imc,
            "idx": self.__idx,
        }

    def run_option(self):
        if not self.__is_valid_option():
            print(f'Not valid menu option \'{self.__current_opt}\'')
            return

        if self.__current_opt == 0: self.__exit()
        elif self.__current_opt == 1: self.__insert_data()
        elif self.__current_opt == 2: self.__calc_imc()
        elif self.__current_opt == 3: self.__calc_document()
        elif self.__current_opt == 4: self.__calc_is_adult()
        elif self.__current_opt == 5: self.__calc_categoric_sex_percent()
        elif self.__current_opt == 6: self.__calc_categoric_weight_percent()
        elif self.__current_opt == 7: self.__calc_categoric_age_percent()
        elif self.__current_opt == 8: self.__get_data()

    def __is_valid_option(self):
        is_correct_opt = (self.__idx > 0) and self.__current_opt < len(self.__menu_options)
        is_minimum_required_options = self.__current_opt in self.MIN_REQ_MENU_OPTIONS
        is_option_in_menu = is_correct_opt or is_minimum_required_options
        if not is_option_in_menu: return False
        return True

    def __exit(self):
        self.logger.log.info("Exit program")
        exit()

    def __insert_data(self):
        print("Insert person data")
        print(f'People to insert: {self.config.n_people} \n')
        self.__idx = 0
        while self.__idx < self.config.n_people:
            user_num = self.__idx + 1
            self.__name.append(HelperClass.input_str(f'({user_num}) Insert name: '))
            self.__age.append(HelperClass.input_int(message = f'({user_num}) Insert age: ', required_positive = True, allowed_zero = False))
            self.__sex.append(HelperClass.input_str(message = f'({user_num}) Insert sex [man(m) | woman(w)]: ', options = ['m', 'w']))
            # self.__dni.append(HelperClass.input_str(f'({user_num}) Insert dni: '))
            self.__weight.append(HelperClass.input_float(message = f'({user_num}) Insert weight (kg): ', required_positive = True, allowed_zero = False))
            self.__height.append(HelperClass.input_float(message = f'({user_num}) Insert height: (m)', required_positive = True, allowed_zero = False))
            # self.__address.append(HelperClass.input_str(f'({user_num}) Insert address: '))
            self.__idx += 1
            print("")

        self.logger.log.info("Data saved correctly")

    def __calc_imc(self):
        """
        IMC = weight(kg) / height(m)
        """
        self.logger.log.info("Calc people imc")
        self.__imc = [ (self.__weight[idx] / self.__height[idx]) for idx in range(0, len(self.__weight)) ]
        for idx, imc in enumerate(self.__imc):
            print(self.__name[idx], "(imc): ", imc)

    def __calc_document(self):
        self.logger.log.info("Calc document")

    def __calc_is_adult(self):
        self.__age_status = ["Adult" if (age > 18) else "NO adult" for age in self.__age]
        self.logger.log.info(f'Calc is adult {self.__age_status}')

    def __calc_categoric_sex_percent(self):
        self.logger.log.info("Calc categoric sex percent")
        man_percentage = (sum([1 if sex == 'm' else 0 for sex in self.__sex]) / self.__idx) * 100
        woman_percentage = (sum([1 if sex == 'w' else 0 for sex in self.__sex]) / self.__idx) * 100
        print(f'Man percentage {man_percentage} %')
        print(f'Woman percentage {woman_percentage} %')

    def __get_data(self):
        self.logger.log.info("Getting data")
        return self.__data