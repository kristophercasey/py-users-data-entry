from src.PersonManager.PersonManager import PersonManager

INSERT_DATA_OPT = 1
EXIT_OPT = 0

def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info("App orchestrator arguments {0} \n".format(config))

        personManager = PersonManager(config = config, logger = logger)

    except Exception as err:
        logger.log_traceback(err)
