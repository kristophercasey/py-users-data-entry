from src.FileManager.FileManager import FileManager
from src.PersonManager.PersonManager import PersonManager

INSERT_DATA_OPT = 1
EXIT_OPT = 0

def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info(f'App orchestrator arguments \'{config}\'')

        data_file = FileManager(
            dir_path = config.file_manager_path,
            filename = config.file_manager_filename,
            write_op = config.file_manager_write_op,
            read_op = config.file_manager_read_op,
            logger = logger
        )


        personManager = PersonManager(config = config, logger = logger)

        result = None
        while True:
            result = personManager.start()
            if not result == None:
                data_file.write_file(f'{result}\n', 'a')
                print(result)
            print("---------------------")

    except Exception as err:
        logger.log_traceback(err)
