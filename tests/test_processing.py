import pytest
from typing import Any
from src.processing import filter_by_state, sort_by_date


inform_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

@pytest.mark.parametrize(
    "state_id, expected",
    [
        ("EXECUTED", [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]),
        ("CANCELED", [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]),
        ("PENDING", []),
    ]
)
def test_filter_by_state(state_id: str, expected: list[dict[str, Any]]) -> None:
    """Тестирование фильтрации списка по статусу."""
    assert filter_by_state(inform_state, state_id) == expected


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (True, [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]),
        (False, [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]),
    ]
)
def test_sort_by_date(reverse: bool, expected: list[dict[str, Any]]) -> None:
    """Тестирование сортировки списка по дате."""
    assert sort_by_date(inform_state, reverse) == expected
