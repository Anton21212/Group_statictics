import sqlite3
from dataclasses import dataclass
from typing import List, Optional

from .groups import GroupOBJ

LIST_ = ['posts.date', 'posts.from_id', 'posts.is_favorite', 'posts.owner_id', 'posts.count_of_comments',
         'posts.count_of_likes',
         'posts.count_of_reposts', 'posts.post_type', 'posts.count_of_views']
LIST_A = ','.join(LIST_)


class PostOBJSList(list):
    @classmethod
    def __handle_db_requests(cls, db_request: str):
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        str_date_base = cursor.execute(db_request)
        all_date = str_date_base.fetchall()
        result = cls()
        for i in all_date:
            dict_date_base = dict(zip(LIST_, i))
            dict_general = {'posts': {}, 'group': {}}
            for key, value in dict_date_base.items():
                mod_key = key.split('.')[-1]
                if key.startswith('posts'):
                    dict_general['posts'][mod_key] = value
                else:
                    dict_general['group'][mod_key] = value
            new_post_obj = PostsOBJ(grouplink=GroupOBJ(**dict_general['group']),
                                    **dict_general['posts'])
            result.append(new_post_obj)

        return result

    @classmethod
    def all(cls):
        db_request = f"SELECT {LIST_A} FROM posts  JOIN groups ON posts.owner_id = groups.id"
        return cls.__handle_db_requests(db_request)

    @classmethod
    def get(cls, offset: int, count: int):
        db_request = f"SELECT {LIST_A} FROM posts  JOIN groups ON posts.owner_id = groups.id " \
                     f"WHERE posts.subsequence >= " \
                     f"{offset} ORDER BY posts.subsequence LIMIT {count}"
        return cls.__handle_db_requests(db_request)

    @classmethod
    def get_by_id(cls, id: int) -> Optional["PostsOBJ"]:
        db_request = f"SELECT {LIST_A} FROM posts  JOIN groups ON posts.owner_id = groups.id where {id}" \
                     f" = posts.subsequence"
        db_response = cls.__handle_db_requests(db_request)
        if db_response:
            result = db_response[0]
        else:
            result = None
        return result


@dataclass
class PostsOBJ:
    objects = PostOBJSList
    grouplink: "GroupOBJ"
    date: int = None,
    from_id: int = None,
    is_favorite: int = None,
    owner_id: int = None,
    count_of_comments: int = None,
    count_of_likes: int = None,
    count_of_views: int = None,
    count_of_reposts: int = None,
    post_type: str = None

    @staticmethod
    def create(date_: int = None, from_id_: int = None, is_favorite_: int = None, owner_id_: int = None,
               count_of_comments_: int = None, count_of_likes_: int = None, count_of_views_: int = None,
               count_of_reposts_: int = None, post_type_: str = None) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute(
            f"INSERT INTO posts (date, from_id, is_favorite, owner_id, count_of_comments, count_of_likes, count_of_views,count_of_reposts, post_type) values (?,?,?,?,?,?,?,?,?)",
            (date_, from_id_, is_favorite_, owner_id_,
             count_of_comments_, count_of_likes_,
             count_of_views_, count_of_reposts_, post_type_,))
        connect.commit()

    @staticmethod
    def update(new_values, id_: int, pols: str) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute(
            f"UPDATE posts SET {pols}={new_values} where subsequence = {id_}"
        )
        connect.commit()

    @staticmethod
    def delete(id_: int) -> None:
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        cursor.execute(
            f"DELETE from posts where subsequence = {id_}"
        )
        connect.commit()
