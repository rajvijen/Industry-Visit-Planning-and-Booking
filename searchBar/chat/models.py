from django.db import models
# Adding user authentication
from django.contrib.auth.models import User

class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id

#//New
# class Chat(models.Model):
#     user = models.ForeignKey(User,on_delete =models.CASCADE)
#     # group = models.ForeignKey(Room,on_delete =models.CASCADE)  //it's for chat in group
#     body = models.CharField(max_length = 50)
#     time = models.DateTimeField()
#     def json(self):
#         return {
#             'user' : self.user,
#             # 'group' : self.group,
#             'body' : self.body,
#         }
        