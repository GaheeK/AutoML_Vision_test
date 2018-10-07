import cv2
import os

#分類器の指定
cascadepath="../opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml"

def make_directory():
  list_dirs = os.listdir()
  list_only_dirs = []
  for list_dir in list_dirs:
    if os.path.isdir(os.path.join(os.getcwd(), list_dir)):
      list_only_dirs.append(list_dir)
    else:
      continue
  for name in list_only_dirs:
      os.makedirs('../face_cut/'+name, exist_ok=True)
      os.makedirs('../face_no_cut/'+name, exist_ok=True)
  return list_only_dirs



if __name__ == "__main__":
  only_dirs= make_directory()

  face_cascade = cv2.CascadeClassifier(cascadepath)
  recur_dir = os.walk(os.getcwd())
  for root, dirs, files in recur_dir:
    face_count = 0
    root_dir = root.split('/')[-1]
    print(root_dir)
    if root_dir not in only_dirs:
      continue
    for file in files:
      if file == (".DS_Store" or 'face.py'):
        continue
      img_path = root + '/' + file
      print(img_path)
      img = cv2.imread(img_path)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      #(x, y, w, h)なので, cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2). 複数の場合はlist で複数戻ってくる
      face = face_cascade.detectMultiScale(gray)

      if len(face)>0:
        for rect in face:
          face_count += 1
          cv2.imwrite('../face_cut/'+ root_dir + '/' + str(face_count) + file, \
                  img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])

      else:
        print(file + ' : No Face founded')
        cv2.imwrite('../face_no_cut/'+ root_dir + '/' + file, img)


