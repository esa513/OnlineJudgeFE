# OnlineJudge Front End
[![vue](https://img.shields.io/badge/vue-2.5.13-blue.svg?style=flat-square)](https://github.com/vuejs/vue)
[![vuex](https://img.shields.io/badge/vuex-3.0.1-blue.svg?style=flat-square)](https://vuex.vuejs.org/)
[![echarts](https://img.shields.io/badge/echarts-3.8.3-blue.svg?style=flat-square)](https://github.com/ecomfe/echarts)
[![iview](https://img.shields.io/badge/iview-2.8.0-blue.svg?style=flat-square)](https://github.com/iview/iview)
[![element-ui](https://img.shields.io/badge/element-2.0.9-blue.svg?style=flat-square)](https://github.com/ElemeFE/element)
[![Build Status](https://travis-ci.org/QingdaoU/OnlineJudgeFE.svg?branch=master)](https://travis-ci.org/QingdaoU/OnlineJudgeFE)

>### A multiple pages app built for OnlineJudge. [Demo](https://qduoj.com)

## Features

+ Webpack3 multiple pages with bundle size optimization
+ Easy use simditor & Nice codemirror editor
+ Amazing charting and visualization(echarts)
+ User-friendly operation
+ Quite beautiful：)

## Get Started

Install nodejs **v8.12.0** first.

### Linux

```bash
npm install
# we use webpack DllReference to decrease the build time,
# this command only needs execute once unless you upgrade the package in build/webpack.dll.conf.js
export NODE_ENV=development
npm run build:dll

# the dev-server will set proxy table to your backend
export TARGET=http://Your-backend

# serve with hot reload at localhost:8080
npm run dev
```
### Windows-CMD

```bash
npm install
# we use webpack DllReference to decrease the build time,
# this command only needs execute once unless you upgrade the package in build/webpack.dll.conf.js
set NODE_ENV=development
npm run build:dll

# the dev-server will set proxy table to your backend
set TARGET=http://Your-backend

# serve with hot reload at localhost:8080
npm run dev
```
### Windows-PowerShell

```bash
npm install
# we use webpack DllReference to decrease the build time,
# this command only needs execute once unless you upgrade the package in build/webpack.dll.conf.js
$env:NODE_ENV="development"
npm run build:dll

# the dev-server will set proxy table to your backend
$env:TARGET="http://Your-backend"

# serve with hot reload at localhost:8080
npm run dev
```

## Screenshots

[Check here.](https://github.com/QingdaoU/OnlineJudge)

## Browser Support

Modern browsers and Internet Explorer 10+.

## LICENSE

[MIT](https://opensource.org/licenses/MIT)


---


## 修改

- [X] Display ID 排序&每頁顯示筆數(預設100筆)
- [X] IO輸出輸入為(none)/(hidden)時，變換背景色
- [X] 前端預設語言改為繁中
- [X] 比賽submission Rejudge
- [X] 分享提交問題:比賽沒有；一般題目會出現問題>拔除按鈕
- [X] 學生查看提交預設為：我的>全部
- [X] 後台跳前台按鈕
- [X] 隱藏上網IP顯示頁面
- [X] 學生提交以後，更改題目測資，比賽功能無法rejudge，但一般題目可以
  * 從[這邊](https://github.com/QingdaoU/OnlineJudge/blob/master/submission/views/admin.py#L15)拿掉 `contest_id__isnull=True` 能解決api層面的問題
- [X] FILE IO 鏡像源更換([參考](https://github.com/QingdaoU/OnlineJudge/issues/309))
- [X] 比對程式碼>已寫python可以自動比對，並將相同程式碼複製到`Same`資料夾
- [ ] 待討論(要不要開後端網址)：如果有開後端網址的話，前端可以看api service的東西(`\src\pages\admin\api.js`)
- [ ] ~~IP問題: 要辨識不易~~

### 小問題
- [ ] 導入題目，題目難度和可用語言會有問題
- [ ] Simditor空格問題
- [ ] ~~導出題目的壓縮檔，依照Display ID排序(改不了，要到後端api改)~~
  * `OnlineJudgeFE\src\pages\admin\api.js#L295`

