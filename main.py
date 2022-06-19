# import time
#
# from libs.vk_api.connector.example.example import vk_api
# from libs.vk_api import ProfileIsPrivate, ThePageHasBeenRemovedOrBlocked
#
#
# class Info:
#     def __init__(self):
#         self.statistic_group = {}
#
#     def get_member(self):
#         """
#         Возвращает список участников сообщества
#         """
#
#         a = vk_api.group.get_members("python_community", "id_asc", count=10)
#         return a
#
#     def get_id_members(self):
#         s = []
#         for i in self.get_member()["response"]["items"]:
#             s.append(i)
#         return s
#
#     def get_group_members(self):
#         m = []
#         for i in self.get_id_members():
#             try:
#                 b = vk_api.group.get(i, count=0, extended=0)
#                 time.sleep(1)
#             except (ProfileIsPrivate, ThePageHasBeenRemovedOrBlocked):
#                 continue
#             else:
#                 m.append(b['response']["items"])
#         return m
#
#     def get_group(self):
#         for i in self.get_group_members():
#             for r in i:
#                 if r not in self.statistic_group:
#                     self.statistic_group[r] = 1
#                 else:
#                     self.statistic_group[r] += 1
#
#     def sorted_statistic_group(self):
#         self.get_group()
#         sorted_values = sorted(self.statistic_group.values(), reverse=True)
#         sorted_dict = {}
#         for i in sorted_values:
#             for k in self.statistic_group.keys():
#                 if self.statistic_group[k] == i:
#                     sorted_dict[k] = self.statistic_group[k]
#         print(self.statistic_group)
#
#     def get_info_groups(self):
#         info_group = []
#         for i in self.sorted_statistic_group():
#             try:
#                 info = vk_api.group.get_by_id(i, fields="description")
#                 time.sleep(1)
#             except:
#                 continue
#             else:
#                 info_group.append(info)
#         return info_group
#
#
# if __name__ == '__main__':
#     a = Info().sorted_statistic_group()

class UserORM:
    def __init__(self, items, count, session):
        self.users_id = items
        self.count_users = count
        self.session = session

        self.dictionary_groups = {}

    def get_groups(self, count):
        for user_id in self.users_id:
            try:
                get_obj = self.session.get_group(user_id=user_id, count=count)
                time.sleep(1)
            except (ProfileIsPrivate, ThePageHasBeenRemovedOrBlocked):
                continue
            else:
                yield get_obj

    def add_dictionary_from_groups(self):
        for i in self.users_id:
            if i not in self.dictionary_groups:
                self.dictionary_groups[i] = 1
            else:
                self.dictionary_groups[i] += 1
        print(self.dictionary_groups)