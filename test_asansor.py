import asansor


def test_on_uc_yasak():
    kat, gerekce = asansor.karar_ver(13, False)
    assert kat != 13
    assert "13" in gerekce


def test_gizli_not_fren_icerir():
    notu = asansor.gizli_notu_ac()
    assert "fren" in notu
    assert "Parti yok" in notu


def test_kat_sayi():
    kat, _ = asansor.karar_ver(4, False)
    assert isinstance(kat, int)
