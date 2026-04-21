from blob_effect.common.components import RangeComponents


def test_range_components_holds_values():
    r = RangeComponents(min=1, max=10)
    assert r.min == 1
    assert r.max == 10


def test_range_components_export_uses_uppercase_keys():
    r = RangeComponents(min=2, max=5)
    assert r.export() == {"MIN": 2, "MAX": 5}


def test_range_components_setters_update_values():
    r = RangeComponents(min=0, max=1)
    r.min = 7
    r.max = 42
    assert (r.min, r.max) == (7, 42)
