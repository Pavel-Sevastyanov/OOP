from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        codes =  {
            'CONTINUE': 'информация', 
            'OK': 'успех', 'USE_PROXY': 
            'перенаправление', 'NOT_FOUND': 
            'ошибка клиента', 'BAD_GATEWAY': 
            'ошибка сервера'
            }
        return codes[self.name]