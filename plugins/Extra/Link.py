from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Command to generate a link dynamically with bot's username
@Client.on_message(filters.command("link"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    
    # Check if movie name is provided
    if len(command_text) < 2:
        await message.reply("Please provide the name for the movie!\nExample: `/link game of thrones`")
        return
    
    # Replace spaces with hyphens for URL formatting
    movie_name = command_text[1].replace(" ", "-")
    
    # Dynamically get the bot's username
    bot_username = (await client.get_me()).username
    
    # Generate the link dynamically based on the bot's username and movie name
    link = f"https://telegram.me/{bot_username}?start=getfile-{movie_name}"
    
    # Send the reply with the generated link and share button
    await message.reply(
        text=f"🎬 Here is your link for *{command_text[1]}*:\n\n🔗 `{link}`\n\n*Powered by @{bot_username}*",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔗 Share Link", url=f"https://telegram.me/share/url?url={link}")],
                [InlineKeyboardButton(text="× Close", callback_data="close_data")]  # Use existing callback data
            ]
        )
    )
