# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'user.access_token'
        db.delete_column('twitterApp_user', 'access_token')

        # Deleting field 'user.access_token_secret'
        db.delete_column('twitterApp_user', 'access_token_secret')

        # Adding field 'User.oauth_token'
        db.add_column('twitterApp_user', 'oauth_token',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'User.oauth_token_secret'
        db.add_column('twitterApp_user', 'oauth_token_secret',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)


        # Changing field 'User.twitter_id'
        db.alter_column('twitterApp_user', 'twitter_id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True))

    def backwards(self, orm):
        # Adding field 'user.access_token'
        db.add_column('twitterApp_user', 'access_token',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'user.access_token_secret'
        db.add_column('twitterApp_user', 'access_token_secret',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Deleting field 'User.oauth_token'
        db.delete_column('twitterApp_user', 'oauth_token')

        # Deleting field 'User.oauth_token_secret'
        db.delete_column('twitterApp_user', 'oauth_token_secret')


        # Changing field 'User.twitter_id'
        db.alter_column('twitterApp_user', 'twitter_id', self.gf('django.db.models.fields.DecimalField')(primary_key=True, decimal_places=0, max_digits=20))

    models = {
        'twitterApp.user': {
            'Meta': {'object_name': 'User'},
            'oauth_token': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'oauth_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'twitter_screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['twitterApp']