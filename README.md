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
------**CAT3** **CAT3で顔切り取りに成功した者の結果画像* <br>
---**face_no_cut** <br>
------**CAT1**  *CAT1で顔切り取りに失敗した画像* <br>
------**CAT2**　　　　*CAT２で顔切り取りに失敗した画像* <br>
------**CAT3**　　 *CAT3で顔切り取りに失敗した画像* <br>
---**origin**　 *変更なし* <br>
---**opencv-master** *変更なし* <br>
