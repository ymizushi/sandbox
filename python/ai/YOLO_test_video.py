from ultralytics import YOLO
import cv2
import csv

csv_filename = 'sample1.csv'
# 出力するデータ
header = ['No','Class', 'Label','Scores','id','x1','y1','x2','y2']
# CSVファイルにデータを書き込む
file = open(csv_filename, mode='w', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(header)

model = YOLO("yolov8x.pt")

# Open the video file
video_path = "./sample/sample_1.mp4"
cap = cv2.VideoCapture(video_path)

frame_cnt = 0
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model.track(frame,persist=True,conf = 0.5,classes=[0,2,7])

        frame_cnt = frame_cnt + 1
        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        items = results[0]
        for item in items:
            cls = int(item.boxes.cls)    # cls, (N, 1)
            label = item.names[int(cls)]
            score = item.boxes.conf.cpu().numpy()[0]   # confidence score, (N, 1)
            x1,y1,x2,y2 = item.boxes.xyxy.cpu().numpy()[0]   # box with xyxy format, (N, 4)

            id_value = item.boxes.id
            if id_value is None:
                track_ids = ''
            else:
                track_ids = item.boxes.id.int().cpu().tolist()[0]

            csv_data = [str(frame_cnt),str(cls),str(label),str(score),str(track_ids),str(x1),str(y1),str(x2),str(y2)]
            writer.writerow(csv_data)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

 # ファイルを閉じる
file.close()   
 

