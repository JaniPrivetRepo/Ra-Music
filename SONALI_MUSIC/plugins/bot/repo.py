from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ Wҽʅƈσɱҽ Tσ Tҽαɱ Jαɳι Rҽρσʂ ❃</u>
 
✼ Rҽρσ Tσ Nԋι Mιʅҽɠα
 
❉ Jαɳι ραρα Bσʅσ Rҽρσ Oɯɳҽɾ Kσ 

✼ || [Sizzu Update](https://t.me/Vip_Jani) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="http://t.me/Vip_Jani"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/+gVWf5Y_c5NA5MGY1"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/SizzuMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/u15ml3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
