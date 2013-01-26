# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'user.twitter_user_name'
        db.delete_column('twitterApp_user', 'twitter_user_name')

        # Adding field 'user.twitter_screen_name'
        db.add_column('twitterApp_user', 'twitter_screen_name',
                      self.gf('django.db.models.fields.CharField')(default=' ', unique=True, max_length=15),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'user.twitter_user_name'
        db.add_column('twitterApp_user', 'twitter_user_name',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=15, unique=True),
                      keep_default=False)

        # Deleting field 'user.twitter_screen_name'
        db.delete_column('twitterApp_user', 'twitter_screen_name')


    models = {
        'twitterApp.user': {
            'Meta': {'object_name': 'user'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'twitter_id': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '0', 'max_digits': '20'}),
            'twitter_screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['twitterApp']