import pprint, json, ast
import urllib2
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import xml.etree.cElementTree as et
import spotipy
import sys
# Create your views here.


def home(request):
    # # if len(sys.argv) > 1:
    # #     search_str = sys.argv[1]
    # # else:
    # #     search_str = 'garden'
    #
    # sp = spotipy.Spotify()
    # result = sp.album_tracks("24mCiOTIF5Ob1uwluRFERv")
    #
    # pprint.pprint(result)
    #
    # return render(request, "index.html", {'result':result})

    sxml = """
    <QUERIES>
      <AUTH>
        <CLIENT>9971968-C149540B51CE26F597BF9EF18F12E36C</CLIENT>
        <USER>260175070775627527-0EF9F1AC117E5B9DA2E8251432C5ABC7</USER>
      </AUTH>
      <QUERY CMD="ALBUM_SEARCH">
        <MODE>SINGLE_BEST_COVER</MODE>
        <TEXT TYPE="ARTIST">flying lotus</TEXT>
        <TEXT TYPE="ALBUM_TITLE">until the quiet comes</TEXT>
        <TEXT TYPE="TRACK_TITLE">all in</TEXT>
        <OPTION>
          <PARAMETER>SELECT_EXTENDED</PARAMETER>
          <VALUE>COVER,REVIEW,ARTIST_BIOGRAPHY,ARTIST_IMAGE,ARTIST_OET,MOOD,TEMPO</VALUE>
        </OPTION>
        <OPTION>
          <PARAMETER>SELECT_DETAIL</PARAMETER>
          <VALUE>GENRE:3LEVEL,MOOD:2LEVEL,TEMPO:3LEVEL,ARTIST_ORIGIN:4LEVEL,ARTIST_ERA:2LEVEL,ARTIST_TYPE:2LEVEL</VALUE>
        </OPTION>
      </QUERY>
    </QUERIES>
    """

    headers = {'Content-Type': 'application/xml'}
    response = requests.post('https://c9971968.web.cddbp.net/webapi/xml/1.0/',data =sxml, headers=headers)
    print response.content
    return render(request, "index.html", {'result': response})

