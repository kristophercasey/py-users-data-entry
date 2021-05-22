from src.PersonManager.PersonManager import PersonManager
from src.Helpers.Helpers import HelperClass

INSERT_DATA_OPT = 1
EXIT_OPT = 0

def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info("App orchestrator arguments {0} \n".format(config))

        personManager = PersonManager(config = config, logger = logger)

        while True:
            personManager.print_menu()
            option = HelperClass.input_int(
                message = "Insert option: ",
                required_positive = True
            )

    except Exception as err:
        logger.log_traceback(err)
