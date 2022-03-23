English | [中文](https://github.com/seriaati/hoyolab-resin-counter/blob/main/README.zh-tw.md)
# hoyolab-resin-counter
![hoyolab-resin-counter (Small)](https://user-images.githubusercontent.com/61446626/159615993-8801f175-84b7-4361-bf65-7fb70708341a.png)
\nHoyolab real-time notes feature but on desktop.

## Features
- Shows your current resin
- Shows how much time until resin is full
- Shows realm currency
- Shows number of expeditions completed
- Super duper fast resin checking after you have setup your account

## Setting up hoyolab-resin-counter
- Download and install python from https://www.python.org/downloads (Remember to check "Add Python to PATH")
- If popped up, click "Disable PATH length limit"
- Download the latest realease of hoyolab-resin-counter and place it somewhere

### Adding your account
- Go to https://www.hoyolab.com and login your account.
- F12 or ctrl+shift+I to open up the developer tools menu.
- In the developer tools menu -> Application -> Cookies -> https://www.hoyolab.com/home
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
