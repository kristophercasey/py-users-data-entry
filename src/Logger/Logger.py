import logging, traceback
import datetime
import sys

class LoggerClass:
    file_date_format = '%Y%m%d'
    print_date_format = '%Y-%m-%d %H:%M:%S'
    logger_level_err_desc = {
        "DEBUG": "Detailed information, typically of interest only when diagnosing problems.",
        "INFO": "Confirmation that things are working as expected.",
        "WARNING": "An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'. The software is still working as expected",
        "ERROR": "Due to a more serious problem, the software has not been able to perform some function",
        "CRITICAL": "A serious error, indicating that the program itself may be unable to continue running"
    }

    def __init__(self, log_path, logging_level, log_identifier):
        """Accept required parameters for logger instantiation

        Args:
            log_path (str): logger storage directory
            logging_level (str): type of error
            log_identifier (str): universal unique identifier
        """
        self.log_path = log_path
        self.logging_level = self._get_logging_level(logging_level)
        self.log_identifier = log_identifier
        self.log = None

    def _get_logging_level(self, logging_level):
        """Set logging level and print message explaining error type

        Args:
            logging_level (str): Logging type [DEBUG, INFO, WARNING, ERROR, CRITICAL]

        Returns:
            logging type: logging type from logging class
        """

        print(f'> Logging level: \'{self.logger_level_err_desc[logging_level]}\'')
        if logging_level == "DEBUG": return logging.DEBUG
        elif logging_level == "INFO": return logging.INFO
        elif logging_level == "WARNING": return logging.WARNING
        elif logging_level == "ERROR": return logging.ERROR
        elif logging_level == "CRITICAL": return logging.CRITICAL


    def init_logger(self):
        """Initialize logger with two handlers, one for wrinte and save logs on disk and other for print out beauty on console
        """
        try:
            # Defining log level
            logger = logging.getLogger(self.log_identifier)
            logger.setLevel(self.logging_level)

            # File handler on Disk
            file_handler = logging.FileHandler(self.log_path +
                                               datetime.date.today().strftime(self.file_date_format) +
                                               '_' + self.log_identifier +
                                               '.log', mode='w')

            file_handler.setLevel(self.logging_level)

            # Console Handler
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(self.logging_level)

            # Create formatter and addit to the handlers
            # formatter_0 = logging.Formatter('[%(asctime)s] || %(levelname)s || \
            #                                 (%(filename)s:%(lineno)s || \
            #                                 %(message)s', datefmt=self.print_date_format)
            # formatter_1 = logging.Formatter('%(levelname)s [%(asctime)s] \n ├── %(filename)s:%(lineno)s \n └── %(message)s', datefmt=self.print_date_format)
            formatter_2 = logging.Formatter('(%(levelname)s) [%(asctime)s] %(filename)s:%(lineno)s \n %(message)s \n', datefmt=self.print_date_format)
            file_handler.setFormatter(formatter_2)
            console_handler.setFormatter(formatter_2)

            # Add the handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            self.log = logger

        except Exception as err:
            self.log.log(logging.ERROR, f'\n Init Logger Error ({err})')
            sys.exit(-1)

    def first_default_log(self):
        """Function that prints first log message example
        """
        try:
            self.log.info("*********** Start Logger Execution: default log ************* \n")
            self.log.info("Type of file to be processed: %s")

        except Exception as err:
            self.log.log(logging.ERROR, f'\n first_default_log Error ({err})')
            sys.exit(-1)

    def log_traceback(self, errMessage = "", logging_level = "ERROR"):
        """Customized log trackeback message

        Args:
            errMessage (str): Contains string error message
        """
        traceback_log_level = self._get_logging_level(logging_level)
        # # Extract error traceback info
        # formatted_lines = traceback.format_exc().splitlines()
        # # Clean traceback lines from empty spaces
        # formatted_lines = [line.strip() for line in formatted_lines]

        # MOST_RECENT_CALL_FILE = 1
        # # Split each error line into small parts (file, line, element) to create custom message format
        # LAST_CALL_FILE = 3
        # most_recent_call_parts = formatted_lines[MOST_RECENT_CALL_FILE].split(",")
        # last_call_parts = formatted_lines[LAST_CALL_FILE].split(",")

        # # Define custom traceback message format
        # FILE = 0
        # LINE = 1
        # ELEMENT = 2
        # LAST_CALL_FN =  4
        # MOST_RECENT_CALL_FN = 2

        # last_call_location = ""
        # most_recent_call_location = ""


        # if len(formatted_lines) <= 4:
        #     most_recent_call_file = most_recent_call_parts[FILE][:-1]
        #     most_recent_call_line = most_recent_call_parts[LINE][6:]
        #     most_recent_call_ele = most_recent_call_parts[ELEMENT]
        #     most_recent_call_location = f'{most_recent_call_file}:{most_recent_call_line}\" {most_recent_call_ele}'

        # if len(formatted_lines) > 4:
        #     last_call_file = last_call_parts[FILE][:-1]
        #     last_call_line = last_call_parts[LINE][6:]
        #     last_call_ele = last_call_parts[ELEMENT]
        #     last_call_location = f'{last_call_file}:{last_call_line}\" {last_call_ele}'


        # most_recent_call_fn = formatted_lines[MOST_RECENT_CALL_FN]
        # last_call_fn = formatted_lines[LAST_CALL_FN]

        # # Make custom message format looks beauty
        # traceback_message = "" + \
        # f'{errMessage} \n' + \
        # f' ├── {most_recent_call_fn} \n' \
        # f' │   └── {most_recent_call_location} \n' \
        # f' └── {last_call_fn} \n' \
        # f'     └── {last_call_location} \n'

        # Print message based on type passed
        self.log.log(traceback_log_level, errMessage, exc_info=True)
