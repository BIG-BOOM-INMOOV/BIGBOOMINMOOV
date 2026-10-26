import customtkinter as ctk
import cv2
import cvzone
from ultralytics import YOLO
from PIL import Image
import math

class HeadLookAtView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.horizontal_mtr = self.controller.horizontal_mtr
        self.vertical_mtr = self.controller.vertical_mtr

        self.horizontal_angle = 90
        self.vertical_angle = 90

        self.horizontal_mtr.write(self.horizontal_angle)
        self.vertical_mtr.write(self.vertical_angle)

        self.cap = cv2.VideoCapture(0)

        self.model = YOLO("../models/yolov8n.pt")

    def thing_recognition(self):
        success, frame = self.cap.read()
        if success:
            results = self.model(frame, stream=True, verbose=False)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    self.middle_x = (x2 + x1) / 2
                    self.middle_y = (y2 + y1) / 2

                    w, h = x2 - x1, y2 - y1
                    cvzone.cornerRect(frame, (x1, y1, w, h))

                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])

                    cvzone.putTextRect(frame, f'{self.model.names[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(640, 480))

            self.video_label.configure(image=ctk_image)
            self.video_label.image = ctk_image
        else:
            print("Failed to grab frame")