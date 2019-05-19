# CameraCalibration
## モチベーション
* iphoneカメラ用の補正ファイルを作っておきたい
* OpenCVのカメラキャリブレーションをやってみたい

## 参考サイト
* [OpenCV日本語サイトのチュートリアル](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_calib3d/py_calibration/py_calibration.html#calibration)
* [pynoteさんの記事](http://pynote.hatenablog.com/entry/opencv-camera-calibration)
* [カニカニクラブライフさんの記事](http://russeng.hatenablog.jp/entry/2015/06/16/004704)

## day2 の結果
* 画像を追加したが、精度が上がらず
* 調べて見ると、点数の数の与え方が、行と列で逆だった
* これを修正したら、まともに変換できるようになったのを確認した
* ただし、カニカニさんのサンプルをそのまま動かすと、キャリブレーション結果の保存時に何故か？エラーが起きる
* OpenCVのサンプルコードを使うようにした

## day1 の結果
* キャリブレーションの誤差が大きい
  * 600以上。０に近いほどよい。エラーなので当然だが…。  
  * カニカニさんの用に、もっと角度を付けたデータが必要かも。
* それと、Python遅いな。Google Colab でやったほうが処理がはやいか？

