
# Not a Basic Telegram Bot 

Hi folks , I created a chat bot with additional features for Telegram in python. its simple and straight forward so you can customize it according to your needs.





## Documentation
**Introduction**

This is simple but not basic telegram bot build in python,
This is sample/test project with every new update bot becomes more advance.

**Features**

    1 - Show News
    2 - Recommend random movie
    3 - Tell weather
    4 - Can play snake,water,gun
    5 - Basic calculator
    6 - Can search on Wikkipedia
    7 - Can serach on google
    8 - Give response to your messages

**commands for bot**
|Features            | commands                                                               |
| ----------------- | ------------------------------------------------------------------ |
| news ||news,show news
| movies suggestion |  movie, suggest movie|
| weather |weather {location}|
| Snake,water,gun | game {snake/water/gun}|
| Calculator | action n1 and n2 {add 2 and 3}|
| Wikkipedia | search keyword {search bitcoin}|
| Google| google keyword {google python}|
|General chat| /start|


**Using Features**

For using advance features you needed to add APIs in constant.py,all the information regarding APIs is giving below.
*only news,weather and movie feature need api, which are optionals but telegram bot api is mandatory.*

**Adding APIs**
```bash
nano /path/to/tg_bot/constant.py
```

*For Developers*

1 - All responses are handling from response.py

2 - all constant/api will add in constant.py

## APIs I'm using in this Bot

|Features            | Url                                                                |
| ----------------- | ------------------------------------------------------------------ |
| news ||https://newsapi.org
| weather |https://rapidapi.com/weatherbit/api/weather/|
| movies suggestion | https://rapidapi.com/jakash1997/api/advanced-movie-search/ |
| Telegram bot API |https://t.me/BotFather|


## Deployment

To deploy this Telegram Bot on Linux(Ubuntu,Debian)
```bash
apt-get update
```
```bash
apt-get upgrade
```
```bash
git clone 
```
```bash
cd /path/to/tg_bot
```
```bash
sudo pip3 install -r requirements.txt  
```
```bash
python3 main.py
```


