from unittest import TestCase

from libs.vk_api.orm_mode.types import *


# class TestGroupsData(TestCase):
#     def test_get_data(self):
#         vk_api = VkApiORM(
#             access_token="vk1.a.DX5AdLaeH0agUkRKQFtKHhVk_QrMHPO1BiX9eE78mFM9iVRz3yQoju7hBpc3TJgUXQ1_aEVx-muhqrbh8K7J9o-zs54DBr2cPRvhQFrkCll6BnWlS2GAQvuXcsMFKoqLeXXHuB5E1C-PROTk2Ps4xDT2dPYeSikhz5p1BKsHze5BKzFoB17afuOQF1yTLlp7")
#         group = vk_api.get_group_by_id(group_id="thecrypt0")
#         new_info = group.get_info(fields='discription')
#         y = group.get_count_of_member()
#         posts = vk_api.get_wall(owner_id=group.id)
#         new_info_by_post = posts.get_info(count=3)
#
#         def get_date_for_datebase(list_posts: list) -> List[tuple]:
#             result = list(map(lambda post: tuple(
#                 (post.date, post.from_id, post.is_favorite, int(str(post.owner_id).replace('-', '')), post.post_type,
#                  post.comments, post.likes,
#                  post.reposts, post.views)
#             ), list_posts))
#             return result


