
# Not a Basic Telegram Bot 

Hi folks, I created a chatbot with additional features for Telegram in Python. it's simple and straight forward so you can customize it according to your needs.





## Documentation
**Introduction**

This is a simple but not basic telegram bot built in Python,
This is a sample/test project with every new update bot becomes more advance.

**Features**

    1 - Show News
    2 - Recommend a random movie
    3 - Tell the weather
    4 - Can play snake, water, gun
    5 - Basic calculator
    6 - Can search on Wikipedia
    7 - Can search on Google
    8 - Give a response to your messages

**commands for bot**
|Features            | commands                                                               |
| ----------------- | ------------------------------------------------------------------ |
| news | news, show news |
| movies suggestion |  movie, suggest movie|
| weather |weather {location}|
| Snake,water,gun | game {snake/water/gun}|
| Calculator | action n1 and n2 {add 2 and 3}|
| Wikipedia | search keyword {search bitcoin}|
| Google| google keyword {google python}|
|General chat| /start|


**Using Features**

For using advanced features you needed to add APIs in constant.py, all the information regarding APIs is given below.
*only news, weather, and movie feature need API, which are optional but telegram bot API is mandatory.*

**Adding APIs**
```bash
nano /path/to/tg_bot/constant.py
```

*For Developers*

1 - All responses are handled from response.py

2 - all constant/API will add in constant.py

## APIs I'm using in this Bot

|Features            | Url                                                                |
| ----------------- | ------------------------------------------------------------------ |
| news ||https://newsapi.org
| weather |https://rapidapi.com/weatherbit/api/weather/|
| movies suggestion | https://rapidapi.com/jakash1997/api/advanced-movie-search/ |
| Telegram bot API |https://t.me/BotFather|


## Deployment

To deploy this Telegram Bot on Linux(Ubuntu, Debian)
```bash
apt-get update
```
```bash
apt-get upgrade
```
```bash
git clone https://github.com/hsbeast/Not_a_Basic_Telegram_bot.git 
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



