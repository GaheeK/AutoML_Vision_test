import sys
import os
import cv2
from google.cloud import automl_v1beta1
import json
from google.protobuf.json_format import MessageToDict


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "" #GCPサービスアカウントのjsonパス
project_id = ""  #GCPプロジェクトID
model_id = "" #使用するAutoMLVisionモデルのID. Automl vision コンソル上で確認可能


cascadepath="../opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml" #顔の分類器のパスを入力
font=cv2.FONT_HERSHEY_SIMPLEX
rectangle_bgr=(0, 0, 0)

def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {'score_threshold': '0.4'}  #推論のthresholdを指定
  request = prediction_client.predict(name, payload, params)
  print(request)
  return request

if __name__ == '__main__':
  file_path = sys.argv[1]

  face_cascade = cv2.CascadeClassifier(cascadepath)

  img = cv2.imread(file_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = face_cascade.detectMultiScale(gray)
  face_count=0

  result_rec = []
  result_name = []

  if len(face)>0:
    for rect in face:
      name = './tmp/'+str(face_count)+'.jpg'
      cv2.imwrite(name, img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
      face_count += 1
      with open(name, 'rb') as ff:
        content=ff.read()
      payloads = get_prediction(content, project_id, model_id)
      response = MessageToDict(payloads, preserving_proto_field_name = True)
      if response != {}:
        name = response['payload'][0]['display_name']
      else:
        name = ''

      result_rec.append(rect)
      result_name.append(name)

  results = zip(result_rec, result_name)
  i = 0
  for a in results:
      (text_width, text_height) = cv2.getTextSize(a[1], font, fontScale=1, thickness=1)[0]
      cv2.rectangle(img, (a[0][0],a[0][1]), (a[0][0]+a[0][2], a[0][1]+a[0][3]), (255, 0,0),2)
      if i%2 == 0:
        cv2.rectangle(img, (a[0][0]-10, a[0][1]-text_height), (a[0][0]+text_width, a[0][1]+10), rectangle_bgr, cv2.FILLED)
        cv2.putText(img, a[1], (a[0][0],a[0][1]), font, 1.0, (255, 0, 255), thickness=2)
      else:
        cv2.rectangle(img, (a[0][0]-10, a[0][1]+a[0][3]), (a[0][0]+text_width, a[0][1]+a[0][3]+text_height+10), rectangle_bgr, cv2.FILLED)
        cv2.putText(img, a[1], (a[0][0],a[0][1]+a[0][3]+text_height), font, 1.0, (255, 0, 255), thickness=2)
      i += 1
  cv2.imwrite('./tmp/final.jpg', img)
