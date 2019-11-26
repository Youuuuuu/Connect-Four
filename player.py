class Player:
    def __init__(self,sign):
        '''
        sign=a character: O or X
        '''
        self.__sign=sign

    def get_sign(self):
        return self.__sign

    sign = property(get_sign, None, None, None)
        
    
