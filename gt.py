from telethon import TelegramClient, events

client = TelegramClient('bot', 15994971, "f82e65c3fa6906f26c9337bb35352b62").start()

@client.on(events.NewMessage(pattern=r'\.sptbio'))
async def fd(event):
    await event.reply('yep')
    '''while(True):
        try:
            song = main()
            result = await client(functions.account.UpdateProfileRequest(
                first_name='Viktor',
                last_name='Kornatovskyi',
                about=main()
            ))
            time.sleep(10)
        except:
            return'''

client.run_until_disconnected()