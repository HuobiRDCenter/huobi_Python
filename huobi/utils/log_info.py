class LogLevel:
    DEBUG = "debug"
    INFO = "info"
    WARNINGS = "warning"
    ERROR = "error"
    FATAL = "fatal"


class LogInfo:
    @staticmethod
    def output(message, log_level=LogLevel.DEBUG):
        # if (message and len(message)):
        #     if log_level == LogLevel.DEBUG:
        #         logging.debug(message)
        #     elif log_level == LogLevel.INFO:
        #         logging.info(message)
        #     elif log_level == LogLevel.WARNINGS:
        #         logging.warnings(message)
        #     elif log_level == LogLevel.ERROR:
        #         logging.error(message)
        #     elif log_level == LogLevel.FATAL:
        #         logging.fatal(message)

        print(message)

    @staticmethod
    def output_list(data_list, log_level=LogLevel.DEBUG):
        if data_list and len(data_list):
            for obj in data_list:
                obj.print_object()
                print()
