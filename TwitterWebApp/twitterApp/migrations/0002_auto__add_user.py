# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'user'
        db.create_table('twitterApp_user', (
            ('twitter_id', self.gf('django.db.models.fields.DecimalField')(primary_key=True, decimal_places=0, max_digits=20)),
            ('twitter_user_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=42)),
        ))
        db.send_create_signal('twitterApp', ['user'])


    def backwards(self, orm):
        # Deleting model 'user'
        db.delete_table('twitterApp_user')


    models = {
        'twitterApp.user': {
            'Meta': {'object_name': 'user'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'twitter_id': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '0', 'max_digits': '20'}),
            'twitter_user_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['twitterApp']