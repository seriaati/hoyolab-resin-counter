# hoyolab-resin-counter
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
- In the developer tools menu -> Application -> Cookies -> https://www.hoyolab.com/home
- 在開發者工具中 -> 
- Copy ltuid and ltoken
- Right click hoyolab-resin-counter.py and "Edit with IDLE" -> "Edit with IDLE"
- Paste your ltuid, ltoken, and putin your uid

## Running hoyolab-resin-counter
- Whenever you want to check your resin (or other things), open up a command prompt
- Head toward the directory where hoyolab-resin-counter.py is located using the ```cd``` command
- For example
```cd C:\Users\seria\Documents```
- Then run the tool by typing ```python hoylab-resin-counter.py```
- You should be able to see the results, an example of what you should see is shown below  
![image](https://user-images.githubusercontent.com/61446626/159394012-b59892f1-1620-44c1-99b3-87a43223dae8.png)
- This tool does not receive data in real-time, when you want to check again, press the upward arrow button on your keyboard to run the command again, or type ```python hoylab-resin-counter.py```
- If you don't want to do the directory thing all over again, just leave the command prompt opened

## Other things
- User data is obtained using https://github.com/thesadru/genshinstats
### Why make this
- Real-time notes feature only on hoyolab app but not desktop version
- Even using the app, I have to make 1000 taps to reach the real-time notes menu
- I don't play on my phone and I use my laptop most of the time, so I always forget checking my resin
