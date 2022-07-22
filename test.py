import re
import sqlite3

from libs.vk_api.orm_mode.types import *
from db import models

if __name__ == '__main__':
    vk_api = VkApiORM(
        access_token="vk1.a.DX5AdLaeH0agUkRKQFtKHhVk_QrMHPO1BiX9eE78mFM9iVRz3yQoju7hBpc3TJgUXQ1_aEVx-muhqrbh8K7J9o-zs54DBr2cPRvhQFrkCll6BnWlS2GAQvuXcsMFKoqLeXXHuB5E1C-PROTk2Ps4xDT2dPYeSikhz5p1BKsHze5BKzFoB17afuOQF1yTLlp7")


    # group = vk_api.get_group_by_id(group_id="thecrypt0")
    # new_info = group.get_info(fields='discription')
    # y = group.get_count_of_member()
    # posts = vk_api.get_wall(owner_id=group.id)
    # new_info_by_post = posts.get_info(count=3)
    #
    #
    # def get_date_for_datebase(list_posts: list) -> List[tuple]:
    #     result = list(map(lambda post: tuple(
    #         (post.date, post.from_id, post.is_favorite, int(str(post.owner_id).replace('-', '')), post.post_type,
    #          post.comments, post.likes,
    #          post.reposts, post.views)
    #     ), list_posts))
    #     return result
    #
    #
    # # connect = sqlite3.connect('db/database_1.db')
    # # cursor = connect.cursor()
    # # cursor.execute("""CREATE TABLE IF NOT EXISTS groups(subsequence INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER,name TEXT,
    # # screen_name TEXT, is_closed INTEGER, type TEXT, photo50 BLOB,photo100 BLOB,photo200 BLOB, count_of_members INTEGER)""")
    # # cursor.execute("""INSERT INTO groups(id,name,screen_name,is_closed,type,photo50,photo100,photo200,
    # # count_of_members) VALUES(?,?,?,?,
    # # ?,?,?,?,?)""",
    # #                [new_info["id"],
    # #                 new_info["name"],
    # #                 new_info["screen_name"], new_info["is_closed"], new_info["type"], new_info["photo_50"],
    # #                 new_info["photo_100"], new_info["photo_200"], group.count_of_members])
    # #
    # # cursor.execute("""CREATE TABLE IF NOT EXISTS posts(subsequence INTEGER PRIMARY KEY AUTOINCREMENT, date INTEGER,
    # # from_id INTEGER, is_favorite TEXT, owner_id INTEGER, count_of_comments INTEGER, count_of_likes INTEGER,
    # # count_of_views INTEGER,count_of_reposts, post_type TEXT, FOREIGN KEY (owner_id) REFERENCES groups (id))""")
    # #
    # # for i in get_date_for_datebase(new_info_by_post):
    # #     cursor.execute("""INSERT INTO posts(date,from_id,is_favorite,owner_id,post_type,count_of_comments,
    # #     count_of_likes,count_of_reposts,count_of_views) VALUES (?,?,?,?,?,?,?,?,?)""", i)
    # # connect.commit()
    #
    #
    # # a = vk_api.get_post_obj(offset=1,count=3)
    # # for i in a:
    # #     print(i)
    #
    # a = models.PostsOBJ.objects.all()
    # print(a)


    # connect = sqlite3.connect('db/database_1.db')
    # cursor = connect.cursor()
    #
    # m = cursor.execute(f"SELECT * FROM posts")
    # print(m.fetchall())
