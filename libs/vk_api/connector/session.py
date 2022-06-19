from .methods import Wall, Group,User


class VkApi:
    def __init__(self, access_token):
        self.access_token = access_token
        self.wall = Wall(access_token=self.access_token)
        self.group = Group(access_token=self.access_token)
        self.user = User(access_token=self.access_token)
