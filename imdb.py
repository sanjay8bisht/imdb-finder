###############################################################################
############                                                       ############
############         Name:        imdb-movie-finder                ############
############         Purpose:     Find movie details               ############
############         Author:      Sanjay Bisht                     ############
############                                                       ############
###############################################################################

import json
import webbrowser
import os
import sys
import datetime


def get_response(url):
    PY_VERSION = sys.version_info[0]

    if PY_VERSION == 2:
        try:
            import urllib
            return json.loads(urllib.urlopen(url).read())
        except:
            raise Exception('try -> pip install urllib')

    if PY_VERSION == 3:
        try:
            import requests
            return json.loads(requests.get(url).text)
        except:
            raise Exception("try -> pip install requests")


def finder(*args):
    if len(args[0]) > 1:
        url = "http://www.omdbapi.com/?t="+str(args[0][0])+"&y="+str(args[0][1])

    else:
        url = "http://www.omdbapi.com/?t="+str(args[0][0])

    response = get_response(url)
    if response["Response"]=="True":
        imdbname = response['Title']
        imdbreleasedate = response['Released']
        imdbrating = response['imdbRating']
        imdbvotes = response['imdbVotes']
        imdbgenre = response['Genre']
        imdbcountry = response['Country']
        imdbactors = response['Actors']
        imdbdirector = response['Director']
        imdburl = "http://www.imdb.com/title/"+response['imdbID']
        imdbruntime = response['Runtime']
        imdbplot = response['Plot']
        imdbawards = response['Awards']
        if len(args[0]) == 3 and args[0][2] == 'open':
            webbrowser.open(imdburl)


    else:
        imdbname = "Could not find"
        imdbreleasedate = "NA"
        imdbrating = "NA"
        imdbvotes = "NA"
        imdbgenre = "NA"
        imdbcountry = "NA"
        imdbactors = "NA"
        imdbdirector = "NA"
        imdburl = "NA"
        imdbruntime = "NA"
        imdbplot = "NA"
        imdbawards = "NA"


    result = """
        Movie : {imdbname}
        Release Date : {imdbreleasedate}
        Rating : {imdbrating}
        Votes : {imdbvotes}
        Genre : {imdbgenre}
        Country : {imdbcountry}
        Actors : {imdbactors}
        Director : {imdbdirector}
        IMDB Link : {imdburl}
        Runtime : {imdbruntime}
        Plot : {imdbplot}
        Awards : {imdbawards}""".format(
                imdbname=imdbname,imdbreleasedate=imdbreleasedate,imdbrating=imdbrating,
                imdbvotes=imdbvotes,imdbgenre=imdbgenre,imdbcountry=imdbcountry,
                imdbactors=imdbactors,imdbdirector=imdbdirector,imdburl=imdburl,
                imdbruntime=imdbruntime,imdbplot=imdbplot,imdbawards=imdbawards
                )

    print(result)

args = []

movie = sys.argv[1]
args.append(movie)

try:
    year = sys.argv[2]
    args.append(year)
except:
    pass

try:
    web = sys.argv[3]
    args.append(web)
except:
    pass

if len(sys.argv) > 4:
    raise Exception("can't have more than 4 arguments")

finder(args)