from libs.vk_api.connector.session import VkApi

vk_api = VkApi(access_token=str(input("Enter the your token: ")))
# vk_api.wall.post(owner_id=-212871717, message="Hello")
# vk_api.group.get_members(group_id=212871717, sort="time_asc", count=10,filter='managers')
# vk_api.group.get(user_id=352851907, count=0, extended=1, offset=0)
print(vk_api.wall.get(domain="we_use_django", count=5, filter='all'))



