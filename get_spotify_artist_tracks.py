import requests
from spotify_auth import spotify_auth


def spotify_album_data(artist_id, group_type, market):
    bearer_token = spotify_auth()["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}

    album_data = []

    for album_type in group_type:
        album_type_endpoint = \
            f"https://api.spotify.com/v1/artists/{artist_id}/albums?&limit=50&include_groups={album_type}&market={market}"

        response_json = requests.get(url=album_type_endpoint, headers=headers).json()

        if response_json["next"] is None:
            album_data.append(response_json)
        else:
            album_data.append(response_json)
            while response_json["next"] is not None:
                next_call = response_json["next"]
                response_json = requests.get(url=next_call, headers=headers).json()
                album_data.append(response_json)

    print(album_data[0]["items"][0]["name"])
    return album_data


spotify_album_data("6kBDZFXuLrZgHnvmPu9NsG", ["album"], "GB")