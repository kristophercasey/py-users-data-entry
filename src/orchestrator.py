from src.PersonManager.PersonManager import PersonManager
from src.Helpers.Helpers import HelperClass

INSERT_DATA_OPT = 1
EXIT_OPT = 0

def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info(f'App orchestrator arguments \'{config}\'')

        personManager = PersonManager(config = config, logger = logger)

        result = None
        while True:
            result = personManager.start()
            if not result == None:
                print(result)
            print("---------------------")

    except Exception as err:
        logger.log_traceback(err)
