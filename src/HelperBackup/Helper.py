import sys
import json
import os.path

from src.settings.common import *

class HelperClass:

    @staticmethod
    def printt(data, beauty=True):
        """Custom optional print beauty json data

        Args:
            data (list of items): data to print
            beauty (bool, optional): Defines if beauty or normal print. Defaults to True.
        """
        if beauty:
            print(json.dumps(data, indent=2, sort_keys=True))
        else:
            print(data)

    @staticmethod
    def save_data_to_file(data_name, data, overwrite = False, DATA_DIR_PATH = "sample_data"):
        """Save data into json file

        Args:
            data_name (str): file name
            data (list of obj): contains data to save on file
            overwrite (bool, optional): Force overwrite if already exist file. Defaults to False.
        """
        path = f'{DATA_DIR_PATH}/{data_name}.json'
        is_empty_file = False

        if not os.path.isfile(path):
            is_empty_file = True
            open(path, "a")
            with open(path, "w") as write_file:
                json.dump([], write_file)

        if overwrite or is_empty_file:
            with open(path, "w") as write_file:
                json.dump(data, write_file, indent=2, default=str)
        else:
            print ("Data file already exist or is not empty, set overwrite = TRUE to overwrite contents")

    @staticmethod
    def get_data_from_local(data_name):
        """Get data from json file

        Args:
            data_name (str): file name

        Returns:
            list json obj: data from file
        """
        path = f'{DATA_DIR_PATH}/{data_name}.json'

        if os.path.isfile(path):
            with open(path) as json_file:
                return json.load(json_file)
        else:
            print(f'File does not exit at "{path}"')

    @staticmethod
    def input_int():
        """Request user just number type value

        Returns:
            int: console inserted number, otherwise returns error message
        """
        while True:
            try:
                number = int(input("Enter number: "))
                break
            except ValueError:
                print("Number is mandatory. Inserted value is not a number")

        return number

    @staticmethod
    def example_control_exceptions():
        """An example to use error control try except
        """
        randomList = [4, 0, 2]

        for entry in randomList:
            try:
                print("The entry is", entry)
                r = int(1/entry)
                print(r)
                break
            except:
                print("Oops!", sys.exc_info()[0], "occured.")
                print("Next entry.")
                print()

        print("The reciprocal of", entry, "is", r)
