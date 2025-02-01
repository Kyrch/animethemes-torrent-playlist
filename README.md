# Description
Download the selected torrent files matching your AnimeThemes playlist.

## **Requirements:**
* Python
* qBittorrent (tested in 4.5.5)
* AnimeThemes torrent file from #faq channel on discord
* Your playlist must be public or unlisted

## Usage
1. First of all, have the `.torrent` file in the same directory as the script.
2. Edit the `.torrent` filename to `AnimeThemes.torrent`.
3. On qBittorrent, go to tools -> options -> Web Ui -> enable Web User Interface.
4. Set the port, username and password to whatever you want, and save it.
5. Edit the `config.json` file to match your qBittorrent settings. Optionally, you can disable auth in "Bypass authentication for clients on localhost".
6. Run the script:

```
python __main__.py
```

7. Insert the hashid. The hashid is on your playlist URL of the website.
8. Now resume the torrent from the client.