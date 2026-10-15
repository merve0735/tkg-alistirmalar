# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import otopark_ucreti, sifre_gucu, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


def test_sifre_gucu_bos_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")


def test_sifre_gucu_zayif_sinir():
    assert sifre_gucu("1234567") == "zayıf"


def test_sifre_gucu_orta():
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("12345678901") == "orta"


def test_sifre_gucu_guclu():
    assert sifre_gucu("123456789012") == "güçlü"
    assert sifre_gucu("1234567890123") == "güçlü"


def test_otopark_ucreti_negatif_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


def test_otopark_ucreti_ucretsiz():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(15) == 0


def test_otopark_ucreti_20tl():
    assert otopark_ucreti(16) == 20
    assert otopark_ucreti(60) == 20


def test_otopark_ucreti_40tl():
    assert otopark_ucreti(61) == 40
    assert otopark_ucreti(180) == 40


def test_otopark_ucreti_60tl():
    assert otopark_ucreti(181) == 60
    assert otopark_ucreti(300) == 60


def test_yuzde_degisim_eski_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)


def test_yuzde_degisim_hesap():
    assert yuzde_degisim(200, 250) == pytest.approx(25.0)
    assert yuzde_degisim(200, 150) == pytest.approx(-25.0)
    assert yuzde_degisim(100, 100) == pytest.approx(0.0)