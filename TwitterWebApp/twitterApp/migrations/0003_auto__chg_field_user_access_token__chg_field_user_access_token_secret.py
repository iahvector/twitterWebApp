# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'user.access_token'
        db.alter_column('twitterApp_user', 'access_token', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'user.access_token_secret'
        db.alter_column('twitterApp_user', 'access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=60))

    def backwards(self, orm):

        # Changing field 'user.access_token'
        db.alter_column('twitterApp_user', 'access_token', self.gf('django.db.models.fields.CharField')(max_length=48))

        # Changing field 'user.access_token_secret'
        db.alter_column('twitterApp_user', 'access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=42))

    models = {
        'twitterApp.user': {
            'Meta': {'object_name': 'user'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'twitter_id': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '0', 'max_digits': '20'}),
            'twitter_user_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['twitterApp']