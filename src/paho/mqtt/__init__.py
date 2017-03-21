__version__ = "1.2.1-fixes-kc1"

class MQTTException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
