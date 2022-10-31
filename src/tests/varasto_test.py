import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_yli_0_tilavuuden(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.varasto = Varasto(-1)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_luo_yli_0_saldon(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.varasto = Varasto(10, -1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastoon_ei_laiteta_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 1)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_oteta_liikaa_tavaraa(self):
        self.varasto.ota_varastosta(self.varasto.tilavuus + 1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_alle_0_lisaaminen_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.saldo)

    def test_alle_0_ottaminen_ei_tee_mitaan(self):
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.saldo)

    def test_printtaa_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
