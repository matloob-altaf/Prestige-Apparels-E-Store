from django.test import TestCase
from  django.test import SimpleTestCase
from django.urls import reverse,resolve
from mlmodel.views import modelResults 


# Create your tests here.
class Testurl(TestCase):
    def test_resolution_for_modelResults(self):
        resolver = resolve('/model/mlresults')
        self.assertEqual(resolver.view_name,'mlmodel:model')
        self.assertEqual(resolver.app_name,'mlmodel')


#Model used here is tested in other file




