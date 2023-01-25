from src.pre_built.sorting import sort_by

mockList = [
    {"max_salary": 1000, "min_salary": 100, "date_posted": "24-01-2023"},
    {"max_salary": 2000, "min_salary": 200, "date_posted": "23-01-2023"},
    {"max_salary": 3000, "min_salary": 300, "date_posted": "22-01-2023"},
    {"max_salary": 4000, "min_salary": 400, "date_posted": "21-01-2023"},
]

mockMinSalarySorted = [
    {"max_salary": 1000, "min_salary": 100, "date_posted": "24-01-2023"},
    {"max_salary": 2000, "min_salary": 200, "date_posted": "23-01-2023"},
    {"max_salary": 3000, "min_salary": 300, "date_posted": "22-01-2023"},
    {"max_salary": 4000, "min_salary": 400, "date_posted": "21-01-2023"},
]

mockMaxSalarySorted = [
    {"max_salary": 4000, "min_salary": 400, "date_posted": "21-01-2023"},
    {"max_salary": 3000, "min_salary": 300, "date_posted": "22-01-2023"},
    {"max_salary": 2000, "min_salary": 200, "date_posted": "23-01-2023"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "24-01-2023"},
]
mockDatePostedSorted = [
    {"max_salary": 4000, "min_salary": 400, "date_posted": "21-01-2023"},
    {"max_salary": 3000, "min_salary": 300, "date_posted": "22-01-2023"},
    {"max_salary": 2000, "min_salary": 200, "date_posted": "23-01-2023"},
    {"max_salary": 1000, "min_salary": 100, "date_posted": "24-01-2023"},
]


def test_sort_by_criteria():
    sort_by(mockList, "min_salary")
    assert mockList == mockMinSalarySorted

    sort_by(mockList, "max_salary")
    assert mockList == mockMaxSalarySorted

    sort_by(mockList, "date_posted")
    assert mockList == mockDatePostedSorted
