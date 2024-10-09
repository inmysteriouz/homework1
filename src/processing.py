from typing import Any

inform_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(inform_state: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует операции по ключу,
    принимает список словарей,
    и возвращает новый список словарей по указанному ключу"""
    list_stat = []
    for key in inform_state:
        if key.get("state") == state_id:
            list_stat.append(key)
    return list_stat


print(filter_by_state(inform_state))


def sort_by_date(inform_state: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей,
    задает порядок сортировки,
    и возвращает новый список отсортированный по дате"""
    sorted_inform_state = sorted(inform_state, key=lambda inform_state: inform_state["date"], reverse=reverse)
    return sorted_inform_state


print(sort_by_date(inform_state))
