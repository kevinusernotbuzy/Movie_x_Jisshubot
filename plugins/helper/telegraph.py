import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO

# Function to upload the image and get the URL
def upload_image_requests(image_path):
    upload_url = "https://envs.sh"
    
    try:
        # Open the file and prepare for upload
        with open(image_path, 'rb') as file:
            files = {'file': file} 
            response = requests.post(upload_url, files=files, timeout=60)  # Set a timeout to avoid hanging

            if response.status_code == 200:
                return response.text.strip()  # Return the link from the API
            else:
                raise Exception(f"Upload failed with status code {response.status_code}")

    except requests.exceptions.Timeout:
        print("Request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except Exception as e:
        print(f"Error during upload: {e}")
        return None


# Command to handle the upload process (for both private and group chats)
@Client.on_message(filters.command(["telegraph", "upload", "img", "tgm"]))
async def upload_command(client, message: Message):
    # Check if the message is a reply
    replied = message.reply_to_message
    
    # Ensure that the reply is a media file
    if not replied:
        await message.reply_text("Please reply to a photo or video to upload.")
        return

    # Check the type and size of the media
    if replied.media:
        if hasattr(replied, 'file_size') and replied.file_size > 5242880:  # 5 MB
            await message.reply_text("File size exceeds the 5 MB limit. Please upload a smaller file.")
            return
        
        # Check if the media is a valid image or video
        if replied.photo:
            file_type = "image"
        elif replied.video:
            file_type = "video"
        else:
            await message.reply_text("Unsupported media type. Only images or videos are allowed.")
            return

    # Download the media file
    silicon_path = await replied.download()

    # Notify user that the upload is in progress
    uploading_message = await message.reply_text("<code>Uploading...</code>")

    try:
        # Upload the media and get the URL
        silicon_url = upload_image_requests(silicon_path)
        if not silicon_url:
            raise Exception("Failed to upload file.")
    except Exception as error:
        # Handle upload failure
        await uploading_message.edit_text(f"Upload failed: {error}")
        return

    try:
        # Clean up by removing the downloaded file after upload
        os.remove(silicon_path)
    except Exception as error:
        print(f"Error removing file: {error}")

    # Send the link with buttons to open, share, or close the menu
    await uploading_message.edit_text(
        text=f"<b>Upload successful!</b>\n\n<b>Link :-</b> <code>{silicon_url}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(text="Open Link", url=silicon_url),  # Button to open the link
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={silicon_url}")  # Button to share the link
        ], [
            InlineKeyboardButton(text="Close", callback_data="close_data")  # Button to close the menu
        ]])
    )
