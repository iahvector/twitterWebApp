from django.db import models

# Create your models here.
class User(models.Model):

    twitter_id = models.BigIntegerField(primary_key=True)
    twitter_screen_name = models.CharField(unique=True, max_length=15)
    oauth_token = models.CharField(max_length=60)
    oauth_token_secret = models.CharField(max_length=60)

    def __unicode__(self):
        return "Twitter ID: " + self.twitter_id + ", Twitter user name: " + self.twitter_user_name
