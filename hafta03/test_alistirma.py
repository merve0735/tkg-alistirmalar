import pytest
from alistirma import bilet_fiyati, kargo_ucreti, ortalama




def test_kargo_negatif_tutar_hata():
    with pytest.raises(ValueError):
        kargo_ucreti(-10)


def test_kargo_ucretli_sinir_alti():
    assert kargo_ucreti(0) == 50
    assert kargo_ucreti(499.99) == 50


def test_kargo_ucretsiz_tam_sinir_ve_ustu():
    assert kargo_ucreti(500) == 0
    assert kargo_ucreti(1000) == 0







def test_bilet_negatif_yas_hata():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)


def test_bilet_ucretsiz_kategori():
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(6) == 0


def test_bilet_ogrenci_kategori():
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(17) == 50


def test_bilet_tam_kategori():
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(19) == 100
    assert bilet_fiyati(64) == 100


def test_bilet_yasli_kategori():
    assert bilet_fiyati(65) == 60
    assert bilet_fiyati(90) == 60







def test_ortalama_bos_liste_hata():
    with pytest.raises(ValueError):
        ortalama([])


def test_ortalama_hesabi_ve_sinirlar():
    assert ortalama([100]) == 100.0
    assert ortalama([80, 90, 100]) == 90.0
    assert ortalama([10, 20, 20]) == pytest.approx(16.666666666666668)
