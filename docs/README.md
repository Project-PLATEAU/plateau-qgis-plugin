# PLATEAUQGISプラグイン(plateau-qgis-plugin)


## 概要
本プラグイン(plateau-qgis-plugin)は、QGIS上で「3D都市モデル標準製品仕様書 第3.0版」に対応したPLATEAUのCityGMLファイルを読み込むためのツール（ベータ版）です。


## プラグイン概要
### 動作環境
本プラグインを実行するには、QGIS（バージョン 3.28）をインストールしている必要があります。QGISのインストールについては以下を参照ください。

* [QGISインストーラー](https://qgis.org/ja/site/forusers/download.html)

### 利用方法
本プラグインの導入から集計の実施までの手順は以下の通りです。
詳細な操作方法は本プラグインの[利用マニュアル](https://github.com/Project-PLATEAU/plateau-qgis-plugin/blob/main/docs/manual.md)を参照ください。
なお、本プラグインは、QGIS上のベクタレイヤに対応しています。

1.	GitHubからプラグインの[Zipファイル](https://github.com/Project-PLATEAU/plateau-qgis-plugin/releases/download/v0.02/plateau_plugin.zip)をダウンロード
2.	QGISを起動
3.	本プラグインをインストール
4.  本プラグインを起動
5.	読み込み対象とするCityGMLファイルを指定
6.	集計方法を指定
7.  必要であれば以下のオプションのチェックボックスをクリックする
    1.  地物を構成する部分ごとにレイヤーを分ける[オプション]
    2.  3次元データを強制的に2次元化する[オプション]
    3.  既存の同名レイヤに追記する[オプション]
    4.  変換先CRS[オプション]
8.	処理を実行

## ライセンス 
* ソースコードおよび関連ドキュメントの著作権は国土交通省に帰属します。
* 本ドキュメントは[Project PLATEAU](https://www.mlit.go.jp/plateau/site-policy/)のサイトポリシー（CCBY4.0および政府標準利用規約2.0）に従い提供されています。

## 注意事項 
* 本リポジトリは参考資料として提供しているものです。動作保証は行っておりません。
* 予告なく変更・削除する可能性があります。
* 本リポジトリの利用により生じた損失及び損害等について、国土交通省はいかなる責任も負わないものとします。