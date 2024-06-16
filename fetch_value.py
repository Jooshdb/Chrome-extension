import plyvel
import os
db_path = os.path.expanduser('~/.config/google-chrome/Default/Local Extension Settings/YOUR_EXTENSION_ID')

db = plyvel.DB(db_path, create_if_missing=False)

key = b'_sync:hello'
value = db.get(key)

if value:
    print(f'Stored value: {value.decode("utf-8")}')
else:
    print('Key not found in the database.')

db.close()