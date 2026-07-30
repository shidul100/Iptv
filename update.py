import re
import json

channels = []

with open("playlist.m3u", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

for i in range(len(lines)):
    line = lines[i]

    if line.startswith("#EXTINF"):
        name = line.split(",")[-1]

        tvg_id = ""
        logo = ""
        group = ""

        match = re.search(r'tvg-id="([^"]*)"', line)
        if match:
            tvg_id = match.group(1)

        match = re.search(r'tvg-logo="([^"]*)"', line)
        if match:
            logo = match.group(1)

        match = re.search(r'group-title="([^"]*)"', line)
        if match:
            group = match.group(1)

        url = ""
        if i + 1 < len(lines):
            url = lines[i + 1]

        channels.append(
            {
                "name": name,
                "tvg_id": tvg_id,
                "logo": logo,
                "group": group,
                "url": url,
            }
        )

with open("channels.json", "w", encoding="utf-8") as f:
    json.dump(channels, f, ensure_ascii=False, indent=2)

print(f"Updated {len(channels)} channels.")
