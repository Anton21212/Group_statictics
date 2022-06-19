import requests

from ..error_checking_decorator import check_vk_api_response_for_errors


class User:
    def __init__(self, access_token):
        self.access_token = access_token
        self.v = 5.131

    @check_vk_api_response_for_errors
    def get(self, user_ids: str, fields: str = None):
        """
        Возвращает расширенную информацию о пользователях.
        :param user_ids:
        :param fields:
        :return:
        """
        response = requests.post(
            url='https://api.vk.com/method/users.get',
            data={
                'access_token': self.access_token,
                'v': self.v,
                'user_ids': user_ids,
                'fields': fields,
            }
        )

        data = response.json()
        return data

    def get_subscriptions(self, user_id: int, count: int = None, extended: int = 0, offset: int = 0) -> dict:
        """
        Возвращает список идентификаторов пользователей и публичных страниц, которые входят в список подписок
        пользователя.
        :param user_id: Идентификатор пользователя, подписки которого необходимо получить.
        :param extended:1 – возвращает объединенный список, содержащий объекты group и user вместе.
        0 – возвращает список идентификаторов групп и пользователей отдельно (по умолчанию).
        :param offset: Смещение необходимое для выборки определенного подмножества подписок. Этот параметр
        используется только если передан extended=1.
        :count:Количество подписок, которые необходимо вернуть. Этот параметр используется только если передан
        extended=1.
        """
        response = requests.post(
            url='https://api.vk.com/method/users.getSubscriptions',
            data={
                'access_token': self.access_token,
                'v': self.v,
                'user_id': user_id,
                'extended': extended,
                'count': count,
                'offset': offset,
            }
        )

        data = response.json()
        return data
