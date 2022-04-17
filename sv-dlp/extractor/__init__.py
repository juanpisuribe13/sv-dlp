import extractor.bing
import extractor.google
import extractor.yandex
# i don't know why i picked this. i literally can't call extractor.[service]
# unless if i import them here, and __all__ causes pyinstaller to act very weirdly. too bad!

class ServiceNotSupported(Exception):
    message = "Service does not support this function"
    pass

class ServiceNotFound(Exception):
    message = "Service not found"
    pass

class ServiceShortURLFound(Exception):
    message = "Short URL used. Avoid using them as they don't work with this service"
    pass