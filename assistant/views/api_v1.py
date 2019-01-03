import traceback
import requests
import flask
from flask import json, jsonify, request, render_template, url_for, Response, make_response
from sentimeter import app, logger

@app.route('/api/v1/assistant', methods=['POST'])
def assistant():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    if req["queryResult"]["action"] == "FindSong":
            return(find_song_and_play(req))

def find_song_and_play(req):
        song_name = req.get("queryResult").get("parameters").get("songname")
        song_url = search_song_url(song_name)
        my_result = {
            "fulfillmentText": "This is a text response",
            "fulfillmentMessages": [
                {
                    "card": {
                        "title": "card title",
                        "subtitle": "card text",
                        "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                        "buttons": [
                            {
                                "text": "button text",
                                "postback": "https://assistant.google.com/"
                            }
                        ]
                    }
                }
            ],
            "source": "example.com",
            "payload": {
                "google": {
                    "expectUserResponse": False,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": "Sure, Let's get your song playing"
                                }
                            },
                            {
                                "mediaResponse": {
                                        "mediaType": "AUDIO",
                                        "mediaObjects": [
                                        {
                                                "name": "Exercises",
                                                        "description": "ex",
                                                        "largeImage": {
                                                        "url": "http://storage.googleapis.com/automotive-media/album_art.jpg",
                                                        "accessibilityText": "..."
                                                        },
                                                "contentUrl": song_url
                                        }
                                        ]
                                }
                            }
                        ]
                    }
                },
                "facebook": {
                    "text": "Hello, Facebook!"
                },
                "slack": {
                    "text": "This is a text response for Slack."
                }
            }
        }



        res = json.dumps(my_result, indent=4)
        print(res)
        r = make_response(res)
        return r

def search_song_url(song_name):
        search_api = "https://api.anyaudio.in"
        song_search_url = "https://api.anyaudio.in/api/v1/search?q="
        song_name = song_name.replace(" ", "+")
        song_search_url = song_search_url + song_name
        search_response = requests.get(song_search_url)
        if search_response.status_code == 200:
                search_results = json.loads(search_response.content)
                song_stream_url = search_api + search_results['results'][0]['stream_url']
                stream_url_response = requests.get(song_stream_url)
                stream_url = json.loads(stream_url_response.content)
                song_url = search_api + stream_url['url']        
                return song_url

