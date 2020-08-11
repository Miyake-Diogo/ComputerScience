def func(x):
    return x + 1
# Esse falha
def test_answer():
    assert func(3) == 5

# esse passa
def test_answer2():
    assert func(3) == 4


# para chamar o teste digire no terminal >>> py.test WEEK_5/examplepytest.py
