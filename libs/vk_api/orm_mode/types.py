import math
import sqlite3
import time
from typing import List, Union

from ..connector.session import VkApi
from ..connector.errors import *

LIST_ = ['posts.date', 'posts.from_id', 'posts.is_favorite', 'posts.owner_id', 'posts.count_of_comments',
         'posts.count_of_likes',
         'posts.count_of_reposts', 'posts.post_type', 'posts.count_of_views', 'groups.id', 'groups.name',
         'groups.screen_name',
         'groups.is_closed',
         'groups.type', 'groups.photo50', 'groups.photo100', 'groups.photo200', 'groups.count_of_members']
LIST_A = ','.join(LIST_)


class GroupORM:
    def __init__(
            self,
            session: "VkApiORM",
            id: Union[str, int] = None,
            name: str = None,
            screen_name: str = None,
            is_closed: int = None,
            type: str = None,
            photo50: str = None,
            photo100: str = None,
            photo200: str = None,
            count_of_members: int = None,
            count: int = None,

    ):
        self.count = count
        self.id = id
        self.name = name
        self.screen_name = screen_name
        self.is_closed = is_closed
        self.type = type
        self.photo50 = photo50
        self.photo100 = photo100
        self.photo200 = photo200
        self.count_of_members = count_of_members
        self.session = session

    def get_info(self, fields) -> None:
        response = self.session.connector.group.get_by_id(group_id=str(self.id), fields=fields)
        info = response['response'][0]
        for key, value in info.items():
            setattr(self, key, value)
        return info

    def get_count_of_member(self) -> int:
        """
        Запрос на получение 0 подписчиков, в ответе нам приходит их количество и пустой список
        """
        response = self.session.connector.group.get_members(group_id=self.id)
        self.count_of_members = response['response']['count']

    def get_members(self, sort: str, offset: int, count: int = None, all: bool = False) -> List["UserORM"]:
        """
        Если передали all, тогда достаем всех подсписчиков начиная с offset.
        Если offset больше чем число подписчиков в группе, то выдаем пустой список


        Если количество меньше либо равна 1000, то можем достать подписчиков в один запрос,
        если количество больше то делим количество на 1000 и округляем до большего целого значения, таким образом
        получим необходимое количество запросов.

        count = 2100
        Количество запросов = 2100/1000 = 2,1, округляем в большую сторону до ближайшего целого числа = 3

        """
        full_list_user_objs = list()
        number_request = 0
        if all == True:
            count_all_request = math.ceil(self.count_of_members / 1000)
            if offset > count_all_request:
                return list()
            while number_request != count_all_request:
                response = self.session.connector.group.get_members(
                    group_id=self.id, sort=sort,
                    offset=offset
                )
                time.sleep(1)
                number_request += 1
                list_of_user_objs = [
                    UserORM(session=self.session, id=user_id) for user_id in
                    response['response']['items']]
                full_list_user_objs.extend(list_of_user_objs)
            return full_list_user_objs
        else:
            if count != None and count > 1000:
                count_request = count / 1000
                request = round(count_request)
                ostatok_request = round((count_request - request) * 1000)
                count_ostatok_request = math.ceil(ostatok_request / 1000)

                all_count_request = request + count_ostatok_request

                while number_request != all_count_request:
                    if count >= 1000:
                        while count >= 1000:
                            response_id_member_by_group = self.session.connector.group.get_members(
                                group_id=self.id,
                                sort=sort,
                                offset=offset,
                                count=1000
                            )

                            list_of_user_objs_by_group = [
                                UserORM(session=self.session, id=user_id) for user_id in
                                response_id_member_by_group
                                ['response']['items']]

                            full_list_user_objs.extend(list_of_user_objs_by_group)

                            number_request += 1
                            count = count - 1000
                            time.sleep(1)
                    if ostatok_request >= 1 and ostatok_request <= 999:
                        response = self.session.connector.group.get_members(
                            group_id=self.id, sort=sort,
                            offset=offset, count=ostatok_request
                        )
                        list_of_user_objs = [
                            UserORM(session=self.session, id=user_id) for user_id in
                            response['response']['items']]

                        full_list_user_objs.extend(list_of_user_objs)
                        number_request += 1

                return full_list_user_objs
            else:
                response = self.session.connector.group.get_members(group_id=self.id, count=count, sort=sort,
                                                                    offset=offset)
                list_of_user_objs = [UserORM(session=self.session, id=user_id) for user_id in response['response'][
                    'items']]
                full_list_user_objs.extend(list_of_user_objs)
                return full_list_user_objs


class UserORM:
    def __init__(
            self,
            session: "VkApiORM",
            id: int,
            first_name: str = None,
            last_name: str = None,
            about: str = None,
            is_closed: bool = None,
            can_access_closed: bool = None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.can_access_closed = can_access_closed
        self.is_closed = is_closed
        self.session = session

    def __str__(self):
        return f"id={self.id}, first_name={self.first_name}, last_name={self.last_name}, about={self.about}"

    def get_info(self) -> None:
        response = self.session.connector.user.get(user_ids=str(self.id))
        info = response['response'][0]
        for key, value in info.items():
            setattr(self, key, value)

    def get_groups(self) -> List[GroupORM]:
        """
        У вк есть метод для получения групп пользователя, а так-же метод для получения его подписок.
        Группы делятся на 2 вида: группа, паблик(публичная страница).
        Группы достаются из метода для получения групп.
        Публичные страницы из метода для получения подписок.
        Метод для получения подписок выдает не только публичные страницы, но и страницы пользователя на которые он
        подписан.
        Данные метод должен получать и группы, и паблики, при этом при использовании метода для получения подписок
        пользователя должен игнорировать все кроме пабликов(страницы других пользователь на которые подписан и т.д)

        Выдаваемые объекты должны иметь информацию об id и сессии.
        """
        full_list_groups_by_users_objs = list()
        response_group = self.session.connector.group.get(user_id=self.id)
        list_groups_by_user_objs = [
            GroupORM(session=self.session, id=response_group['response']['items'], count=response_group[
                'response']['count'])]
        full_list_groups_by_users_objs.extend(list_groups_by_user_objs)
        response_subscriptions = self.session.connector.user.get_subscriptions(user_id=self.id)
        for i in response_subscriptions['response']['users']['items']:
            for k in response_group['response']['items']:
                if i == k:
                    i.remove(response_subscriptions['response']['users']['items'])
        list_subscriptions_by_user_objs = [
            GroupORM(session=self.session, id=response_subscriptions['response']['users']['items'])]

        full_list_groups_by_users_objs.extend(list_subscriptions_by_user_objs)
        return full_list_groups_by_users_objs


class WallORM:
    def __init__(
            self,
            session: "VkApiORM",
            owner_id: int = None,
            domain: str = None,
    ):
        self.session = session
        self.owner_id = owner_id
        self.domain = domain

    def __str__(self):
        return f"owner_id={self.owner_id}, domain = {self.domain}"

    def open_comments(self) -> None:
        self.session.connector.wall.open_comments(owner_id=self.owner_id, post_id=self.post)

    def post(self, message: str) -> None:
        self.session.connector.wall.post(owner_id=self.owner_id, message=message)

    def get_info(self, count: int) -> "PostORM":
        response = self.session.connector.wall.get(owner_id=self.owner_id, count=count)
        info = response['response']['items']
        list_subscriptions_by_user_objs = [
            PostORM(session=self.session, owner_id=value['owner_id'],
                    date=value['date'], from_id=value['from_id'], marked_as_ads=value['marked_as_ads'],
                    is_favorite=value['is_favorite'], post_type=value['post_type'], text=value['text'],
                    comments=value['comments']['count'], likes=value['likes']['count'], reposts=value['reposts'][
                    'count'],
                    views=value[
                        'views']['count'],
                    ) for value in info

        ]
        return list_subscriptions_by_user_objs


class PostOBJSList(list):
    @classmethod
    def get_post_obj(cls, offset: int, count: int) -> "PostsOBJ":
        connect = sqlite3.connect('db/database_1.db')
        cursor = connect.cursor()
        str_date_base = cursor.execute(
            f"SELECT {LIST_A} FROM posts  JOIN groups ON posts.owner_id = groups.id  WHERE  "
            f"posts.subsequence >="
            f" {offset} ORDER BY posts.subsequence LIMIT {count}")
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

    def get_owner_ids(self):
        self: List[PostsOBJ]
        result = []
        for i in self:
            result.append(i.owner_id)
        return result


class PostORM:

    def __init__(
            self,
            session: "VkApiORM",
            from_id: int = None,
            owner_id: int = None,
            date: int = None,
            marked_as_ads: int = None,
            is_favorite: bool = None,
            post_type: str = None,
            text: str = None,
            comments: int = None,
            likes: int = None,
            reposts: int = None,
            views: object = None,
            score: int = None

    ):
        self.session = session
        self.from_id = from_id
        self.owner_id = owner_id
        self.date = date
        self.marked_as_ads = marked_as_ads
        self.is_favorite = is_favorite
        self.post_type = post_type
        self.text = text
        self.comments = comments
        self.likes = likes
        self.reposts = reposts
        self.views = views
        self.score = score

    def __str__(self):
        return f" {self.date} {self.text} {self.owner_id} {self.from_id}"


class GroupOBJ:
    def __init__(
            self,
            id: int = None,
            name: str = None,
            screen_name: str = None,
            is_closed: int = None,
            type: str = None,
            photo50: str = None,
            photo100: str = None,
            photo200: str = None,
            count_of_members: int = None,
    ):
        self.id = id
        self.name = name
        self.screen_name = screen_name
        self.is_closed = is_closed
        self.type = type
        self.photo50 = photo50
        self.photo100 = photo100
        self.photo200 = photo200
        self.count_of_members = count_of_members


class PostsOBJ:

    def __init__(
            self,
            grouplink: "GroupOBJ",
            date: int = None,
            from_id: int = None,
            is_favorite: int = None,
            owner_id: int = None,
            count_of_comments: int = None,
            count_of_likes: int = None,
            count_of_views: int = None,
            count_of_reposts: int = None,
            post_type: str = None

    ):
        self.grouplink = grouplink
        self.date = date
        self.from_id = from_id
        self.is_favorite = is_favorite
        self.owner_id = owner_id
        self.count_of_comments = count_of_comments,
        self.count_of_likes = count_of_likes,
        self.count_of_views = count_of_views
        self.count_of_reposts = count_of_reposts
        self.post_type = post_type

    def __str__(self):
        return f" date: {self.date}"

    def __repr__(self):
        return self.__str__()


class VkApiORM:
    def __init__(self, access_token):
        self.access_token = access_token
        self.connector = VkApi(access_token=access_token)

    def get_group_by_id(self, group_id: int) -> GroupORM:
        return GroupORM(session=self, id=group_id)

    def get_user_by_id(self, user_id: int) -> UserORM:
        return UserORM(session=self, id=user_id)

    def get_wall(self, domain: str = None, owner_id: int = None) -> WallORM:
        """
        Выдает объект стены.

        * Передать что-то одно, либо domain, либо owner_id
        """
        return WallORM(session=self, domain=domain, owner_id=-owner_id)

