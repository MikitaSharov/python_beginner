# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня WARNING и выше — в warnings_errors.log.

import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


class DebugInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO


class WarningsErrorsFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING


debug_and_info_handler = logging.FileHandler('debug_info.log')
debug_and_info_handler.setLevel(logging.DEBUG)
debug_and_info_handler.setFormatter(formatter)
debug_and_info_handler.addFilter(DebugInfoFilter())

warnings_and_err = logging.FileHandler('warnings_errors.log')
warnings_and_err.setLevel(logging.WARNING)
warnings_and_err.setFormatter(formatter)
warnings_and_err.addFilter(WarningsErrorsFilter())

logger.addHandler(debug_and_info_handler)
logger.addHandler(warnings_and_err)

logger.debug('debag')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
