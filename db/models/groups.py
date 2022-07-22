import sqlite3
from dataclasses import dataclass

from typing import Union

LIST_ = ['groups.id', 'groups.name',
         'groups.screen_name',
         'groups.is_closed',
         'groups.type', 'groups.photo50', 'groups.photo100', 'groups.photo200', 'groups.count_of_members']
LIST_A = ','.join(LIST_)


class GroupOBJSList(list):
    @classmethod
    def __handle_db_requests(cls, db_request):
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        str_date_base = cursor.execute(db_request)
        all_date = str_date_base.fetchall()
        result = cls()
        dict_general = {'group': {}}
        for i in all_date:
            dict_date_base = dict(zip(LIST_, i))
            for key, value in dict_date_base.items():
                mod_key = key.split('.')[-1]
                if key.startswith('group'):
                    dict_general['group'][mod_key] = value
            new_post_obj = GroupOBJ(**dict_general['group'])
            result.append(new_post_obj)
        return result

    @classmethod
    def all(cls):
        db_request = f"SELECT {LIST_A} FROM groups"
        return cls.__handle_db_requests(db_request)

    @classmethod
    def get_by_subsequence(cls, subsequence: int) -> str:
        db_request = f"SELECT {LIST_A} FROM groups where subsequence = {subsequence}"
        db_response = cls.__handle_db_requests(db_request)
        if db_response:
            result = db_response[0]
        else:
            result = None
        return result


@dataclass
class GroupOBJ:
    objects = GroupOBJSList
    id: int = None,
    name: str = None,
    screen_name: str = None,
    is_closed: int = None,
    type: str = None,
    photo50: str = None,
    photo100: str = None,
    photo200: str = None,
    count_of_members: int = None,

    @staticmethod
    def create(id_: int = None, name_: str = None, screen_name_: str = None,
               is_closed_: int = None,
               type_: str = None, photo50_: str = None, photo100_: str = None,
               photo200_: str = None, count_of_members_: int = None) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute("INSERT INTO groups (id, name, screen_name, is_closed, type, photo50, photo100, photo200, "
                       "count_of_members) VALUES (?,?,?,?,?,?,?,?,?)", (id_, name_, screen_name_, is_closed_, type_,
                                                                        photo50_, photo100_, photo200_,
                                                                        count_of_members_,))
        connect.commit()

    @staticmethod
    def update(pols: str, new_values: Union[str, int], subsequence: int) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute(f"UPDATE groups SET {pols}={new_values} where subsequence = {subsequence}")
        connect.commit()



    @staticmethod
    def delete(subsequence: int) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM groups where subsequence = {subsequence}")
        connect.commit()
