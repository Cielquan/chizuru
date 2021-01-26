"""
    tests.test_chizuru
    ~~~~~~~~~~~~~~~~~~

    Test for module: chizuru

    :copyright: (c) 2021, Christian Riedel and AUTHORS
    :license: GPL-3.0, see LICENSE for details
"""  # noqa: D205,D208,D400
from chizuru import chizuru


def test_dummy() -> None:
    """Test a dummy to silence pytest exit code 5."""
    print(chizuru)

    result = 1 + 1

    assert result == 2
