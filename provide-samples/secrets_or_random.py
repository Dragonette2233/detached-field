import secrets
import string

class SecureData():

    def __init__(self):
        # self.length = 0
        self._password: str
        self._urlpass: str
        self._hexpass: str 
        self._symbols_for_generation = string.ascii_letters + string.digits + string.punctuation

    def set_password(self, length=16):
       
        self.__password = ''.join(secrets.choice(self._symbols_for_generation) for _ in range(length))

    def set_hexpass(self, length=32):

        self.__hexpass = secrets.token_hex(length)
        self.__urlpass = secrets.token_urlsafe(length)

    def get_codes(self):
        # print(self._password)
        return f'Your password is: {self.__password}\nYour hex_url code is: {self.__hexpass, self.__urlpass}' 
        

        
security = SecureData()
security.set_hexpass()
security.set_password(14)
print(security.get_codes())



