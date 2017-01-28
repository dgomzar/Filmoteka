# -*- coding: utf-8 -*-
from lxml import html
import urllib

class Movie:
    title = ''
    org_title = ''
    director = ''
    writer = ''
    genres = ''
    producer = ''
    release_year = ''
    description = ''
    rate = ''

    def printAll(self):
        print "title: ", self.title
        print "org_title: ", self.org_title
        print "director: ", self.director
        print "writer: ", self.writer
        print "genres: ", self.genres
        print "producer: ", self.producer
        print "release_year: ", self.release_year
        print "description: ", self.description
        print "rate: ", self.rate

def getMovieFromFilmweb(title):
    searchLink = 'http://www.filmweb.pl/search?q='
    titleWithoutSpaces = title.replace(' ', '+')
    urlSearch = searchLink + titleWithoutSpaces
    connection = urllib.urlopen(urlSearch)
    root = html.fromstring(connection.read())

    firstMovieFromSearchPath = '//ul[@class="sep-hr resultsList"]/li[1]//h3/a'
    movieLink = 'http://www.filmweb.pl' + root.xpath(firstMovieFromSearchPath)[0].attrib['href']

    return __parse(movieLink)

def __parse(url):
    connection = urllib.urlopen(url)
    root = html.fromstring(connection.read())
    movie = Movie()

    title_path = '//h1[@class="inline filmTitle"]/a'
    org_title_path = '//div[@class="filmMainHeader"]//h2'
    director_path = '//tr[contains(th, "yseria:")]/td'
    writer_path = '//tr[contains(th, "scenariusz:")]/td'
    genres_path = '//tr[contains(th, "gatunek:")]/td'
    producer_path = '//tr[contains(th, "produkcja:")]/td'
    release_year_path = '//span[@class="halfSize"]'
    description_path = '//div[@class="filmPlot bottom-15"]/p'
    rate_path = '//span[@property="v:average"]'

    movie.title = __getText(root, title_path)
    movie.org_title = __getText(root, org_title_path)
    movie.director = __getText(root, director_path)
    movie.writer = __getText(root, writer_path)
    movie.genres = __getText(root, genres_path)
    movie.producer = __getText(root, producer_path)
    movie.release_year = __getText(root, release_year_path)
    movie.description = __getText(root, description_path)
    movie.rate = __getText(root, rate_path)

    # remove spaces
    movie.rate = movie.rate.strip()
    movie.release_year = movie.release_year.strip()

    # remove parenthesis
    movie.release_year = movie.release_year.replace('(', '')
    movie.release_year = movie.release_year.replace(')', '')

    # when polish title is original title
    if (not movie.org_title):
        movie.org_title = movie.title
        movie.title = ""

    return movie

def __getText(root, xpath):
    entities = root.xpath(xpath + "//li")
    if(not entities):
        entities = root.xpath(xpath)
    result_string = ''
    if len(entities) == 1:
        result_string = entities[0].text_content()
    elif len(entities) > 1:
        for e in entities:
            result_string = result_string + e.text_content() + ', '
        result_string = result_string[:len(result_string) - 2] # without last comma and space
    return result_string
