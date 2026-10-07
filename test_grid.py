from copy import deepcopy
import unittest
import grid

class NormalizeGridTests(unittest.TestCase):
    def setUp(self):
        self.metadata = {
            'grid': {'columns': 2160, 'rows': 1080, 'version': 1},
            'reveal_media_present': False,
            'successful_cases': [
                'historical_reveal', 'missing_reveal_media', 'public_share', 'start'
            ],
        }

    def assert_rejected_without_mutation(self, metadata):
        original = deepcopy(metadata)
        with self.assertRaises(ValueError):
            grid.normalize_grid(metadata)
        self.assertEqual(metadata, original)

    def test_controller_projection(self):
        original = deepcopy(self.metadata)
        result = grid.normalize_grid(self.metadata)
        self.assertEqual(result, {'rows': 1080, 'columns': 2160, 'version': 1})
        self.assertEqual(self.metadata, original)
        self.assertIsNot(result, self.metadata['grid'])
        result['rows'] = 1
        self.assertEqual(self.metadata, original)

    def test_other_positive_integers(self):
        for projection in (
            {'rows': 1, 'columns': 1, 'version': 1},
            {'rows': 7, 'columns': 13, 'version': 2},
        ):
            with self.subTest(projection=projection):
                metadata = {'grid': projection}
                original = deepcopy(metadata)
                self.assertEqual(grid.normalize_grid(metadata), projection)
                self.assertEqual(metadata, original)

    def test_missing_grid(self):
        self.assert_rejected_without_mutation({})

    def test_invalid_metadata_or_grid_container(self):
        for value in (None, True, 1, 'grid', [], ['rows', 'columns', 'version']):
            with self.subTest(value=value):
                self.assert_rejected_without_mutation(value)
                self.assert_rejected_without_mutation({'grid': value})

    def test_missing_grid_fields(self):
        for field in ('rows', 'columns', 'version'):
            with self.subTest(field=field):
                metadata = deepcopy(self.metadata)
                del metadata['grid'][field]
                self.assert_rejected_without_mutation(metadata)
        self.assert_rejected_without_mutation({'grid': {}})

    def test_extra_grid_field(self):
        self.metadata['grid']['extra'] = 1
        self.assert_rejected_without_mutation(self.metadata)

    def test_replaced_grid_field(self):
        del self.metadata['grid']['columns']
        self.metadata['grid']['width'] = 2160
        self.assert_rejected_without_mutation(self.metadata)

    def test_invalid_grid_values(self):
        for field in ('rows', 'columns', 'version'):
            for value in (0, -1, True, False, 1.0, '1', None, [], {}):
                with self.subTest(field=field, value=value):
                    metadata = deepcopy(self.metadata)
                    metadata['grid'][field] = value
                    self.assert_rejected_without_mutation(metadata)
