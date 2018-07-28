from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestCrudPai(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()

    def test_crud(self):
        client = Client()
        client.force_login(User.objects.get(username='jon'))
        self._addpai(client, 'tony')
        self._addpai(client, 'regis')
        self._addpai(client, 'elias')
        self._list_pais_assert_count(client, 3, ['tony', 'regis', 'elias'])
        self._list_pais_edit_name(client, 1, 'REGINA')
        self._list_pais_assert_count(client, 3, ['tony', 'REGINA', 'elias'])
        self._list_pais_remove(client, 1)
        self._list_pais_assert_count(client, 2, ['tony', 'elias'])
        self._list_pais_and_get(client, 1, 'elias')

    def _addpai(self, client, name):
        pai = {
            'name': name,
            'countfilhos': 10,
            'maisvelho': 'espoleta'
        }
        r = client.post('/api/pais/save', {'pai': json.dumps(pai)})
        self.assertEqual(200, r.status_code)

    def _list_pais_assert_count(self, client, count, expectednames):
        r = client.get('/api/pais')
        self.assertEqual(200, r.status_code)
        pais = json.loads(r.content.decode('utf-8'))
        self.assertEqual(count, len(pais))
        self.assertEqual(expectednames, [p['name'] for p in pais])

    def _list_pais_edit_name(self, client, idx, newname):
        r = client.get('/api/pais')
        self.assertEqual(200, r.status_code)
        pais = json.loads(r.content.decode('utf-8'))
        pai = pais[idx]
        pai['name'] = newname
        self.assertTrue('id' in pai)
        r = client.post('/api/pais/save', {'pai': json.dumps(pai)})
        self.assertEqual(200, r.status_code)

    def _list_pais_remove(self, client, idx):
        r = client.get('/api/pais')
        self.assertEqual(200, r.status_code)
        pais = json.loads(r.content.decode('utf-8'))
        pai = pais[idx]
        r = client.post('/api/pais/%s/remove' % pai['id'])
        self.assertEqual(200, r.status_code)

    def _list_pais_and_get(self, client, idx, expectedname):
        r = client.get('/api/pais')
        self.assertEqual(200, r.status_code)
        pais = json.loads(r.content.decode('utf-8'))
        pai = pais[idx]
        r = client.get('/api/pais/%s' % pai['id'])
        self.assertEqual(200, r.status_code)
        pai = json.loads(r.content.decode('utf-8'))
        self.assertEqual(expectedname, pai['name'])





