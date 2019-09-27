import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render
from movieapp.models import Movie

# Create your views here.
page = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
soup = BeautifulSoup(page.content,'html.parser')
movie_list = soup.find_all(class_="titleColumn")
l = len(movie_list)


def create_movie_list(request):
    for i in range(l):
        movie_url = movie_list[i].find('a').get('href')
        description_url = 'http://imdb.com'+ movie_url
        second_page = requests.get(description_url)
        soup1 = BeautifulSoup(second_page.content,'html.parser')
        movie_name = soup1.find('h1').get_text().split('(')[0]
        #print(movie_name.split('(')[0])
        movie_rating = soup1.find('span',itemprop='ratingValue').get_text()
        #print(movie_rating)
        movie_release_date = soup1.find('a',title='See more release dates').get_text().split('(')[0]
        #print(movie_release_date.split('(')[0])
        movie_duration =soup1.find('time').get_text().strip()
        # movie_sduration = movie_duration.strip()
        #print(movie_duration)
        movie_description = soup1.find(class_='summary_text').get_text().strip()
        Movie.objects.create(
            movie_name=movie_name,
            movie_rating=movie_rating,
            release_date=movie_release_date,
            movie_duration=movie_duration,
            movie_description=movie_description
        )
    return HttpResponseRedirect('/')
