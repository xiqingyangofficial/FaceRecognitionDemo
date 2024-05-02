import face_recognition
import cv2
import os
import numpy as np

# 读取已经采集的姓名人脸
dataset_path = './dataset/'
known_image_paths = [os.path.join(dataset_path, file_name) for file_name in os.listdir(dataset_path)]
known_images = [face_recognition.load_image_file(s_known_image_path) for s_known_image_path in known_image_paths]
rgb_known_images = [cv2.cvtColor(known_image, cv2.COLOR_BGR2RGB)for known_image in known_images]
known_images_features = [face_recognition.face_encodings(sin_img, model='large')[0] for sin_img in rgb_known_images]
known_names = [str(os.path.split(s_image_path)[1].split('_')[1].split('.')[0]) for s_image_path in known_image_paths]
known_ids = [int(os.path.split(s_image_path)[1].split('_')[0]) for s_image_path in known_image_paths]

# 摄像头设备
webcam = cv2.VideoCapture(0)

# 采集新人脸数据并遍历比较实现识别
new_face_names = list()
new_face_locations = list()
new_face_features = list()
flag = True
while True:
    ret, new_face_image = webcam.read()

    if flag:
        faster_new_face_image = cv2.resize(new_face_image, (0, 0), fx=0.5, fy=0.5)
        new_face_locations = face_recognition.face_locations(faster_new_face_image)
        new_face_features = face_recognition.face_encodings(faster_new_face_image, new_face_locations)
        for (top, right, bottom, left), face_feature in zip(new_face_locations, new_face_features):
            match_faces = face_recognition.compare_faces(known_images_features, face_feature)
            name = "Stranger"
            face_distances = face_recognition.face_distance(known_images_features, face_feature)
            best_match_face_index = np.argmin(face_distances)
            if match_faces[best_match_face_index]:
                name = known_names[best_match_face_index]
            new_face_names.append(name)
    flag = not flag
    for (top, right, bottom, left), name in zip(new_face_locations, new_face_names):
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        cv2.rectangle(new_face_image, (left, top), (right, bottom), color=(183, 104, 0), thickness=5)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(new_face_image, 'User: ' + name, (left + 6, bottom - 6), cv2.FONT_ITALIC, 0.75,
                    (255, 0, 0), 2)

    cv2.imshow("System Working (Press Q to quit)", new_face_image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        exit()






