import configparser
import platform
import logging
import sys


import sys, logging, platform, configparser

class EnvLoader:
    __CONFIG_PATH = "config"
    __CONFIG_FILE = "default.ini"
    DIR_SEP = None
    ENV_TYPE = None
    CONFIG = None

    app_version = None
    app_debug = None
    sample_data_path = None

    log_path = None
    log_level = None
    log_identifier = None

    file_manager_path = None
    file_manager_filename = None
    file_manager_operation = None

    def __init__(self, env_type = "dev"):
        """Environment loader constructor where initialized and config based on environment type

        Args:
            environment (str, optional): Set environment configuration. Defaults to "dev".
        """
        print("Application config")
        print(f'> Environment \'{env_type}\'')
        self.ENV_TYPE = env_type
        self._set_dir_separator_type()

        try:
            config_file_path = self.__get_env_file_path_for(self.__CONFIG_PATH, self.__CONFIG_FILE)

            self.__read_config_file(config_file_path)
            self.__set_environment_config_values()
            self.__print_environment_values()

        except Exception as err:
            print(f'\n Load env function Error ({err})')
            sys.exit(-1)


    def _set_dir_separator_type(self):
        """Define separator type based on machine type
        """
        PLATFORM = platform.system().lower()
        print(f'> Running platform \'{PLATFORM}\' system')
        if PLATFORM == "linux" or PLATFORM == "linux2": self.DIR_SEP = "/"
        elif PLATFORM == "darwin": self.DIR_SEP = "/"
        elif PLATFORM == "win32" or PLATFORM == "win64": self.DIR_SEP = "\\"
        else:
            print(f'> Running platform \'{PLATFORM}\' system is not supported for this ETL')
            sys.exit(-1)

    def __get_env_file_path_for(self, dir_name, file_name):
        env_root_path = self.__get_env_dir_path_for(dir_name)
        env_file_path = f'{env_root_path}{self.DIR_SEP}{file_name}'
        return env_file_path

    def __get_env_dir_path_for(self, dir_name):
        root_path = f'.{self.DIR_SEP}{dir_name}'
        env_root_path = f'{root_path}{self.DIR_SEP}{self.ENV_TYPE}'
        return env_root_path

    def __read_config_file(self, config_file_path):
        print(f'> Reading file path \'{config_file_path}\'')
        self.CONFIG = configparser.ConfigParser()
        self.CONFIG.sections()
        self.CONFIG.read(config_file_path)

    def __set_environment_config_values(self):
        self.app_version = self.CONFIG['APP_INFO']['APP_VERSION']
        self.sample_data_path = self.CONFIG['APP_INFO']['SAMPLE_DATA_PATH']
        self.app_debug = self.CONFIG['APP_INFO']['DEBUG']

        self.log_path = self.CONFIG['LOGGING']['LOG_PATH']
        self.log_level = self.CONFIG['LOGGING']['LOG_LEVEL']
        self.log_identifier = self.CONFIG['LOGGING']['LOG_IDENTIFIER']

        self.file_manager_path = self.CONFIG['FILE_CONTENT_MANAGER']['DIR_PATH']
        self.file_manager_filename = self.CONFIG['FILE_CONTENT_MANAGER']['FILE_NAME']
        self.file_manager_write_op = self.CONFIG['FILE_CONTENT_MANAGER']['FILE_WRITE_OP']
        self.file_manager_read_op = self.CONFIG['FILE_CONTENT_MANAGER']['FILE_READ_OP']

        self.n_people = int(self.CONFIG['PARAMETERS']['N_PEOPLE'])

    def __print_environment_values(self):
        print(f'> App version: \'{self.app_version}\'')
        print(f'> Sample data dir path: \'{self.sample_data_path}\'')
        print(f'> App debug: \'{self.app_debug}\'')
        print("")
        print(f'> Logger dir path: \'{self.log_path}\'')
        print(f'> Logger level: \'{self.log_level}\'')
        print(f'> Logger identifier: \'{self.log_identifier}\'')
        print("")
        print(f'> File manager dir path: \'{self.file_manager_path}\'')
        print(f'> File manager file path: \'{self.file_manager_filename}\'')
        print(f'> File manager operation: \'{self.file_manager_operation}\'')