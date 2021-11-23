import cv2
import time
import json
class Camare:
    def __init__(self):
        userinfo = self.getInfo()
        self.ID = userinfo["ID"]
        self.interval = userinfo["interval"]
        Resolution = userinfo["Resolution"]
        self.size_x = Resolution[0]
        self.size_y = Resolution[1]
        self.amount = userinfo["amount"]
        
        print(f'Camare init')
    
    def getInfo(self):
        f = open("photoInfo.json")
        lines = f.read()
        infodict = json.loads(s = lines)
        #print(infodict)
        f.close()
        return infodict

    def shot(self):
        print(f'begin shot')
        frame = cv2.VideoCapture(0)
        for i in range(self.amount):
            time.sleep(self.interval)
            ret, imgTemp = frame.read()
            img = cv2.resize(imgTemp,(self.size_x,self.size_y))
            if (frame):
                cv2.imwrite(f'./images{self.ID}{i}.jpg',img)


        frame.release()
        cv2.destroyAllWindows()


