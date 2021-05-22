

class HelperClass:

    @staticmethod
    def input_int(message, required_positive = False, allowed_zero = True):
        """
        Request input only integer type allowed. Configurable validate positive and zero values.

        Args:
            message (str): Input message
            required_positive (bool, optional): Force input to be positive number. Defaults to False.
            allowed_zero (bool, optional): Validate number to allow zero value. Defaults to True.

        Returns:
            int: console inserted value that pass configured rules(required_positive and allowed_zero)
        """

        int_value = 0
        while True:
            try:
                int_value = int(input(message))
                is_positive = (int_value >= 0) and required_positive
                is_zero = ((int_value == 0) and allowed_zero)
                is_valid = is_positive and (is_zero or (int_value != 0))
                if not is_valid:
                    type_value = type(int_value)
                    print(f'Integer number > 0 is mandatory. Inserted value is \'{int_value}\' {type_value}')
                    continue
                break
            except ValueError:
                print("Value type integer is mandatory.")

        return int_value


    @staticmethod
    def input_float(message, required_positive = False, allowed_zero = True):
        """
        Request input only float type allowed. Configurable validate positive and zero values.

        Args (rules):
            message (str): Input message
            required_positive (bool, optional): Force input to be positive number. Defaults to False.
            allowed_zero (bool, optional): Validate number to allow zero value. Defaults to True.

        Returns:
            float: console inserted value that pass configured rules(required_positive and allowed_zero)
        """
        float_value = 0
        while True:
            try:
                float_value = float(input(message))
                is_positive = (float_value >= 0) and required_positive
                is_zero = ((float_value == 0) and allowed_zero)
                is_valid = is_positive and (is_zero or (float_value != 0))
                if not is_valid:
                    type_value = type(float_value)
                    print(f'Float number > 0.0 is mandatory. Inserted value is \'{float_value}\' {type_value}')
                    continue
                break
            except ValueError:
                print("Value type float is mandatory.")

        return float_value


    @staticmethod
    def input_str(message = "", options = []):
        opt = ""
        while True:
            opt = input(message)
            if (len(options) > 0) and (opt not in options):
                type_opt = type(opt)
                print(f'Specific value is mandatory. Inserted value is \'{opt}\' {type_opt}')
                continue
            else:
                break

        return opt
