import math
import time
from typing import List, Union

from ..connector.session import VkApi
from ..connector.errors import *


class GroupORM:
    def __init__(
            self,
            session: "VkApiORM",
            id: Union[str, int] = None,
            name: str = None,
            screen_name: str = None,
            is_closed: int = None,
            type: str = None,
            photo_50: str = None,
            photo_100: str = None,
            photo_200: str = None,
            count_of_members: int = None,
            count: int = None,

    ):
        self.count = count
        self.id = id
        self.name = name
        self.screen_name = screen_name
        self.is_closed = is_closed
        self.type = type
        self.photo_50 = photo_50
        self.photo_100 = photo_100
        self.photo_200 = photo_200
        self.count_of_members = count_of_members
        self.session = session

    def get_info(self) -> None:
        response = self.session.connector.group.get_by_id(group_id=str(self.id))
        info = response['response'][0]
        for key, value in info.items():
            setattr(self, key, value)

    def get_count_of_member(self) -> int:
        """
        Запрос на получение 0 подписчиков, в ответе нам приходит их количество и пустой список
        """
        response = self.session.connector.group.get_members(group_id=self.id)
        self.count_of_members = response['items']['count']

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
            from_id: int = None,
            owner_id: int = None,
            date: int = None,
            marked_as_ads: int = None,
            is_favorite: bool = None,
            post_type: str = None,
            text: str = None,
            comments: object = None,
            likes: object = None,
            reposts: object = None,
            views: object = None,
            donut: object = None,
            is_pinned: int = None,
            count: int = None,
            domain: str = None,
    ):
        self.from_id = from_id
        self.session = session
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
        self.donut = donut
        self.is_pinned = is_pinned
        self.count = count
        self.domain = domain

    def __str__(self):
        return f"owner_id={self.owner_id}, domain = {self.domain}"

    def open_comments(self) -> None:
        self.session.connector.wall.open_comments(owner_id=self.owner_id, post_id=self.post)

    def post(self, message: str) -> None:
        self.session.connector.wall.post(owner_id=self.owner_id, message=message)

    def get_info(self):
        response = self.session.connector.wall.get(domain=str(self.domain), count=self.count)
        info = response['response']['items']
        for i in info:
            for key, value in i.items():
                setattr(self, key, value)


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
        :param domain:
        :param owner_id:
        :return:
        """
        return WallORM(session=self, domain=domain, owner_id=owner_id)
