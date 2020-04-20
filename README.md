# ORDERLY Python / Django Interview

Hi,

感謝您

這是根據您的回覆所訂製的問題，大約會花費 3- 5 小時的挑戰時間

若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請發個PR到此專案

### 挑戰一: Django CVB (folder: x_1)

> 請使用 startapp 在一個全新的 Django 專案中建立新的 app 。
>
> 於 Django CVB 中繼承 View 並實作 get() (views.py)，並需有一個 url pattern (urls.py) 可進入此頁面，當使用 GET 進入時，會偵測特定目錄 (自行定義) 下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過。
>
> 賦予此 CVB 一個 create_csv()，並需有一個 url pattern, 當進入 (GET) 此頁面時，會隨機寫入 500 筆客戶資料至 customers.csv (csv 請放在 ilovecoffee 資料夾裡)，csv 結構如下:

```
customer_id,customer_name, customer_mobile, frequency
"y88xTa", "tom.y88xTa","+886938766119", "4"
"uYt49x", "peter.uYt49x","+886938922440", "6"
"p9g5As", "hank.p9g5As","+886918300227", "1"
````

##### customer_id:
長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字

##### customer_name: 
隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....]
將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"

##### customer_mobile
隨機產生一個+886開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生

##### frequency
從 [0-20] 中隨機選取

>
> 最後，賦予此 CVB 一個 calculate_csv() 並需有一個 url pattern，當進入此頁面時 (GET) 回傳 JsonResponse，其內容為 frequency 的中數、眾數及平均數 (取至小數點後 5 位)
>



### 挑戰二: Django 排程 (folder: x_2)
> 請使用 startapp 在一個全新的 Django 專案中建立新的 app 。
> 
> 在 tasks.py 中撰寫一支爬蟲，透過 Django Q ，讓這隻爬蟲會在每天凌晨四點被啟動，並爬取 https://tw.yahoo.com/ 首頁，統計”台灣”二字出現的字數，將爬取日期時間與字數存於 SQLite 中。
> 
> 撰寫一個 CVB get()，當被 GET 時，會主動呼此此爬蟲進行動作。


### 挑戰三: Project 開發分配 (folder: x_3)
> ORDERLY 是一款企業商用軟體，該產品已上線二年，具有一定規模的客戶量體，但功能仍然簡單，因此如何分配開發資源就顯得非常重要。
> 
> 假設現在是星期三早上 10 點鐘，請您針對以下狀況進行思考，除說明每項的應對方式外，並於最後排序您的工作優先次序 (eg: DCABFE):
```
(A) 重量級客戶一個月前提出的改進需求，此需求你評估認為非常實用，但需耗時 2 天完成。
(B) 昨天晚上 11 點，客戶寄信來回報的操作錯誤，內容為:"我按了這個按鍵，但它完全沒反應"。
(C) 早上 9 點系統發出的 alert, 警示訊息為 DB 異常。
(D) 剛剛你無意中注意到的前台破圖，大約 20 分鐘可搞定。
(E) 近 3 天專注開發的一項功能，如果現在不接著工作，很可能會忘記重要事項。
(F) 昨天無意中發現的程式 bug，但不在自已掌管範圍內。
````


## 當您挑戰結束時，請在您的最後一次 commit 中輸入您對此份工作的期待，謝謝您。

