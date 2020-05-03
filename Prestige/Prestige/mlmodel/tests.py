from django.test import TestCase
from  django.test import SimpleTestCase
from django.urls import reverse,resolve
from mlmodel.views import modelResults 


# Create your tests here.
class Testurl(TestCase):
    '''class to test url for this app'''
    def test_resolution_for_modelResults(self):
        '''function to test view and app name for this mlmodel app'''
        resolver = resolve('/model/mlresults')
        self.assertEqual(resolver.view_name,'mlmodel:model')
        self.assertEqual(resolver.app_name,'mlmodel')






