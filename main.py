import os,telebot,requests,json

# bot_token = os.environ.get('TELEGRAM_TOKEN', None)

# TELEGRAM_BOT_TOKEN = "1464973754:AAHG3Lj7EX0URgg6I_WbHvXNH5xqmILdluo"
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', None)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# BOT_ADMIN = "1072778890"
BOT_ADMIN = os.environ.get('BOT_ADMIN', None)
# CHANNEL_ID = "-423212571"
CHANNEL_ID = os.environ.get('CHANNEL_ID', None)

@bot.message_handler(commands=['start'])
def start(m):
    cid = m.chat.id
    if cid == int(BOT_ADMIN):
        bot.send_message(BOT_ADMIN,"Hi <b>Admin</b>\nThis bot is now operating <b>properly</b>\n\n<b><s>Note</s></b> : To start bot and start <b>sending deals</b> to your <b>channel</b> or <b>bot</b> , click on /senddeals and this command can only be used by admin of the bot.\nThis bot is in beta version and some errors can come, Please forward any <b>error</b> to @P4R4D0XXX",parse_mode="HTMl")

@bot.message_handler(commands=['senddeals'])
def send_deals(m):
    cid = m.chat.id

    url = "https://tbb-dealscraper.herokuapp.com/api/posts?per_page=100"
    deals_request = requests.get(url).text
    deals_json = json.loads(deals_request)

    for deals in deals_json:
        id = deals['id']
        title = deals['title']
        discount_price = deals['discount']
        original_price = deals['original']
        website_link = deals['website']
        liked_by = deals['hotness']
        deal_link = deals['deal_link']
        publish_date = deals['posting_date']
        expiry_date = deals['expiry_date']
        days_left = deals['days_left']
        image_link = deals['image']

        bot.send_photo(CHANNEL_ID,image_link,title+"/n"+website_link+"/n"+deal_link,parse_mode='HTML')

        from matplotlib import pyplot as plt
        plt.pause(300)



bot.polling()
