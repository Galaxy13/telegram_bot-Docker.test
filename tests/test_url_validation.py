from libraries import url as val

def test_url_validation():
    assert val.url_validate('https://github.com/eternnoir/pyTelegramBotAPI') == True