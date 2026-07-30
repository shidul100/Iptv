import json

with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n\n")

    for ch in channels:
        name = ch.get("name", "")
        tvg_id = ch.get("tvg_id", "")
        logo = ch.get("logo", "")
        group = ch.get("group", "")
        url = ch.get("url", "")

        extinf = (
            f'#EXTINF:-1 '
            f'tvg-id="{tvg_id}" '
            f'tvg-logo="{logo}" '
            f'group-title="{group}",'
            f'{name}'
        )

        f.write(extinf + "\n")
        f.write(url + "\n\n")

print(f"Generated M3U with {len(channels)} channels.")
