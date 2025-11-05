import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldon_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 30.0)
    
    def test_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 08.0)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_metodi_palauttaa_true_jos_tililla_on_katetta(self):
        true = self.maksukortti.ota_rahaa(500)
        self.assertTrue(true)

    def test_metodi_palauttaa_false_jos_tililla_ei_ole_katetta(self):
        false = self.maksukortti.ota_rahaa(50000)
        self.assertFalse(false)