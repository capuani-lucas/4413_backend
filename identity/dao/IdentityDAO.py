from django.contrib.auth.models import User

class IdentityDAO():

  def create_user(self, username, password):
    user = User.objects.create_user(
      username=username,
      email=username,
      password=password
    )
    return user
