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
        success INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        postponed INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        refused INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        invite_friend INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        transfer_abroad INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        mobile_bank INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        debit_card INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        credit_card INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        sim_card INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        investments INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        junior INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        subscription INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        card_protection INTEGER UNSIGNED DEFAULT 0 NOT NULL,
        FOREIGN KEY (user_id) REFERENCES bot_user (id) 
    );
'''

GET_ALL_USER_IDS = '''
    SELECT id
    FROM bot_user;
'''
