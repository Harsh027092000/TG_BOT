import requests
import json
from datetime import datetime
from datetime import timedelta
import random
import time
from googlesearch import search
import wikipedia
from geopy.geocoders import Nominatim
from constant import news_api,movie_api,weather_api



def sample_response(input_text):
    user_msg = str(input_text).lower()

    if user_msg in ("news","News","Show news","tell news"):
        """this function is use to fetch news from newsapi.org by typing news in chatbox""" 
        n1 = random.randint(1,9)
        n2 = random.randint(1,9)
        presentday = datetime.now()
        yesterday = presentday - timedelta(1)
        date = yesterday.strftime('%Y-%m-%d')
        topic  = ["politics","science","technology","business","socialmedia"]
        topic = random.choice(topic)
        api_key = news_api
        reponse = requests.get(f"https://newsapi.org/v2/everything?q={topic}&from={date}&apiKey={api_key}")
        news = reponse.content
        news1 = json.loads(news.decode('utf-8'))
        try:
            news2 = news1["articles"][n2:n1][0]
            newst = news2["title"]
            newsd = news2["description"]
            newsu = news2["url"]
            return "title :: ",newst,"description :: ",newsd,"read in deatils :: ",newsu
        except:
            return "No news right now kindly try again"
    if user_msg.startswith('search'):
        """this function is use to fetch infomation from wikkipedia by typing search(keyword)""" 
        se = wikipedia.summary(user_msg.strip("search "))
        return se
    
    if user_msg.startswith('weather'):
        """this function is use to fetch weather infomation from weatherbit/rapid api by typing weather city"""
        ge = user_msg.strip("weather ")
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(ge)
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

        querystring = {"lat":getLoc.latitude,"lon":getLoc.longitude}

        headers = {
            "X-RapidAPI-Key": weather_api,
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()['data'][0]
    """basic calculator format(action firstnumber and secondnumber)"""
    li = ("add","+","addition","sum","minus","sub","substract","-","multiple","*","X","multiply","div","divide","/","division")
    if user_msg.startswith(li):
        if user_msg.startswith(li[0:4]):
            l = user_msg.split(" ")
            try:
                result = str(int(l[1]) + int(l[3]))
                result = f"result = {result}"
                return result
            except:
                return "enter valid input (action 1num and 2num)"
        if user_msg.startswith(li[4:8]):
            l = user_msg.split(" ")
            try:
                result = str(int(l[1]) - int(l[3]))
                result = f"result = {result}"
                return result
            except:
                return "enter valid input (action 1num and 2num)"
        if user_msg.startswith(li[8:12]):
            l = user_msg.split(" ")
            try:
                result = str(int(l[1]) * int(l[3]))
                result = f"result = {result}"
                return result
            except:
                return "enter valid input (action 1num and 2num)"
        if user_msg.startswith(li[12:16]):
            l = user_msg.split(" ")
            try:
                result = str(int(l[1]) / int(l[3]))
                result = f"result = {result}"
                return result
            except:
                return "enter valid input (action 1num and 2num)"
    if user_msg in ("movie","suggest movie","show movie"):
        """this function used to recommend random movie"""
        genre = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]
        genre = random.choice(genre)
        page = random.randint(1,5)
        url = "https://advanced-movie-search.p.rapidapi.com/discover/movie"
        querystring = {"with_genres":str(genre),"page":str(page)}
        headers = {
            "X-RapidAPI-Key": movie_api,
            "X-RapidAPI-Host": "advanced-movie-search.p.rapidapi.com"
            }
        response = requests.get(url, headers=headers, params=querystring)
        content = response.json()["results"] 
        ind = random.randint(0,5)
        movie = content[ind]['original_title']
        overview = content[ind]['overview']
        poster = content[ind]['poster_path']
        ratings = content[ind]['vote_average']
        release_date = content[ind]['release_date']
        return f"movie name : {movie} || release date : {release_date} || details : {overview} || ratings : {ratings} || {poster}"
    if user_msg.startswith('google'):
        """Google serach this function is not so efficient""" 
        query = user_msg.strip("google ")  
        my_results_list = []  
        for i in search(query,        # The query you want to run  
            tld = 'com',  # The top level domain  
            lang = 'en',  # The language  
            num = 10,     # Number of results per page  
            start = 0,    # First result to retrieve  
            stop = None,  # Last result to retrieve  
            pause = 2.0,  # Lapse between HTTP requests  
            ):  
            my_results_list.append(i)  
            return my_results_list 
        
    """Chat response""" 
    if user_msg in ("hi","hello","greetings","sup"):
        return "Hey how may i help you?"    
    if user_msg in ("who are you","what is you","who","who you","who u"):
        return "I am TG_BOT"
    if user_msg in ('bye','quit','adios','tata','see you again','bbye'):
        return "Bye have a great time"
    if user_msg in ('How are you','how is you','are you fine','are you good'):
        return "I am good thanks for asking"
       
          

def game(input_text):
    user_msg = str(input_text).lower()
    c = random.choice(['snake','gun','water'])
    text = user_msg.split(' ')
    u = text[1]
    if u == 'gun' and c == 'snake' or u == 'water' and c == 'gun' or u == 'snake' and c == 'water':
         return f"You win i choosed::{c}"
    elif c ==u:
         return f'draw with we both choosed::{c}'
    else:
        return f"I win i choosed::{c}"