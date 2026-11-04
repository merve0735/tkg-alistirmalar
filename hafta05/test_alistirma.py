# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145



@pytest.mark.parametrize(
    "tutar, beklenen_indirim",
    [
        (0, 0),
        (99, 0),
        (100, 5),
        (499, 5),
        (500, 10),
        (999, 10),
        (1000, 15),
        (1500, 15),
    ]
)
def test_indirim_orani_gecerli_tutarlar(tutar, beklenen_indirim):
    assert indirim_orani(tutar) == beklenen_indirim


def test_indirim_orani_negatif_tutar():
    with pytest.raises(ValueError, match="tutar negatif olamaz"):
        indirim_orani(-1)


def test_sepet_toplami_bos_sepet():
    assert sepet_toplami([]) == 0


@pytest.mark.parametrize("hatali_adet", [0, -1])
def test_sepet_toplami_gecersiz_adet(hatali_adet):
    sepet = [{"urun": "elma", "fiyat": 10, "adet": hatali_adet}]
    with pytest.raises(ValueError, match="adet pozitif olmalı"):
        sepet_toplami(sepet)


def test_en_pahali_urun_normal():
    sepet = [
        {"urun": "elma", "fiyat": 10, "adet": 1},
        {"urun": "muz", "fiyat": 30, "adet": 1},
        {"urun": "armut", "fiyat": 20, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "muz"


def test_en_pahali_urun_esit_fiyatli():
    sepet = [
        {"urun": "elma", "fiyat": 30, "adet": 1},
        {"urun": "muz", "fiyat": 30, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "elma"


def test_en_pahali_urun_bos_sepet():
    assert en_pahali_urun([]) is None
    