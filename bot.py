import time
from pprint import pprint
import requests
from telethon import TelegramClient, events, functions

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = \
    'BQDqbfa0JHrnwvpUOY_yjNlpC8Y07KtDIsFwtmz9SKOWkbYrOSm375DbG2VVsiI0_9cIiuMhzJCwsgF1Rg-53TWWtogpgjG8CQ4A8uuDIPaxp25tmh0MnN7TbHR5H7EvOXFgkb9YsbUSItz-udIsg7O00d0NYNBtS4-1JUTAOlpd0D1cQFPJbcg1SsW-VIQxnnqwMo4-KCTN444'

client = TelegramClient('bot', 15994971, "f82e65c3fa6906f26c9337bb35352b62").start()


@client.on(events.NewMessage(outgoing=True, pattern=r'\.d'))
async def fd(event):
    await event.reply('yep')
    while True:
        try:
            await client(functions.account.UpdateProfileRequest(
                first_name='Viktor',
                last_name='Kornatovskyi',
                about=main()
            ))
            print('+')
            time.sleep(10)
        except:
            return
@client.on(events.NewMessage)
async def fdr(event):
    print(event.text)

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": artist_names,
        "link": link
    }

    return current_track_info


def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']

        time.sleep(1)
        return current_track_info['track_name']


if __name__ == '__main__':
    main()

client.run_until_disconnected()
