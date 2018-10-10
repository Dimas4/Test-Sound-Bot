import time

from initialize.initialize_backend.initialize import initialize as init_backend
from initialize.initialize_db.initialize import initialize as init_db


def start(token, backend, db, filename):
    bot = init_backend(token, backend)
    print(db)
    db = init_db(db)

    while True:
        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, body = bot.get_message_and_id(messages)
            bot.convert_text_to_voice(body)
            uploaded_voice = bot.upload_file(filename, id)
            bot.send_message(id, attach=uploaded_voice)

        time.sleep(1)
