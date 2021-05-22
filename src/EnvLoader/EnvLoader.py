import configparser
import platform
import logging
import sys


import sys, logging, platform, configparser

class EnvLoader:
    DIR_SEP = None
    ENV_TYPE = None
    CONFIG = None

    app_version = None
    log_path = None
    log_level = None
    log_identifier = None

    input_file = None
    data_dir_path = None

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
            config_file_path = self._get_path_to_config_file("config", "default")
            self._read_config_file(config_file_path)

            self._set_environment_config_values()
            print(f'> App version: \'{self.app_version}\'')
            print(f'> Config file path \'{config_file_path}\'')
            print(f'> Data dir path \'{self.data_dir_path}\'')
            print(f'> Logger dir path \'{self.log_path}\'')


        except Exception as err:
            print(f'\n Load env function Error ({err})')
            sys.exit(-1)


    def _set_dir_separator_type(self):
        """Define separator type based on machine type
        """
        PLATFORM = platform.system().lower()

        if PLATFORM == "linux" or PLATFORM == "linux2":
            print(f'> Running platform \'{PLATFORM}\' system')
            self.DIR_SEP = "/"
        elif PLATFORM == "darwin":
            print(f'> Running platform \'{PLATFORM}\'  macoos system')
            self.DIR_SEP = "/"
        elif PLATFORM == "win32" or PLATFORM == "win64":
            print(f'> Running platform \'{PLATFORM}\' system')
            self.DIR_SEP = "\\"
        else:
            print(f'> Running platform \'{PLATFORM}\' system is not supported for this ETL')
            sys.exit(-1)


    def _get_path_to_config_file(self, dir_name, file_name):
        path_dir_env = self._build_dir_path_by_name(dir_name)
        return path_dir_env + file_name + "-" + self.ENV_TYPE + ".ini"

    def _build_dir_path_by_name(self, dir_name):
        config_root_dir = "." + self.DIR_SEP + dir_name + self.DIR_SEP
        return config_root_dir


    def _read_config_file(self, config_file_path):
        self.CONFIG = configparser.ConfigParser()
        self.CONFIG.sections()
        self.CONFIG.read(config_file_path)


    def _set_environment_config_values(self):
        self.app_version = self.CONFIG['APP_INFO']['APP_VERSION']

        self.data_dir_path = self._build_dir_path_by_name(self.CONFIG['APP_INFO']['SAMPLE_DATA_DIR_PATH'])

        self.log_path = self.CONFIG['LOGGING']['LOG_PATH']
        self.log_level = self.CONFIG['LOGGING']['LOG_LEVEL']
        self.log_identifier = self.CONFIG['LOGGING']['LOG_IDENTIFIER']
