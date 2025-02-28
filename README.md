# Description
Download the selected torrent files matching your AnimeThemes playlist.

**Requirements:**
* Python
* qBittorrent (tested in 4.5.5)
* AnimeThemes torrent file from #faq channel on discord
* Your playlist must be public or unlisted

**Install:**
```
pip install animethemes-torrent-playlist
```

1. On qBittorrent, go to tools -> options -> Web Ui -> enable Web User Interface.
2. Set the port, username and password to whatever you want, and save it.
3. Edit the `config.json` file to match your qBittorrent settings. Optionally, you can disable auth in "Bypass authentication for clients on localhost".

## Usage
```
python -m torrent_playlist [-h] [--playlist | -p] [--file [FILE]]
```

Now resume the torrent from the client once script is finished.

**Playlist**

The hashid of the playlist (https://animethemes.moe/playlist/hashid).

**File**

The path of the `.torrent` file from the #faq channel on Discord.