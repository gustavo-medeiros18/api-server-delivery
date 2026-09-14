from exemplo_soma.soma import soma


def test_soma():
    resultado = soma(10, 5)

    assert resultado == 15