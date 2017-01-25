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

    title_path = '//div[@class="filmMainHeader"]//h1[@class="inline filmTitle"]/a'
    org_title_path = '//div[@class="filmMainHeader"]//h2'
    director_path = '//div[@class="filmMainHeader"]//div[@class="filmInfo bottom-15"]/table//tr[contains(th, "yseria:")]/td//li'
    writer_path = '//div[@class="filmMainHeader"]//div[@class="filmInfo bottom-15"]/table//tr[contains(th, "scenariusz:")]/td//li'
    genres_path = '//div[@class="filmMainHeader"]//div[@class="filmInfo bottom-15"]/table//tr[contains(th, "gatunek:")]/td//li'
    producer_path = '//div[@class="filmMainHeader"]//div[@class="filmInfo bottom-15"]/table//tr[contains(th, "produkcja:")]/td//li'
    release_year_path = '//div[@class="filmMainHeader"]//span[@class="halfSize"]'
    description_path = '//div[@class="filmMainHeader"]/div[@class="filmPlot bottom-15"]/p'
    rate_path = '//div[@class="filmVoteRatingPanelWrapper "]//span[@property="v:average"]'

    movie.title = __getText(root, title_path)
    movie.org_title = __getText(root, org_title_path)
    movie.director = __getText(root, director_path)
    movie.writer = __getText(root, writer_path)
    movie.genres = __getText(root, genres_path)
    movie.producer = __getText(root, producer_path)
    movie.release_year = __getText(root, release_year_path)
    movie.description = __getText(root, description_path)
    movie.rate = __getText(root, rate_path)
    movie.rate = movie.rate[1:]

    movie.release_year = movie.release_year[1:]
    movie.release_year = movie.release_year[:len(movie.release_year)-2]

    return movie


def __getText(root, xpath):
    elems = root.xpath(xpath)
    if len(elems) == 1:
        return elems[0].text_content()
    elif len(elems) > 1:
        my_string = ''
        for g in elems:
            my_string = my_string + g.text_content() + ', '
        my_string = my_string[:len(my_string) - 2] # without last comma and space
        return my_string
    else:
        return ''