CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS bot_user (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30)
    );
'''

CREATE_RESULT_TABLE = '''
    CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        success INTEGER DEFAULT 0 NOT NULL,
        postponed INTEGER DEFAULT 0 NOT NULL,
        canceled INTEGER DEFAULT 0 NOT NULL,
        invite_friend INTEGER DEFAULT 0 NOT NULL,
        transfer_abroad INTEGER DEFAULT 0 NOT NULL,
        mobile_bank INTEGER DEFAULT 0 NOT NULL,
        debit_card INTEGER DEFAULT 0 NOT NULL,
        credit_card INTEGER DEFAULT 0 NOT NULL,
        sim_card INTEGER DEFAULT 0 NOT NULL,
        investments INTEGER DEFAULT 0 NOT NULL,
        junior INTEGER DEFAULT 0 NOT NULL,
        subscription INTEGER DEFAULT 0 NOT NULL,
        FOREIGN KEY (user_id) REFERENCES bot_user (id) 
    );
'''

GET_ALL_USER_IDS = '''
    SELECT id
    FROM bot_user;
'''
