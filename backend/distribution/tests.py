from django.test import SimpleTestCase

from distribution.factories import DistributionFactory


class DistributionTestCase(SimpleTestCase):
    def setUp(self):
        self.distribution = DistributionFactory(
            name='Test',
            message="Simple message"
        )

    def test_distribution(self):
        self.assertEqual(self.distribution.name, 'Test')
        self.assertEqual(self.distribution.message, 'Simple message')
        self.distribution.name = "test_2"
        self.distribution.save(update_fields=['name'])
        self.assertEqual(self.distribution.name, 'test_2')



