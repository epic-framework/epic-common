import datetime as dt

from epic.common.time import to_datetime


def test_to_datetime():
    t = dt.datetime(
        1981, 7, 8, 12, 34, 56,
        tzinfo=dt.timezone(dt.timedelta(hours=2), name="Tel Aviv"),
    )
    for x in ("today", "yesterday", "NOW", 100, 100.5):
        assert isinstance(to_datetime(x), dt.datetime)
    assert to_datetime(t) is t
    assert to_datetime(t.isoformat()) == t
    t_no_tz = t.replace(tzinfo=None)
    assert to_datetime(t_no_tz.isoformat()) == t_no_tz
