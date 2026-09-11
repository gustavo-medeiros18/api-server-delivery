from exemplo_soma.soma import soma


class TestExample:
    def test_soma(self):
        resultado = soma(10, 5)

        assert resultado == 15