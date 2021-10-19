from libraries import url as val


def test_url_validation():
    assert val.url_validate("https://github.com/eternnoir/pyTelegramBotAPI")
    assert val.url_validate("http://detsadmo.mosreg.ru")
    assert not val.url_validate("12345")
    assert not val.url_validate("")
