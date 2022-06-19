from abc import ABC, ABCMeta, abstractmethod

from libs.vk_api.orm_mode.types import *
from math import cos, sin
from enum import Enum

if __name__ == '__main__':
    vk_api = VkApiORM(
        access_token="vk1.a.vY03McmdPCJzq6KUwIvPgvSejvVnd2cLhZ4xqWN9PfouMUxA5Zt8-K-ja4Wg_gmzBM8lQUnFKc5gaMdTuUqzJX1NcMMi8KCxKKMfkDfDw9fyBo-K8YLcb_qC2_xE5_eC2MOfKi93QnRQJOb92p0D-flrctFScG1cBo-Gnc2llkZjSrAixuKlluX3oIOH53JO")
    group = vk_api.get_group_by_id(group_id="thecrypt0")
    list_of_user_objs = group.get_members(sort="id_asc", offset=0, all=False)
    list_of_users_group_obj = list()
    for user_obj in list_of_user_objs:
        try:
            time.sleep(1)
            list_of_user_group_obj = user_obj.get_groups()
        except (UserWasDeletedOrBanned, ProfileIsPrivate, YouDoNotHavePermissionToPerformThisAction):
            continue
        list_of_users_group_obj.extend(list_of_user_group_obj)

    similarity_groups = dict()
    for group_obj in list_of_users_group_obj:
        group_obj_id = group_obj.id
        for group_id in group_obj_id:
            if group_id not in similarity_groups:
                similarity_groups[group_id] = 1
            else:
                similarity_groups[group_id] += 1

    sorted_values = sorted(similarity_groups.values(), reverse=True)
    sorted_simalary_groups = {}
    for i in sorted_values:
        for k in similarity_groups.keys():
            if similarity_groups[k] == i:
                sorted_simalary_groups[k] = similarity_groups[k]

    print(sorted_simalary_groups)
