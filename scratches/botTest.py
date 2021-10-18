import telebot  # importing Telegram API classes and functions
import libraries.qr_make as qr  # import qr_make lib with qr functions
from telebot import types
import os

# defining global vars
TOKEN = None

with open('token.txt') as f:
    TOKEN = f.read().strip()

# list with ids of users, who pressed start button
known_users = []
# dict with users ids, used for determination, who used /qr command
user_step = {}
bot = telebot.TeleBot(TOKEN)
# dict of bot commands
commands = {
    'start': 'Get used to bot',
    'help': 'Gives you information about available commands',
    'qr': 'Creates QR-image from web link'
}

# defining call to function, creating keyboard
commandSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
commandSelect.add('/help', '/qr')

# defining call to function, hiding keyboard
hideBoard = types.ReplyKeyboardRemove()


# function checks, if user is known and returns value out of user_step{}, if /qr was executed
def get_user_step(CHAT_ID):
    if CHAT_ID in user_step:
        return user_step[CHAT_ID]
    else:
        known_users.append(CHAT_ID)
        user_step[CHAT_ID] = 0
        print('New user detected, press start')
        return 0


# debug function, prints message to console, if /qr command hasn't been executed
def listener(messages):
    for mes in messages:
        if mes.content_type == 'text':
            return mes.text


# register listener func
bot.set_update_listener(listener)


# register and define start command
@bot.message_handler(commands=['start'])
def command_start(m):
    CHAT_ID = m.chat.id
    if CHAT_ID not in known_users:
        known_users.append(CHAT_ID)
        bot.send_message(CHAT_ID, 'Hello, stranger, let me scan you...')
        bot.send_message(CHAT_ID, 'Scanning complete, I know you now')
        user_step[CHAT_ID] = 1
    else:
        bot.send_message(CHAT_ID, 'I already know you, f**k off')
    bot.send_message(CHAT_ID, 'Please, make a choice:', reply_markup=commandSelect)


# register and define command /help
@bot.message_handler(commands=['help'])
def command_help(m):
    CHAT_ID = m.chat.id
    help_text = 'The following commands are available: \n'
    for key in commands:
        help_text += '/' + key + ': '
        help_text += commands[key] + '\n'
    bot.send_message(CHAT_ID, help_text)


# register and define command /qr
@bot.message_handler(commands=['qr'])
def command_qr(m):
    global user_step
    CHAT_ID = m.chat.id
    user_step[CHAT_ID] = 2
    bot.send_message(CHAT_ID, 'Please upload your link:')
    # set value 2 in dict with key CHAT_ID, so the link_to_qr would be executed


# register and define keyboard handler
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def com_select(m):
    CHAT_ID = m.chat.id
    text = m.text
    types.ReplyKeyboardRemove()

    bot.send_chat_action(CHAT_ID, 'typing')

    if text == '/help':
        bot.send_message(CHAT_ID, '/help', reply_markup=hideBoard)
        command_help(m)
    elif text == '/qr':
        bot.send_message(CHAT_ID, '/qr', reply_markup=hideBoard)
        command_qr(m)
    else:
        bot.send_message(CHAT_ID, 'Please use keyboard!')


# register and define link_to_qr func, with check, if user is execute /qr
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2)
def link_to_qr(m):
    CHAT_ID = m.chat.id
    CHAT_ID_STR = str(CHAT_ID)
    qr.image_make(m.text, CHAT_ID_STR)    # launching func from qr lib
    bot.send_message(CHAT_ID, 'Here is your QR')
    bot.send_photo(CHAT_ID, open('test_' + CHAT_ID_STR + '.png', 'rb'))     # sending user[CHAT_ID] message with photo
    os.remove('test_' + CHAT_ID_STR + '.png')                               # removing photo from local space
    user_step[CHAT_ID] = 0


# register and define message handler, which executes, if /qr has not executed
@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handler(m):
    CHAT_ID = m.chat.id
    bot.send_message(CHAT_ID, "Type /qr to get your QR-code")


# working continuously
bot.infinity_polling()
