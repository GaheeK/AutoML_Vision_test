# AutoML_Vision_test

## 1. opencvで顔の切り取りを行うサンプル

### サンプルの使い方

まず、テストのために下記のディレクトリ構成を作ります.

-**test**　　　　<br>
---**origin**　<br>
-----face.py　　　*(1_sample_opencvから取得)* <br> 
-----**CAT1**　　　　*(配下に顔を切り取る画像)* <br>
-----**CAT2**　　　　*(配下に顔を切り取る画像)*<br>
-----**CAT3**　　　　*(配下に顔を切り取る画像)*<br>
---**opencv-master** *([ココ](https://github.com/opencv/opencv)でダウンロード)*

origin上でface.pyを実行. face_cut と face_no_catに顔切り取りした結果がカテゴリ別に保存される.
実行後の結果は以下になる

-**test**　　　　<br>
---**face_cut**  <br>
------**CAT1** *CAT1で顔切り取りに成功した者の結果画像* <br>
------**CAT2** *CAT2で顔切り取りに成功した者の結果画像* <br>
------**CAT3** *CAT3で顔切り取りに成功した者の結果画像* <br>
---**face_no_cut** <br>
------**CAT1**  *CAT1で顔切り取りに失敗した画像* <br>
------**CAT2**　　　　*CAT２で顔切り取りに失敗した画像* <br>
------**CAT3**　　 *CAT3で顔切り取りに失敗した画像* <br>
---**origin**　 *変更なし* <br>
---**opencv-master** *変更なし* <br>


## 2. 作成済みのautoML Visionを使った顔認識サンプル

### サンプルの使い方

このサンプルでは、人物の画像を与えた時に、opencvで顔を切り取り、autoMLを利用して顔認識をし元の画像に結果を表示するサンプルです.
先ほどのディレクトリの例で説明します.

-**test**　　　　<br>
---**origin**　<br>
---**opencv-master** *([ココ](https://github.com/opencv/opencv)でダウンロード)* <br>
---**predict** <br>
------predict.py *(2_sample_automlから取得)* <br>
------test.jpg *テストする画像* <br>
------**tmp** *空のフォルダー*

2_sample_automlからサンプルを取得し、GCPプロジェクト名などの必要情報を埋めて後、predict上で<br>
`python predict.py test.jpg`を実行すると、test.jpgに対して顔認識を行い表示した結果をtmpフォルダー内に保存する.
