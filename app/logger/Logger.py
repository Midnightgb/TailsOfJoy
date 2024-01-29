class Logger:
    COLORS = {
        'RESET': '\033[0m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m'
    }

    @staticmethod
    def error(text):
        print(Logger.COLORS['RED'] + text + Logger.COLORS['RESET'])

    @staticmethod
    def success(text):
        print(Logger.COLORS['GREEN'] + text + Logger.COLORS['RESET'])

    @staticmethod
    def warning(text):
        print(Logger.COLORS['YELLOW'] + text + Logger.COLORS['RESET'])

    @staticmethod
    def info(text):
        print(Logger.COLORS['BLUE'] + text + Logger.COLORS['RESET'])

    @staticmethod
    def debug(text):
        print(Logger.COLORS['MAGENTA'] + text + Logger.COLORS['RESET'])
