import time


class myTime:
    zero = -1
    
    def setZero(self):
        self.zero = time.time()
    
    def getZeroTimeStamp(self):
        return self.zero

    def getDelta(self):
        return round(time.time()-self.zero, 3)
    
    def __init__(self):
        self.setZero()
        
    def __str__(self):
        return ("zero: {}; curretnrDelta: {}".format(self.zero, self.getDelta()))