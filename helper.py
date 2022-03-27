import json
import requests
from secrets import spotify_user_id
from datetime import date
from refresh import Refresh


def get_playback_state():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player"

    response = requests.get(query, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

    response_json = response.json()

    return response_json['is_playing']

def skip_to_previous():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/previous"

    response = requests.post(query, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

def skip_to_next():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/next"

    response = requests.post(query, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

def pause_playback():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/pause"

    response = requests.put(query, data={}, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

def resume_playback():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/play"

    response = requests.put(query, data={}, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

def start_playback(track_id, track_type):

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/play"

    data = json.dumps({'context_uri': "spotify:{}:{}".format(track_type, track_id)})
    response = requests.put(query, data=data, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

def get_available_devices():

    refreshCaller = Refresh()
    spotify_token = refreshCaller.refresh()

    query = "https://api.spotify.com/v1/me/player/devices"

    response = requests.get(query, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        })

    response_json = response.json()

    return response_json['devices']

def play_on_device(device_name):

    devices = get_available_devices()

    for device in devices:

        if (device['name'] == device_name):

            refreshCaller = Refresh()
            spotify_token = refreshCaller.refresh()

            query = "https://api.spotify.com/v1/me/player"

            data = json.dumps({'device_ids': [device['id']]})
            response = requests.put(query, data=data, headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(spotify_token)
                })

            break
