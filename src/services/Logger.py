import logging

class Logger:
    logging_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def __init__(self, log_level):
        self.logger = logging.getLogger(self.__class__.__name__)
        if log_level not in self.logging_levels:
            log_level = "INFO"
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, additional_message):
        self.logger.info(additional_message)

    def log_warning(self, additional_message):
        self.logger.warning(additional_message)

    def log_error(self, additional_message):
        self.logger.error(additional_message)

    def log_critical(self, additional_message):
        self.logger.critical(additional_message)

    def log_debug(self, additional_message):
        self.logger.debug(additional_message)
