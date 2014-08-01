import pprint, json, ast
import urllib2
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
import xml.etree.cElementTree as et
import spotipy
import sys
# Create your views here.
from mood.forms import EmailUserCreationForm
from mood.models import Song, Movie, Listener
from moodproject import settings
import pygn


def home(request):
    g_client_id = "9971968-C149540B51CE26F597BF9EF18F12E36C"
    g_user_id = "260175070775627527-0EF9F1AC117E5B9DA2E8251432C5ABC7"
    # # if len(sys.argv) > 1:
    # #     search_str = sys.argv[1]
    # # else:
    # #     search_str = 'garden'
    #
    # sp = spotipy.Spotify()
    #
    # result2 = sp.search("garden state motion picture", limit=1, type="album")
    #
    # result2 = result2['albums']['items'][0]['id']
    # result = sp.album_tracks(result2)
    # artist = result['items'][0]['artists'][0]['name']
    #
    #
    #
    # pprint.pprint(result)
    # # pprint.pprint(result2)
    # return render(request, "index.html", {'result':result2})

    # result = pygn.search(clientID= g_client_id, userID= g_user_id, artist='Kings Of Convenience', track='Homesick')
    # result = result["mood"]

    # generate a radio via gracenote pgyn.
    # result = pygn.createRadio(clientID=g_client_id, userID=g_user_id, mood='65322', popularity ='1000', similarity = '1000')
    # print json.dumps(result, sort_keys=True, indent=4)
    # return render(request, "index.html", {'result': result})

    # sxml = """
    # <QUERIES>
    #   <AUTH>
    #     <CLIENT>9971968-C149540B51CE26F597BF9EF18F12E36C</CLIENT>
    #     <USER>260175070775627527-0EF9F1AC117E5B9DA2E8251432C5ABC7</USER>
    #   </AUTH>
    #   <QUERY CMD="ALBUM_SEARCH">
    #     <MODE>SINGLE_BEST_COVER</MODE>
    #     <TEXT TYPE="ARTIST">flying lotus</TEXT>
    #     <TEXT TYPE="ALBUM_TITLE">until the quiet comes</TEXT>
    #     <TEXT TYPE="TRACK_TITLE">all in</TEXT>
    #     <OPTION>
    #       <PARAMETER>SELECT_EXTENDED</PARAMETER>
    #       <VALUE>COVER,REVIEW,ARTIST_BIOGRAPHY,ARTIST_IMAGE,ARTIST_OET,MOOD,TEMPO</VALUE>
    #     </OPTION>
    #     <OPTION>
    #       <PARAMETER>SELECT_DETAIL</PARAMETER>
    #       <VALUE>GENRE:3LEVEL,MOOD:2LEVEL,TEMPO:3LEVEL,ARTIST_ORIGIN:4LEVEL,ARTIST_ERA:2LEVEL,ARTIST_TYPE:2LEVEL</VALUE>
    #     </OPTION>
    #   </QUERY>
    # </QUERIES>
    # """
    #
    # headers = {'Content-Type': 'application/xml'}
    # response = requests.post('https://c9971968.web.cddbp.net/webapi/xml/1.0/',data =sxml, headers=headers)
    # print response.content
    # return render(request, "index.html", {'result': response})


@login_required
@csrf_exempt
def search(request):
    return render(request, "search.html")


def index(request):
    return render(request, "index.html")

@login_required
@csrf_exempt
def search_results(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print "HELLO!"
        print data
        pprint.pprint(data)
        query = "{} motion picture".format(data['album_query'])
        print query
        sp = spotipy.Spotify()
        current_movie = Movie.objects.create(title=data['album_query'])
        current_movie.save()
        current_movie.listener.add(request.user)
        # current_movie.add(request.user)
        movie_id = sp.search(query, limit=1, type="album")['albums']['items'][0]['id']
        # current_movie.add(Listener.objects.get(username=request.user))
        print request.user
        current_movie.save()
        songs = sp.album_tracks(movie_id)
        for song in songs['items']:
            this_song = Song.objects.create(title=song['name'], artist=song['artists'][0]['name'])
            this_song.save()
            print song['name']
            print song['artists'][0]['name']
            this_song.song_movie.add(current_movie)
            this_song.listener.add(request.user)
            # above line to link the many to many relationship
            print this_song.song_movie

        # artist = songs['items'][0]['artists'][0]['name']

        return HttpResponse(json.dumps({'hello': 'hello'}), content_type='application/json')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #user.email_user("Welcome!", "Thank you for signing up for our website.")
            # text_content = 'Thank you for signing up for our website, {} {}.' \
            #                'You joined us at {}'.format(user.first_name, user.last_name, user.date_joined)
            # html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our ' \
            #                'site. You joined us at {} </div>'.format(user.first_name, user.last_name, user.date_joined)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("search")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def profile(request):
    return render(request, "index.html")

