import json
from multiprocessing.sharedctypes import Value
from src.Helpers.Helpers import HelperClass


class PersonManager:
    __name = []
    __age  = []
    __age_status = []
    __dni     = []
    __weight  = []
    __height  = []
    __address = []
    __sex = []
    __bmi = []
    __idx = 0
    __EXIT_OPT_POS        = 0
    __INSERT_DATA_OPT_POS = 1
    __menu_options = [
        "Exit",
        "Insert data",
        "Calc person weight",
        "Calc is adult",
        "Calc sex percent",
        "Get data",
    ]
    __current_opt = None
    __data = {}

    def __init__(self, config, logger):
        self.MIN_REQ_MENU_OPTIONS = [self.__INSERT_DATA_OPT_POS, self.__EXIT_OPT_POS]
        self.config               = config
        self.logger               = logger

    def start(self):
        self.__print_options()
        self.__input_option()
        result = self.__run_option()

        if not result == None:
            return result

    def __print_options(self):
        print("")
        for idx in range(0, len(self.__menu_options)): self.__print_option(idx)
        print("")

    def __print_option(self, position):
        if not self.__is_empty_data():
            print(f'{position}) ', self.__get_option_name_for(position))
        elif position in self.MIN_REQ_MENU_OPTIONS:
            print(f'{position}) ', self.__get_option_name_for(position))

    def __get_option_name_for(self, idx):
        return self.__menu_options[idx]

    def __is_empty_data(self):
        return (self.__idx <= 0)

    def __input_option(self):
        while True:
            self.__current_opt = HelperClass.input_int(
                message           = "Insert option: ",
                required_positive = True
            )
            if not self.__is_valid_option():
                print(f'Not valid menu option \'{self.__current_opt}\'')
                continue
            print("Current")
            break

    def __run_option(self):
        if self.__current_opt == self.__EXIT_OPT_POS: self.__exit()
        elif self.__current_opt == self.__INSERT_DATA_OPT_POS: self.__insert_data()
        elif self.__current_opt == 2:
            self.__calc_bmi()
            self.__print_values_for(data = self.__bmi, tag = 'BMI', units = "kg/m")
        elif self.__current_opt == 3:
            self.__calc_is_adult()
            self.__print_values_for(data = self.__age_status, tag = 'Age status')
        elif self.__current_opt == 4:
            self.__calc_categoric_sex_percent()
            self.__print_categoric_sex_percent()
        elif self.__current_opt == 5: return self.__get_data()
        return None

    def __is_valid_option(self):
        is_minimum_required_option = self.__is_empty_data and self.__current_opt in self.MIN_REQ_MENU_OPTIONS
        is_option_in_menu = self.__current_opt < len(self.__menu_options)
        is_correct_opt = is_minimum_required_option or is_option_in_menu
        if not is_correct_opt: return False
        return True

    def __exit(self):
        self.logger.log.info("Exit program")
        exit()

    def __insert_data(self):
        print(f'Total people to insert: {self.config.n_people}')
        print("Insert person data\n")
        self.__idx = 0
        while self.__idx < self.config.n_people:
            self.__insert_row()
            self.__idx += 1
            print("")

        self.logger.log.info("Data saved correctly")
        self.__save_data()

    def __save_data(self):
        self.__data = {
            "name": self.__name,
            "age":  self.__age,
            "age_status": self.__age_status,
            "dni":     self.__dni,
            "weight":  self.__weight,
            "height":  self.__height,
            "address": self.__address,
            "sex":     self.__sex,
            "bmi":     self.__bmi,
            "idx":     self.__idx,
            "man_percentage": 0,
            "woman_percentage": 0
        }

    def __insert_row(self):
        user_num = self.__idx + 1
        self.__name.append(
            HelperClass.input_str(f'({user_num}) Insert name: ')
        )
        self.__age.append(
            HelperClass.input_int(
                message = f'({user_num}) Insert age: ',
                required_positive = True,
                allowed_zero = False
            )
        )
        self.__sex.append(
            HelperClass.input_str(
                message = f'({user_num}) Insert sex [man(m) | woman(w)]: ',
                options = ['m', 'w']
            )
        )
        self.__dni.append(
            HelperClass.input_str(f'({user_num}) Insert dni: ')
        )
        self.__weight.append(
            HelperClass.input_float(
                message = f'({user_num}) Insert weight (kg): ',
                required_positive = True,
                allowed_zero = False
            )
        )
        self.__height.append(
            HelperClass.input_float(
                message = f'({user_num}) Insert height: (m): ',
                required_positive = True,
                allowed_zero = False
            )
        )
        self.__address.append(
            HelperClass.input_str(f'({user_num}) Insert address: ')
        )

    def __calc_bmi(self):
        """
        BMI = weight(kg) / height(m)
        """
        self.logger.log.info("Calc people BMI")
        self.__bmi = [ (self.__weight[idx] / self.__height[idx]) for idx in range(0, len(self.__weight)) ]
        self.__data['bmi'] = self.__bmi

    def __print_values_for(self, data, tag, units = ""):
        for idx, val in enumerate(data):
            print(f'{self.__name[idx]} ({tag}): {val} {units}')

    def __calc_is_adult(self):
        self.logger.log.info("Calc if people is adult")
        self.__age_status = ["Adult" if (age > 18) else "NO adult" for age in self.__age]
        self.__data['age_status'] = self.__age_status

    def __calc_categoric_sex_percent(self):
        self.logger.log.info("Calc people categoric sex percent")
        self.__data['man_percentage'] = (sum([1 if sex == 'm' else 0 for sex in self.__sex]) / self.__idx) * 100
        self.__data['woman_percentage'] = (sum([1 if sex == 'w' else 0 for sex in self.__sex]) / self.__idx) * 100

    def __print_categoric_sex_percent(self):
        man_perc = self.__data['man_percentage']
        wom_perc = self.__data['woman_percentage']
        print(f'Man percentage {man_perc} %')
        print(f'Woman percentage {wom_perc} %')

    def __get_data(self):
        self.logger.log.info("Getting data")
        return self.__data