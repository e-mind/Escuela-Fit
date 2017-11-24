from __future__ import unicode_literals

from django.db import models


class AOAAltoEnGrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    colesterol = models.CharField(max_length=50)
    vitaminaa = models.CharField(db_column='vitaminaA', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierrogm = models.CharField(db_column='HierroGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    selenio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'A.O.A ALTO EN GRASA'

    def __str__(self):
        return self.alimentos


class AOABajosEnGrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    colesterol = models.CharField(max_length=50)
    vitaminaa = models.CharField(db_column='vitaminaA', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierrogm = models.CharField(db_column='HierroGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    selenio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'A.O.A BAJOS EN GRASA'

    def __str__(self):
        return self.alimentos


class AOAModeradosEnGrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    colesterol = models.CharField(max_length=50)
    vitaminaa = models.CharField(db_column='vitaminaA', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierrogm = models.CharField(db_column='HierroGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    selenio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'A.O.A MODERADOS EN GRASA'

    def __str__(self):
        return self.alimentos


class AOAMuyBajosEnGrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    colesterol = models.CharField(max_length=50)
    vitaminaa = models.CharField(db_column='vitaminaA', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierrogm = models.CharField(db_column='HierroGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    selenio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'A.O.A MUY BAJOS EN GRASA'

    def __str__(self):
        return self.alimentos


class Frutas(models.Model):
    alimentos = models.CharField(max_length=50)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    fibragr = models.CharField(db_column='fibraGr', max_length=50)  # Field name made lowercase.
    vitaminaa = models.CharField(db_column='vitaminaA', max_length=50)  # Field name made lowercase.
    acidoascorbico = models.CharField(db_column='AcidoAscorbico', max_length=50)  # Field name made lowercase.
    acidofolico = models.CharField(db_column='AcidoFolico', max_length=50)  # Field name made lowercase.
    hierronohemgm = models.CharField(db_column='HierroNOHEMGm', max_length=50)  # Field name made lowercase.
    potasiomg = models.CharField(db_column='PotasioMg', max_length=50)  # Field name made lowercase.
    azucarporequivalente = models.CharField(db_column='AzucarPorEquivalente', max_length=50)  # Field name made lowercase.
    indiceglicemico = models.CharField(db_column='IndiceGlicemico', max_length=50)  # Field name made lowercase.
    cargaglicemica = models.CharField(db_column='CargaGlicemica', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Frutas'

    def __str__(self):
        return self.alimentos


class Verduras(models.Model):
    alimentos = models.CharField(max_length=50)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    fibragr = models.CharField(db_column='fibraGr', max_length=50)  # Field name made lowercase.
    vitaminaa = models.CharField(db_column='VitaminaA', max_length=50)  # Field name made lowercase.
    acidoascorbicomg = models.CharField(db_column='AcidoAscorbicoMg', max_length=50)  # Field name made lowercase.
    acidofolico = models.CharField(db_column='AcidoFolico', max_length=50)  # Field name made lowercase.
    hierronohemgm = models.CharField(db_column='HierroNOHEMGm', max_length=50)  # Field name made lowercase.
    potasiomg = models.CharField(db_column='PotasioMg', max_length=50)  # Field name made lowercase.
    indiceglicemico = models.CharField(db_column='IndiceGlicemico', max_length=50)  # Field name made lowercase.
    cargaglicemica = models.CharField(db_column='CargaGlicemica', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Verduras'

    def __str__(self):
        return self.alimentos


class Cerealescongrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    fibragr = models.CharField(db_column='fibraGr', max_length=50)  # Field name made lowercase.
    acidofolico = models.CharField(db_column='AcidoFolico', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierronohemgm = models.CharField(db_column='HierroNOHEMGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    azucarporequivalente = models.CharField(db_column='AzucarPorEquivalente', max_length=50)  # Field name made lowercase.
    indiceglicemico = models.CharField(db_column='IndiceGlicemico', max_length=50)  # Field name made lowercase.
    cargaglicemica = models.CharField(db_column='CargaGlicemica', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cerealesConGrasa'

    def __str__(self):
        return self.alimentos


class Cerealessingrasa(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    fibragr = models.CharField(db_column='fibraGr', max_length=50)  # Field name made lowercase.
    acidofolico = models.CharField(db_column='AcidoFolico', max_length=50)  # Field name made lowercase.
    calcio = models.CharField(max_length=50)
    hierronohemgm = models.CharField(db_column='HierroNOHEMGm', max_length=50)  # Field name made lowercase.
    sodio = models.CharField(max_length=50)
    azucarporequivalente = models.CharField(db_column='AzucarPorEquivalente', max_length=50)  # Field name made lowercase.
    indiceglicemico = models.CharField(db_column='IndiceGlicemico', max_length=50)  # Field name made lowercase.
    cargaglicemica = models.CharField(db_column='CargaGlicemica', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cerealesSinGrasa'

    def __str__(self):
        return self.alimentos


class Leguminosas(models.Model):
    alimentos = models.CharField(max_length=100)
    cantidadsugerida = models.CharField(db_column='cantidadSugerida', max_length=50)  # Field name made lowercase.
    unidad = models.CharField(max_length=50)
    pesobrutoredondeadogr = models.CharField(db_column='pesoBrutoRedondeadoGr', max_length=50)  # Field name made lowercase.
    pesonetogr = models.CharField(db_column='pesoNetoGr', max_length=50)  # Field name made lowercase.
    energiakcal = models.CharField(db_column='energiaKcal', max_length=50)  # Field name made lowercase.
    proteinagr = models.CharField(db_column='proteinaGr', max_length=50)  # Field name made lowercase.
    lipidosgr = models.CharField(db_column='LipidosGr', max_length=50)  # Field name made lowercase.
    hidratosdecarbonogr = models.CharField(db_column='HidratosDeCarbonoGr', max_length=50)  # Field name made lowercase.
    fibragr = models.CharField(db_column='fibraGr', max_length=50)  # Field name made lowercase.
    hierronohemgm = models.CharField(db_column='HierroNOHEMGm', max_length=50)  # Field name made lowercase.
    selenio = models.CharField(max_length=50)
    sodio = models.CharField(max_length=50)
    fosforo = models.CharField(max_length=50)
    potasio = models.CharField(max_length=50)
    azucarporequivalente = models.CharField(db_column='AzucarPorEquivalente', max_length=50)  # Field name made lowercase.
    indiceglicemico = models.CharField(db_column='IndiceGlicemico', max_length=50)  # Field name made lowercase.
    cargaglicemica = models.CharField(db_column='CargaGlicemica', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leguminosas'

    def __str__(self):
        return self.alimentos
