# PythonLearning

### 概要
* 学習期間: 2022年4月~5月 
* 使用技術: Python,Django

typeScriptの自学習用リポジトリ。"TS-プロジェクト名"でリポジトリを分けて、分野毎の学習しました。
* Vue.js + typeScript の学習状況に関しては[こちら](https://github.com/worldwideweb13/typeScript/blob/main/ts-vue-grammer/README.md)を参照

---

### typeScript核学習ファイルの確認事項


* TS-libs　TS-DemoApp ではwebpackを利用しています。これらのフォルダでは、webpackをインストールしてアプリケーションの実行環境を作っています。`npm install --save @types/google.maps`

* [TS-libs](TS-libs) プロジェクトの実行環境    ※これらのサードパーティライブラリーをインストールした際は、`npm start`でサーバー再起動をかけることで変更が適用されます 
  * [lodash](https://lodash.com/) のインストール　※webpackで利用するため `npm i --save lodash`
  * [@types/lodash](https://www.npmjs.com/package/@types/lodash/) のインストール `npm install --save-dev @types/lodash`
  * [class-transfer](https://www.npmjs.com/package/class-transformer#installation) のインストール
    * `npm install class-transformer --save`
    * `npm install reflect-metadata --save`
  * [class-validator](https://www.npmjs.com/package/class-validator) のインストール `npm install class-validator --save`

* [TS-mapApp](typeScript/TS-mapApp)...キーワード検索でGoogleMapを表示します。GoogleMapAPI,typeScriptで作成しました。
  * 動作をさせる際は、axiosをインストールします。　`npm install --save axios`
  * 型定義`type GoogleGeocrdingResponse = {...}`は、[GoogleMapAPI公式のレスポンス定義](https://developers.google.com/maps/documentation/geocoding/requests-geocoding)を参考に作成
  * [GoogleMapの@types](https://www.npmjs.com/package/@types/google.maps) を使うことでts環境でgooglemap関数の型補完を使えるようになります。

---
### Django のMVC　モデル

<p align="center">
  <img src="https://user-images.githubusercontent.com/75665390/179008552-41f81a9d-ee84-4fd0-9e7a-1e92e5afee6a.png" />
</p>

