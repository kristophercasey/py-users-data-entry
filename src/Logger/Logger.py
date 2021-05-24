import logging
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

    def init_logger(self):
        """Initialize logger with two handlers, one for wrinte and save logs on disk and other for print out beauty on console
        """
        try:
            # Defining log level
            logger = logging.getLogger(self.log_identifier)
            logger.setLevel(self.logging_level)

            # File handler on Disk
            dir_path = self.log_path.rstrip('/')
            current_date = datetime.date.today().strftime(self.file_date_format)
            file_handler = logging.FileHandler(f'{dir_path}/{current_date}__{self.log_identifier}.log', mode='w')

            file_handler.setLevel(self.logging_level)

            # Console Handler
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(self.logging_level)

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

        # First default log
        self.__first_default_log()

    def log_traceback(self, errMessage = "", logging_level = "ERROR"):
        """Customized log trackeback message

        Args:
            errMessage (str): Contains string error message
        """
        traceback_log_level = self._get_logging_level(logging_level)
        self.log.log(traceback_log_level, errMessage, exc_info=True)

    def __first_default_log(self):
        """Function that prints first log message example
        """
        try:
            self.log.info("*********** Start Logger Execution: default log *************")
            self.log.info("Type of file to be processed: %s")

        except Exception as err:
            self.log.log(logging.ERROR, f'\n first_default_log Error ({err})')
            sys.exit(-1)

    def _get_logging_level(self, logging_level):
        """Set logging level and print message explaining error type

        Args:
            logging_level (str): Logging type [DEBUG, INFO, WARNING, ERROR, CRITICAL]

        Returns:
            logging type: logging type from logging class
        """

        print(f'> Configured logging level ({logging_level}): \'{self.logger_level_err_desc[logging_level]}\'')
        if logging_level == "DEBUG": return logging.DEBUG
        elif logging_level == "INFO": return logging.INFO
        elif logging_level == "WARNING": return logging.WARNING
        elif logging_level == "ERROR": return logging.ERROR
        elif logging_level == "CRITICAL": return logging.CRITICAL
