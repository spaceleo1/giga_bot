from databases import Database

database = Database('sqlite:///bot.db')

# maybe unused
async def create_table():
    sql = '''
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            nickname text NOT NULL
        );
    '''
    await database.execute(sql)

async def save(user_id, nickname):
    sql = '''
        INSERT OR IGNORE INTO users(user_id, nickname)
        VALUES({user_id}, "{nickname}");
    '''.format(
        user_id=user_id,
        nickname=nickname,
    )
    await database.execute(sql)
    
    sql = '''
        UPDATE users
        SET user_id={user_id}, nickname="{nickname}"
        WHERE user_id LIKE {user_id};
    '''.format(
        user_id=user_id,
        nickname=nickname,
    )
    await database.execute(sql)

async def get_nickname(user_id):
    sql = '''
        SELECT nickname
        FROM users
        WHERE user_id == {user_id}
    '''.format(user_id=user_id)

    nickname = await database.fetch_one(sql)

    return nickname[0]

async def get_random():
    user_id = await database.fetch_one('''
        SELECT user_id
        FROM users
        ORDER BY RANDOM()
    ''')

    return user_id[0]

async def get_count(user_id):
    count = await database.fetch_one('''
        SELECT count
        FROM users
        WHERE user_id=={user_id}
    '''.format(user_id=user_id))

    return count[0]

async def inc_count(user_id):
    sql = '''
        UPDATE users
        SET count=count+1
        WHERE user_id LIKE {user_id};
    '''.format(
        user_id=user_id,
    )
    await database.execute(sql)

async def get_top():
    sql = '''
        SELECT nickname, count
        FROM users
        ORDER BY count DESC
    '''

    top = await database.fetch_all(sql)
    return top
