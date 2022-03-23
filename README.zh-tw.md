[English](https://github.com/seriaati/hoyolab-resin-counter/blob/main/README.md) | 中文
# hoyolab-resin-counter
![hoyolab-resin-counter (Small)](https://user-images.githubusercontent.com/61446626/159615993-8801f175-84b7-4361-bf65-7fb70708341a.png)

Hoyolab的實時便籤功能，但在電腦上實現。

## 功能
- 顯示帳號裡目前剩餘的樹脂數量
- 顯示距離樹脂填滿還有多少時間
- 顯示塵歌壺的錢幣數量
- 顯示已派遣的探索數量
- 迅速且方便的資料查詢（在帳號設置完成之後

## 設置hoyolab-resin-counter
- 至 https://www.python.org/downloads 下載並安裝python（記得勾選「Add python to PATH」）
- 如果有跳出提示，請點擊「Disable PATH legnth limit」
- 下載最新版本的hoyolab-resin-counter.py
- 將檔案放到任意一個資料夾

### 新增你的帳號
- 到 https://www.hoyolab.com 並登入你的帳號
- 按F12或是透過ctrl+shift+I的快捷鍵來開啟開發者工具的界面
- 在開發者工具中 -> 應用程式 -> Cookies -> https://www.hoyolab.com/home
- 找到並複製 ltuid 與 ltoken
- 右鍵hoyolab-resin-counter.py -> 「Edit with IDLE」
- 將剛剛複製的 ltuid, ltoken 以及你的遊戲 uid 放上

## 運行hoyolab-resin-counter
- 使用 Win+R 快捷鍵並輸入「cmd」來打開命令視窗
- 透過 ```cd``` 指令來進入 hoyolab-resin-counter.py 所在的資料夾
- 例如：
```cd C:\Users\seria\Documents```
- Then run the tool by typing ```python hoylab-resin-counter.py```
- 接著使用 ```python hoyolab-resin-counter.py``` 指令來執行hoyolab-resin-counter
- 下面是你在運行指令後應該在命令視窗應該見到的畫面：  
![image](https://user-images.githubusercontent.com/61446626/159394012-b59892f1-1620-44c1-99b3-87a43223dae8.png)
- 資料依序是：uid, 樹脂數量, 最大樹脂剩餘時間, 塵歌壺幣數量, 已派遣的探索數量
- hoyolab-resin-counter並不會自動更新這些數據，如果你想再確認一遍，按方向鍵的「上」或是再輸入一次 ```python hoylab-resin-counter.py``` 的指令
- 如果你不想重複進行導入資料夾的步驟，保持開啟命令視窗

## 其他事項
- 使用者資料是由 https://github.com/thesadru/genshinstats 導入
### 這有什麼用處？
- 目前，hoyolab的實時便籤功能只有在手機app才有，而且需要按好多個按鍵才能查看，不是非常迅速且便利
- 同時，我都是用我的筆電來玩原神的，所以我很常忘記用手機查看樹脂，導致160/160頻頻出現
- 我找不到能實現這樣功能的工具，所以我就自己做了一個
