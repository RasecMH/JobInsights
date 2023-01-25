from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert list(
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0].keys()
    ) == ["title", "salary", "type"]
