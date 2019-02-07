import unittest
from app.models import News_Sources,News_Article

class News_Sources_Test(unittest.TestCase):
    """ class that tests the correct insatiation of variables"""
    def setUp(self):
        '''
        Set up class that will run before any test
        '''
        self.sources=News_Sources('test','Test','test to showcase testing','technology','test.com')
    def test_instance(self):
        self.assertTrue(setinstance(self.sources,News_Sources))
    def test_instance_variables(self):
        self.assertEquals(self.sources.id,'test')
        self.assertEquals(self.sources.name,'Test')
        self.assertEquals(self.sources.description,'test to showcase testing')
        self.assertEquals(self.sources.category,'technology')
        self.assertEquals(self.sources.url,'test.com')


# if __name__ == '__main__':
#     unittest()
