import json
import requests

# Get video paths of the playlist by its hashid
def get_video_paths(hashid):
    r = requests.get(f'https://api.animethemes.moe/playlist/{hashid}?include=tracks.video&fields[playlist]=name&fields[video]=path')
    data = r.json()

    video_paths = [track['video']['path'] for track in data['playlist']['tracks']]

    print_green(f'Retrieved {len(video_paths)} videos')

    return {
        'name': data['playlist']['name'],
        'videos': video_paths
    }

def main():
    hashid = input('Playlist hashid (https://animethemes.moe/playlist/hashid): ')
    info = get_video_paths(hashid)

    session = requests.Session()

    config = get_config()

    url = get_url(config)

    # Login to the client
    session.post(f'{url}/auth/login', data={'username': config['username'], 'password': config['password']})

    # Add torrent to the client
    session.post(f'{url}/torrents/add', files=get_torrent_file(), data={'paused': 'true'})
   # time.sleep(2)

    # Get all torrents available in the client
    animethemes_torrent = []
    while animethemes_torrent == []:
        torrents = session.get(f'{url}/torrents/info').json()

        # Filter by AnimeThemes torrent
        animethemes_torrent = list(filter(lambda torrent: torrent['name'] == 'AnimeThemes', torrents))

    hash = animethemes_torrent[-1]['hash']

    # Get files of the AnimeThemes torrent
    files = session.get(f'{url}/torrents/files?hash={hash}').json()

    # Get the list of ids to not download
    files_to_decrease = [str(file['index']) for file in files if file['name'].replace('AnimeThemes/', '') not in info['videos']]

    # Set all unwanted files priority to 0
    session.post(f'{url}/torrents/filePrio', data={
        'hash': hash,
        'id': '|'.join(files_to_decrease),
        'priority': 0
    })

# Read AnimeThemes.torrent file
def get_torrent_file():
    return {
        'torrents': open('AnimeThemes.torrent', 'rb')
    }

# Get the client API URL
def get_url(config):
    return config['ip'] + ':' + config['port'] + '/api/v2'

# Read config.json file
def get_config():
    with open('config.json', 'r') as config:
        return json.loads(config.read())

def print_green(text: str):
    print('\033[92m' + text + '\033[0m')

if __name__ == '__main__':
    main()