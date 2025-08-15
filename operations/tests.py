from django .test import TestCase
from .models import Harvest

class HarvestModelTest(TestCase):
    def setup(self):
        Harvest.object.create( date_harvested="2025.04.10",total_mites=5,batch_number="Gsp200")

    def test_harvest_creation(self):
        Harvest = Harvest.object.get(batch_number="Gsp200")
        self.assertEqual(Harvest.total_mites,5)
        self.assertEqual(str(Harvest.date_harvested), "2025-04-10")


    