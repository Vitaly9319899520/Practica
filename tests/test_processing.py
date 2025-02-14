from src.processing import filter_by_state
import pytest
from src.processing import sort_by_data

from tests.conftest import fixture_list, fixture_processing


def test_filter_by_state(fixture_masks):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
        == fixture_masks
    )


def test_filter_by_state_list(fixture_list):
    assert filter_by_state(fixture_list) == []


@pytest.mark.parametrize(
    "x,y", [([], []), ([{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], ([]))]
)
def test_filter_by_state_parametr(x, y):
    assert filter_by_state(x) == y


def test_sort_by_data(fixture_processing):
    assert sort_by_data(fixture_processing) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_data_revers():
    assert sort_by_data(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        reverse=False,
    )


def test_sort_by_data_revers_2():
    assert sort_by_data(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2019-07-03T18:35:29.512364",
            },
        ]
    )


def test_sort_by_data_revers_3():
    assert sort_by_data(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "18.02.2018"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "18.02.2019",
            },
            {"id": 594226727, "state": "CANCELED", "date": "18.07.2018"},
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "18.02.2017",
            },
        ]
    )
