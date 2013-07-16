# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    depends_on = (
        ('hsauth', '0001_initial'),
    )
    def forwards(self, orm):
        # Adding model 'Revision'
        db.create_table(u'reversion_revision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manager_slug', self.gf('django.db.models.fields.CharField')(default=u'default', max_length=200, db_index=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hsauth.User'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reversion', ['Revision'])

        # Adding model 'Version'
        db.create_table(u'reversion_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('revision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reversion.Revision'])),
            ('object_id', self.gf('django.db.models.fields.TextField')()),
            ('object_id_int', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('serialized_data', self.gf('django.db.models.fields.TextField')()),
            ('object_repr', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'reversion', ['Version'])


    def backwards(self, orm):
        # Deleting model 'Revision'
        db.delete_table(u'reversion_revision')

        # Deleting model 'Version'
        db.delete_table(u'reversion_version')


    models = {
        u'actor.actor': {
            'Meta': {'object_name': 'Actor', 'db_table': "u'actor'"},
            'actor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actor.ActorType']"}),
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['locations.Location']", 'symmetrical': 'False'}),
            'bitflag': ('core.models.fields.HSBitflagField', [], {'default': '0', 'bitflagmask': '39'}),
            'contactable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'actor.actortype': {
            'Meta': {'object_name': 'ActorType', 'db_table': "u'actor_type'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hsauth.user': {
            'Meta': {'object_name': 'User', '_ormbases': [u'actor.Actor']},
            u'actor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['actor.Actor']", 'unique': 'True', 'primary_key': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'u'", 'max_length': '1'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_security_number': ('core.models.fields.EncryptedCharField', [], {'max_length': '165', 'null': 'True', 'blank': 'True'})
        },
        u'locations.country': {
            'Meta': {'object_name': 'Country', 'db_table': "u'country'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number_regex': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'phone_prefix': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'postal_code_regex': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'second_level_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'third_level_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'locations.county': {
            'Meta': {'ordering': "(u'country', u'identifier')", 'object_name': 'County', 'db_table': "u'county'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'counties'", 'to': u"orm['locations.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "u'location'"},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.PostalCode']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'locations.municipality': {
            'Meta': {'object_name': 'Municipality', 'db_table': "u'municipality'"},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'municipalities'", 'to': u"orm['locations.County']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'locations.postalcode': {
            'Meta': {'object_name': 'PostalCode', 'db_table': "u'postal_code'"},
            'address_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'postal_codes'", 'to': u"orm['locations.Municipality']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'reversion.revision': {
            'Meta': {'object_name': 'Revision'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_slug': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '200', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hsauth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'reversion.version': {
            'Meta': {'object_name': 'Version'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {}),
            'object_id_int': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'object_repr': ('django.db.models.fields.TextField', [], {}),
            'revision': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reversion.Revision']"}),
            'serialized_data': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['reversion']
