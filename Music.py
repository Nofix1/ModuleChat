# meta developer: @AHIMETYAHKA
from .. import loader


@loader.tds
class AnimeVoicesMod(loader.Module):
    """🥵Плейлист лоликонщика🥵"""

    strings = {"name": "😬playlist lolikonshchika😬"}

    async def M1cmd(self, message):
        """⚡Выстрел В Пустоту⚡"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/Lolicon_Play_List/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def M2cmd(self, message):
      """🔞newlightchild — fuckoff🔞"""
reply = await message.get_reply_message()
await message.delete()
await message.client.send_file(
message.to_id,
"https://t.me/Lolicon_Play_List/8",
voice_note=True,
reply_to=reply.id if reply else None,
)
return
