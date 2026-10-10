import unittest
from decimal import Decimal
from tools.estimate_lca import calculate

EXAMPLE = {
    'status': 'ILLUSTRATIVE',
    'system_boundary': 'IT+site+fabrication allouee',
    'factor_source': 'HYPOTHETICAL',
    'factor_method': 'hypothetical',
    'model_or_workload': '10k valid responses - synthetic',
    'it_energy_kwh': 100,
    'pue': 1.25,
    'grid_intensity_kgco2e_per_kwh': 0.05,
    'allocated_embodied_kgco2e': 8,
    'valid_results': 10000,
}


class LCATests(unittest.TestCase):
    def test_private_illustration(self):
        r = calculate(EXAMPLE)
        self.assertEqual(Decimal(r['total_included_kgco2e']), Decimal('14.25'))
        self.assertEqual(Decimal(r['kgco2e_per_1000_valid_results']), Decimal('1.425'))
        self.assertFalse(r['measured_footprint'])

    def test_cloud_illustration(self):
        d = dict(EXAMPLE, it_energy_kwh=70, pue=1.18,
                 grid_intensity_kgco2e_per_kwh=0.30,
                 allocated_embodied_kgco2e=3)
        r = calculate(d)
        self.assertEqual(Decimal(r['total_included_kgco2e']), Decimal('27.78'))
        self.assertEqual(Decimal(r['kgco2e_per_1000_valid_results']), Decimal('2.778'))

    def test_reject_missing_embodied(self):
        d = EXAMPLE.copy()
        d.pop('allocated_embodied_kgco2e')
        with self.assertRaises(ValueError):
            calculate(d)

    def test_reject_invalid_pue(self):
        with self.assertRaises(ValueError):
            calculate(dict(EXAMPLE, pue=.8))

    def test_reject_nan(self):
        with self.assertRaises(ValueError):
            calculate(dict(EXAMPLE, it_energy_kwh='NaN'))

    def test_reject_no_valid_results(self):
        with self.assertRaises(ValueError):
            calculate(dict(EXAMPLE, valid_results=0))

    def test_reject_missing_disclosures(self):
        with self.assertRaises(ValueError):
            calculate(dict(EXAMPLE, factor_source=''))


if __name__ == '__main__':
    unittest.main()
