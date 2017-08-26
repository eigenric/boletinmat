from concurso import solve


def test_solve():
    assert list(solve(91)) == [(1, 13), (10, 16), (45, 46)]
