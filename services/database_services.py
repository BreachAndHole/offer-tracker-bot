from config import queries
from database import execute_query, execute_read_query
from structures import DailyResult


def get_all_user_ids() -> list[int]:
    query_result = execute_read_query(queries.GET_ALL_USER_IDS)
    ids = [user_id for user_id, in query_result]
    return ids


def user_is_in_database(user_id: int) -> bool:
    user_ids = get_all_user_ids()
    return user_id in user_ids


def add_user_to_database(user_id: int) -> bool:
    """ Adding user to database. Return True if it's a new user """
    if user_is_in_database(user_id):
        return False

    query = f'''
        INSERT INTO result (user_id)
        VALUES ({user_id});
    '''
    execute_query(query)
    return True


def get_user_result(user_id: int) -> DailyResult:
    if not user_is_in_database(user_id):
        add_user_to_database(user_id)
    query = f'''
        SELECT 
            success, postponed, refused, 
            invite_friend, transfer_abroad, mobile_bank,
            debit_card, credit_card, sim_card,
            investments, junior, subscription,
            card_protection
        FROM result
        WHERE user_id == {user_id}  
    '''
    query_result = execute_read_query(query)[0]
    daily_result = DailyResult(
        success=query_result[0],
        postponed=query_result[1],
        refused=query_result[2],
        invite_friend=query_result[3],
        transfer_abroad=query_result[4],
        mobile_bank=query_result[5],
        debit_card=query_result[6],
        credit_card=query_result[7],
        sim_card=query_result[8],
        investments=query_result[9],
        junior=query_result[10],
        subscription=query_result[11],
        card_protection=query_result[12],
    )
    return daily_result


def change_result_field(user_id: int, field_name: str, is_increment: bool):
    if is_increment:
        query = f'''
            UPDATE result 
            SET {field_name} = {field_name} + 1
            WHERE user_id == {user_id};
        '''
    else:
        # Checking if value is not positive
        get_field_value_query = f'SELECT {field_name} FROM result WHERE user_id == {user_id};'
        field_value = execute_read_query(get_field_value_query)[0][0]
        if field_value <= 0:
            return

        query = f'''
            UPDATE result 
            SET {field_name} = {field_name} - 1
            WHERE user_id == {user_id};
        '''
    execute_query(query)


def reset_user_result(user_id: int):
    query = f'''
        UPDATE result
        SET
            success = 0,
            postponed = 0,
            refused = 0,
            invite_friend = 0,
            transfer_abroad = 0,
            mobile_bank = 0,
            debit_card = 0,
            credit_card = 0,
            sim_card = 0,
            investments = 0,
            junior = 0,
            subscription = 0,
            card_protection = 0
        WHERE user_id == {user_id};       
    '''
    execute_query(query)
