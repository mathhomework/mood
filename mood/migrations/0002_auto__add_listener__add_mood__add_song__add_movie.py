# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Listener'
        db.create_table(u'mood_listener', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'mood', ['Listener'])

        # Adding M2M table for field groups on 'Listener'
        m2m_table_name = db.shorten_name(u'mood_listener_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('listener', models.ForeignKey(orm[u'mood.listener'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['listener_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Listener'
        m2m_table_name = db.shorten_name(u'mood_listener_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('listener', models.ForeignKey(orm[u'mood.listener'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['listener_id', 'permission_id'])

        # Adding model 'Mood'
        db.create_table(u'mood_mood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mood', ['Mood'])

        # Adding M2M table for field listener on 'Mood'
        m2m_table_name = db.shorten_name(u'mood_mood_listener')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mood', models.ForeignKey(orm[u'mood.mood'], null=False)),
            ('listener', models.ForeignKey(orm[u'mood.listener'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mood_id', 'listener_id'])

        # Adding model 'Song'
        db.create_table(u'mood_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('album', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'mood', ['Song'])

        # Adding M2M table for field mood on 'Song'
        m2m_table_name = db.shorten_name(u'mood_song_mood')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm[u'mood.song'], null=False)),
            ('mood', models.ForeignKey(orm[u'mood.mood'], null=False))
        ))
        db.create_unique(m2m_table_name, ['song_id', 'mood_id'])

        # Adding M2M table for field listener on 'Song'
        m2m_table_name = db.shorten_name(u'mood_song_listener')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm[u'mood.song'], null=False)),
            ('listener', models.ForeignKey(orm[u'mood.listener'], null=False))
        ))
        db.create_unique(m2m_table_name, ['song_id', 'listener_id'])

        # Adding model 'Movie'
        db.create_table(u'mood_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'mood', ['Movie'])

        # Adding M2M table for field song on 'Movie'
        m2m_table_name = db.shorten_name(u'mood_movie_song')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'mood.movie'], null=False)),
            ('song', models.ForeignKey(orm[u'mood.song'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'song_id'])

        # Adding M2M table for field listener on 'Movie'
        m2m_table_name = db.shorten_name(u'mood_movie_listener')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'mood.movie'], null=False)),
            ('listener', models.ForeignKey(orm[u'mood.listener'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'listener_id'])


    def backwards(self, orm):
        # Deleting model 'Listener'
        db.delete_table(u'mood_listener')

        # Removing M2M table for field groups on 'Listener'
        db.delete_table(db.shorten_name(u'mood_listener_groups'))

        # Removing M2M table for field user_permissions on 'Listener'
        db.delete_table(db.shorten_name(u'mood_listener_user_permissions'))

        # Deleting model 'Mood'
        db.delete_table(u'mood_mood')

        # Removing M2M table for field listener on 'Mood'
        db.delete_table(db.shorten_name(u'mood_mood_listener'))

        # Deleting model 'Song'
        db.delete_table(u'mood_song')

        # Removing M2M table for field mood on 'Song'
        db.delete_table(db.shorten_name(u'mood_song_mood'))

        # Removing M2M table for field listener on 'Song'
        db.delete_table(db.shorten_name(u'mood_song_listener'))

        # Deleting model 'Movie'
        db.delete_table(u'mood_movie')

        # Removing M2M table for field song on 'Movie'
        db.delete_table(db.shorten_name(u'mood_movie_song'))

        # Removing M2M table for field listener on 'Movie'
        db.delete_table(db.shorten_name(u'mood_movie_listener'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mood.listener': {
            'Meta': {'object_name': 'Listener'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'mood.mood': {
            'Meta': {'object_name': 'Mood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listener': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mood.Listener']", 'symmetrical': 'False'})
        },
        u'mood.movie': {
            'Meta': {'object_name': 'Movie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listener': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mood.Listener']", 'symmetrical': 'False'}),
            'song': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mood.Song']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mood.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listener': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mood.Listener']", 'symmetrical': 'False'}),
            'mood': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mood.Mood']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mood']