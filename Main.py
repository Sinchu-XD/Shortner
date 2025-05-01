from pyrogram import Client, filters
from playwright.async_api import async_playwright
import re
import os

API_ID = 6067591
API_HASH = "94e17044c2393f43fda31d3afe77b26b"
BOT_TOKEN = "8054585269:AAEj_cGeYi9UFMOpPVXm1lmCA_sBG-eRDSs"

bot = Client("shortener_bypass_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

url_pattern = re.compile(r'https?://\S+')

async def get_final_url(url):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(7000)
            try:
                await page.click("text=Get Link")  # Common label; may vary
                await page.wait_for_timeout(3000)
            except:
                pass
            final_url = page.url
            await browser.close()
            return final_url
    except Exception as e:
        return f"❌ Error: {e}"

@bot.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def bypass_link(_, message):
    urls = url_pattern.findall(message.text)
    if not urls:
        return await message.reply("❌ No link found in your message.")
    
    for url in urls:
        await message.reply(f"🔗 Bypassing: {url}")
        result = await get_final_url(url)
        await message.reply(f"✅ Final URL:\n{result}")

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
    await message.reply("👋 Send me any shortened link, and I’ll try to get its final destination URL.")

bot.run()
