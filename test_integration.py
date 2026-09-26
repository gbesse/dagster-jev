import unittest
from unittest.mock import MagicMock, patch
from dagster_jev import semantic_asset_check

class CheckTest(unittest.TestCase):
    def test_declares_blocking_asset_check(self):
        with patch('dagster.asset_check') as decorator:
            decorator.side_effect = lambda **kwargs: lambda fn: fn
            fn = semantic_asset_check('reviews', question='Good?', client=MagicMock())
            self.assertTrue(callable(fn))
            self.assertTrue(decorator.call_args.kwargs['blocking'])
