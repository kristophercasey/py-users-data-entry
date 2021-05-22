
def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
    except Exception as err:
        logger.log_traceback(err)
