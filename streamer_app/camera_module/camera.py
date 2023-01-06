import cv2
import json
import os
import numpy as np

from ..object_detector.yolo_classifier import Yolov5Model
from ..settings import BASE_PATH


config_filename = os.path.join(BASE_PATH, 'configs/yolo_config.json')


def read_config(config_filename):
    f = open(config_filename)
    config = json.load(f)
    return config

class VideoCamera(object):
    def __init__(self, source=0):
        self.camera = cv2.VideoCapture(source)
        self.set_classifier_model()
    
    def __del__(self):
        try:
            self.camera.stop()
            self.camera.stream.release()
        except:
            print("NO capture object!")
        cv2.destroyAllWindows()
    
    def set_classifier_model(self, config_filename=config_filename):
        config = read_config(config_filename)
        self.model = Yolov5Model(config=config['model_classification'])
    
    def get_frame(self):
        success, frame = self.camera.read()
        if success:
            predictions = self.model.predict_result(frame)
            for obj in predictions:
                x1 = int(obj["x1"])
                y1 = int(obj["y1"])
                x2 = int(obj["x2"])
                y2 = int(obj["y2"])
                label = obj["label"]
                confidence = obj["confidence"]
                text = f"{label.upper()} : {confidence} %"

                color_val = min(255, obj["label_int"]*3)
                box_color = (255, color_val, color_val)

                cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, (1))
                cv2.putText(frame, text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, box_color, 1)
            frame = np.fliplr(frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
