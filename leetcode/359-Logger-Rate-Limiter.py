class Logger(object):

    def __init__(self):
        self._d = {}

    def shouldPrintMessage(self, timestamp, message):

        if message in self._d and timestamp - self._d[message] < 10:
            return False
        else:
            self._d[message] = timestamp
            return True

