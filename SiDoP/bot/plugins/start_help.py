# (c) NobiDeveloper
from SiDoP.bot import StreamBot
from SiDoP.vars import Var
import logging
logger = logging.getLogger(__name__)
from SiDoP.bot.plugins.stream import MY_PASS
from SiDoP.utils.human_readable import humanbytes
from SiDoP.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from SiDoP.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if 1==1:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚", "Join📢"],
                ["Movie Grp","status📊"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚"],
                ["Movie-Search-Grp","list"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.private & filters.command("start") | filters.regex('start⚡️')))
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://graph.org/file/d7fda0806e439dcca9632.jpg",
        caption =f'{m.from_user.mention(style="md")},\n\nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ɢᴇɴᴇʀᴀᴛᴏʀ  ʙᴏᴛ.\n\nᴊᴜꜱᴛ  ꜱᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ꜰɪʟᴇ  ᴀɴᴅ  ɢᴇᴛ  ᴀ  ᴅɪʀᴇᴄᴛ  ᴅᴏᴡɴʟᴏᴀᴅ  ʟɪɴᴋ  ᴀɴᴅ  ꜱᴛʀᴇᴀᴍᴀʙʟᴇ  ʟɪɴᴋ.',
        reply_markup=buttonz)
        await db.add_user(m.from_user.id)
      #  await pass_db.add_user_pass(m.from_user.id, MOVIESXSTORE)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/d7fda0806e439dcca9632.jpg",
                caption="<b>⚠️  ɪɴ  ᴏʀᴅᴇʀ  ᴛᴏ  ᴜꜱᴇ  ᴍᴇ.  ʏᴏᴜ  ʜᴀᴠᴇ  ᴛᴏ  ᴊᴏɪɴ  ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇs  ᴄʜᴀɴɴᴇʟ  ꜰɪʀsᴛ.</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔   ᴜᴘᴅᴀᴛᴇ  ᴄʜᴀɴɴᴇʟ   ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>ꜱᴏᴍᴇᴛʜɪɴɢ  ᴡᴇɴᴛ  ᴡʀᴏɴɢ  <a href='https://telegram.me/botxhub'>ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ꜰᴏʀ  ꜱᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://graph.org/file/d7fda0806e439dcca9632.jpg",
        caption =f'{m.from_user.mention(style="md")},\n\nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ɢᴇɴᴇʀᴀᴛᴏʀ  ʙᴏᴛ.\n\nᴊᴜꜱᴛ  ꜱᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ꜰɪʟᴇ  ᴀɴᴅ  ɢᴇᴛ  ᴀ  ᴅɪʀᴇᴄᴛ  ᴅᴏᴡɴʟᴏᴀᴅ  ʟɪɴᴋ  ᴀɴᴅ  ꜱᴛʀᴇᴀᴍᴀʙʟᴇ  ʟɪɴᴋ.',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://graph.org/file/d7fda0806e439dcca9632.jpg",
                caption="<b>⚠️  ᴘʟᴇᴀꜱᴇ  ꜰᴏʟʟᴏᴡ  ᴛʜɪꜱ  ʀᴜʟᴇ  ⚠️\n\n ɪɴ  ᴏʀᴅᴇʀ  ᴛᴏ  ᴜꜱᴇ  ᴍᴇ.\n\nʏᴏᴜ  ʜᴀᴠᴇ  ᴛᴏ  ᴊᴏɪɴ  ᴏᴜʀ  ᴏꜰꜰɪᴄɪᴀʟ  ᴄʜᴀɴɴᴇʟ  ꜰɪʀsᴛ.</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(" 🔥   𝙹𝙾𝙸𝙽  𝙾𝚄𝚁  𝙲𝙷𝙰𝙽𝙽𝙴𝙻   🔥 ", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ [ᴏᴡɴᴇʀ](https://telegram.me/Don_owner).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs 😜</b>

<b>╭━━━━〔ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b> 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 : Just 𝚂𝙴𝙽𝙳 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾</b>
┣⪼<b>ᴜᴘᴅᴀᴛᴇꜱ : <a href='https://t.me/Movies_x_store'> MAIN CHANNEL</a></b>
┣⪼<b>ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ : <a href='https://t.me/MoviesSearchingGroup'>🔎SEARCH HERE🔍</a></b>
┃
<b>╰━━━━〔ᴘʟᴇᴀꜱᴇ sᴜᴘᴘᴏʀᴛ〕</b>""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻  ᴏᴡɴᴇʀ", url="https://t.me/UNKNOWNforall")]
                
            ]
        )
    )
