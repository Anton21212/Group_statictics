import requests

from ..error_checking_decorator import check_vk_api_response_for_errors


class Wall:
    def __init__(self, access_token):
        self.access_token = access_token
        self.v = 5.131

    @check_vk_api_response_for_errors
    def post(self, owner_id: int, message: str, friends_only: int = 0, from_group: int = 0) -> dict:
        """
        Позволяет создать запись на стене

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param message: Текст сообщения.
        :param friends_only: 1 — запись будет доступна только друзьям, 0 — всем пользователям.
        По умолчанию публикуемые записи доступны всем пользователям.
        :param from_group: Данный параметр учитывается, если owner_id < 0 (запись публикуется на стене группы).
        1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя (по умолчанию).
        """

        response = requests.post(
            url='https://api.vk.com/method/wall.post',
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'friends_only': friends_only,
                'from_group': from_group,
                'message': message,
            }
        )

        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def check_copyright_link(self, link: str) -> dict:
        """
        Проверка ссылки для указания источника

        :param link: Ссылка на источник. Поддерживаются внешние и внутренние ссылки.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.checkCopyrightLink",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'link': link,
            })
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def close_comments(self, owner_id: int, post_id: int) -> dict:
        """
        Выключает комментирование записи

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.closeComments",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            })
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def create_comment(self, owner_id: int, post_id: int, message: str, reply_to_comment: int, *,
                       sticker_id: int = None) -> dict:
        """
        Создание коммента к записи

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        :param message: Текст комментария
        :param reply_to_comment: Идентификатор комментария, в ответ на который должен быть добавлен новый комментарий.
        :param sticker_id: Идентификатор стикера.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.createComment",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
                'message': message,
                "reply_to_comment": reply_to_comment,
                "sticker_id": sticker_id

            })
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def delete(self, owner_id: int, post_id: int) -> dict:
        """
        Удаляет запись со стены.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.delete",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def delete_comment(self, owner_id: int, comment_id: int) -> dict:
        """
        Удаляет комментарий к записи на стене.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param comment_id: Идентификатор комментария.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.deleteComment",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'comment_id': comment_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def edit(self, owner_id: int, post_id: int, friends_only: int, message: str, close_comments: int) -> dict:
        """
        Редактирует запись на стене.


        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        :param friends_only: 1 — запись будет доступна только друзьям, 0 — всем пользователям.
        :param message: Текст сообщения
        :param close_comments: 1 — комментарии к записи отключены, 0 — комментарии к записи включены.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.edit",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
                'friends_only': friends_only,
                'message': message,
                'close_comments': close_comments,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def edit_comment(self, owner_id: int, comment_id: int, message: str) -> dict:
        """
        Редактирует комментарий на стене.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param comment_id: Идентификатор комментария, который необходимо отредактировать.
        :param message: Новый текст комментария.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.editComment",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'comment_id': comment_id,
                'message': message,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def get(self, count: int, filter: str = None, *, offset: int = None, domain: str = None,
            owner_id: int = None) -> dict:
        """
        Возвращает список записей со стены пользователя или сообщества.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param count: Количество записей, которое необходимо получить. Максимальное значение: 100.
        :param filter: Определяет, какие типы записей на стене необходимо получить. Возможные значения:
        •owner — записи владельца стены;
        •others — записи не от владельца стены;
        •all — все записи на стене (owner + others).
        :param offset: Смещение, необходимое для выборки определённого подмножества записей.
        :param domain: Короткий адрес пользователя или сообщества.
        """

        response = requests.get(
            url="https://api.vk.com/method/wall.get",
            params={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'count': count,
                'filter': filter,
                'offset': offset,
                'domain': domain,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def get_by_id(self, posts: tuple[int]) -> dict:
        """
        Возвращает список записей со стен пользователей или сообществ по их идентификаторам.

        :param posts: Перечисленные через запятую идентификаторы, которые представляют собой идущие через знак подчеркивания
        ID владельцев стен и ID самих записей на стене. Максимум 100 идентификаторов.
        Пример значения posts: 93388_21539,93388_20904,-1_340364.
        """

        response = requests.get(
            url="https://api.vk.com/method/wall.getById",
            params={
                'access_token': self.access_token,
                'v': self.v,
                'posts': posts,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def get_comment(self, owner_id: int, comment_id: int) -> dict:
        """
        Получает информацию о комментарии на стене.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param comment_id: Идентификатор комментария.
        """

        response = requests.get(
            url="https://api.vk.com/method/wall.getComment",
            params={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'comment_id': comment_id,

            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def get_comments(self, owner_id: int, post_id: int, sort: str, start_comment_id: int, comment_id: int, *,
                     count: int = 10,
                     offset: int = None,
                     need_likes: int = 0) -> dict:
        """
        Возвращает список комментариев к записи на стене.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        :param need_likes: 1 — возвращать информацию о лайках, по умолчанию - 0.
        :param offset: Сдвиг, необходимый для получения конкретной выборки результатов.
        :param count: Число комментариев, которые необходимо получить. По умолчанию: 10, максимальное значение: 100.
        :param sort: Порядок сортировки комментариев. Возможные значения:
        •asc — от старых к новым;
        •desc — от новых к старым.
        :param comment_id: Идентификатор комментария, ветку которого нужно получить.
        :param start_comment_id: Идентификатор комментария, начиная с которого нужно вернуть список
        """

        response = requests.get(
            url="https://api.vk.com/method/wall.getComments",
            params={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
                'need_likes': need_likes,
                'offset': offset,
                'count': count,
                'sort': sort,
                'comment_id': comment_id,
                'start_comment_id': start_comment_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def get_reposts(self, owner_id: int, post_id: int, count: int, *, offset: int = None) -> dict:
        """
        Позволяет получать список репостов заданной записи.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        :param count: Количество записей, которое необходимо получить.
        :param offset: Смещение, необходимое для выборки определенного подмножества записей.
        """

        response = requests.get(
            url="https://api.vk.com/method/wall.getReposts",
            params={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
                'count': count,
                'offset': offset,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def open_comments(self, owner_id: int, post_id: int) -> dict:
        """
        Включает комментирование записи

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.openComments",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def pin(self, owner_id: int, post_id: int) -> dict:
        """
        Закрепляет запись на стене (запись будет отображаться выше остальных).

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.pin",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def report_comment(self, owner_id: int, comment_id: int, reason: int) -> dict:
        """
        Позволяет пожаловаться на комментарий к записи.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param comment_id: Идентификатор комментария.
        :param reason: Причина жалобы:
        •0 — спам;
        •1 — детская порнография;
        •2 — экстремизм;
        •3 — насилие;
        •4 — пропаганда наркотиков;
        •5 — материал для взрослых;
        •6 — оскорбление;
        •8 — призывы к суициду.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.reportComment",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'comment_id': comment_id,
                'reason': reason,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def report_post(self, owner_id: int, post_id: int, reason: int) -> dict:
        """
        Позволяет пожаловаться на запись

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи.
        :param reason: Причина жалобы:
        •0 — спам;
        •1 — детская порнография;
        •2 — экстремизм;
        •3 — насилие;
        •4 — пропаганда наркотиков;
        •5 — материал для взрослых;
        •6 — оскорбление;
        •8 — призывы к суициду.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.reportPost",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
                'reason': reason,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def repost(self, object: str, message: str, group_id: id, *, mark_as_ads: int = 0) -> dict:
        """
        Копирует объект на стену пользователя или сообщества.

        :param object: Строковый идентификатор объекта, который необходимо разместить на стене, например, wall66748_3675
        или wall-1_340364.Формируется из типа объекта (wall, photo, video и т.п.), идентификатора владельца объекта и
        идентификатора самого объекта.
        :param message: Сопроводительный текст, который будет добавлен к записи с объектом.
        :param group_id: Идентификатор сообщества, на стене которого будет размещена запись с объектом.
        Если не указан, запись будет размещена на стене текущего пользователя.
        :param mark_as_ads: 1 — пометить запись как рекламную, по умолчанию - 0.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.repost",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'object': object,
                'message': message,
                'group_id': group_id,
                'mark_as_ads': mark_as_ads,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def restore(self, owner_id: int, post_id: int) -> dict:
        """
        Восстанавливает удалённую запись на стене пользователя или сообщества.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        :return:
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.restore",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def restore_comment(self, owner_id: int, comment_id: int) -> dict:
        """
        Восстанавливает удаленный комментарий к записи на стене.


        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param comment_id: Идентификатор комментария на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.restoreComment",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'comment_id': comment_id,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def search(self, owner_id: int, query: str, *, domain: str, count: int = 20, owners_only: int = 0,
               offset: int = None) -> dict:
        """
        Позволяет искать записи на стене в соответствии с заданными критериями.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param query: Поисковой запрос. Для точного результата запрос необходимо передавать в двойных кавычках.
        :param owners_only: 1 — возвращать только записи от имени владельца стены, по умолчанию - 0.
        :param count: Количество записей, которые необходимо вернуть. Положительное число, по умолчанию  — 20,
        максимальное значение 100.
        :param offset: Смещение, необходимо для получения определенного подмножества результатов.
        :param domain: Короткий адрес пользователя или сообщества.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.search",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'query': query,
                'owners_only': owners_only,
                'offset': offset,
                'count': count,
                'domain': domain,
            }
        )
        data = response.json()
        return data

    @check_vk_api_response_for_errors
    def unpin(self, owner_id: int, post_id: int) -> dict:
        """
        Отменяет закрепление записи на стене.

        :param owner_id: Идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись.
        Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком «-».
        :param post_id: Идентификатор записи на стене.
        """

        response = requests.post(
            url="https://api.vk.com/method/wall.unpin",
            data={
                'access_token': self.access_token,
                'v': self.v,
                'owner_id': owner_id,
                'post_id': post_id,
            }
        )
        data = response.json()
        return data
