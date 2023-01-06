import cv2

class VideoCamera(object):
    def __init__(self, source=0):
        self.camera = cv2.VideoCapture(source)
    
    def __del__(self):
        try:
            self.camera.stop()
            self.camera.stream.release()
        except:
            print("NO capture object!")
        cv2.destroyAllWindows()
    
    def get_frame(self):
        success, frame = self.camera.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()