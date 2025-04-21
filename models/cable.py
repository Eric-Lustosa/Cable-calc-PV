class Cable:
    def __init__(self, fabricante, modelo, secao_mm2, resistividade_ohm_km, isolamento, tipo_cabo, capacidade_nominal_a):
        self.fabricante = fabricante
        self.modelo = modelo
        self.secao_mm2 = secao_mm2
        self.resistividade_ohm_km = resistividade_ohm_km
        self.isolamento = isolamento
        self.tipo_cabo = tipo_cabo
        self.capacidade_nominal_a = capacidade_nominal_a  # <- adicionar aqui

    def __repr__(self):
        return f"<Cable {self.modelo} {self.secao_mm2}mm² - {self.tipo_cabo}>"
