import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)
    
    def test_kassapaate_on_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_kateis_osto_toimii_edulliset(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kateis_osto_toimii_maukkaat(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassa.maukkaat, 1)
        
    def test_kateis_osto_toimii_edulliset_vaihtorahat(self):
        maksu = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(maksu, 10)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kateis_osto_toimii_maukkaat_vaihtorahat(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(maksu, 10)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassa.maukkaat, 1)

        
    def test_kateis_osto_toimii_edulliset_ei_riittavasti_katetta(self):
        maksu = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kateis_osto_toimii_maukkaat_ei_riitavasti_katetta(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
        
    def test_kortti_osto_toimii_edulliset(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kortti_osto_toimii_maukkaat(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kortti_osto_toimii_edulliset_palauttaa_true(self):
        maksu = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(maksu)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kortti_osto_toimii_maukkaat_palauttaa_true(self):
        maksu = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(maksu)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kortti_osto_toimii_edulliset_palauttaa_false_jos_kortilla_ei_ole_rahaa(self):
        maksu = self.kassa.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertFalse(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kortti_osto_toimii_maukkaat_palauttaa_false_jos_kortilla_ei_ole_rahaa(self):
        maksu = self.kassa.syo_maukkaasti_kortilla(Maksukortti(200))
        self.assertFalse(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_lataa_kortille_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.0)

    def test_ei_voi_ladata_kortille_negatiivista_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)