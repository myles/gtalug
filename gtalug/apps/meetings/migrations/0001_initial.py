
from south.db import db
from django.db import models
from gtalug.apps.meetings.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Meeting'
        db.create_table('meetings', (
            ('id', orm['meetings.Meeting:id']),
            ('topic', orm['meetings.Meeting:topic']),
            ('slug', orm['meetings.Meeting:slug']),
            ('date', orm['meetings.Meeting:date']),
            ('time', orm['meetings.Meeting:time']),
            ('tba', orm['meetings.Meeting:tba']),
            ('tease', orm['meetings.Meeting:tease']),
            ('body', orm['meetings.Meeting:body']),
            ('presenter', orm['meetings.Meeting:presenter']),
            ('presenter_user', orm['meetings.Meeting:presenter_user']),
            ('date_added', orm['meetings.Meeting:date_added']),
            ('date_modified', orm['meetings.Meeting:date_modified']),
        ))
        db.send_create_signal('meetings', ['Meeting'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Meeting'
        db.delete_table('meetings')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'meetings.meeting': {
            'Meta': {'db_table': "'meetings'"},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenter': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'presenter_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '25', 'db_index': 'True'}),
            'tba': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(19, 30)'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['meetings']
