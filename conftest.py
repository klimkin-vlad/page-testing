from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
import pytest

service = Service(executable_path='./geckodriver')

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language (ar, ca, cs, da, de, en, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sl, uk, zh)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_argument("-profile")
    options.add_argument("./profile")
    if not language in ["ar", "ca", "cs", "da", "de", "en", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sl", "uk", "zh"]:
        raise pytest.UsageError("--language should be in (ar, ca, cs, da, de, en, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sl, uk, zh)")
    options.set_preference("intl.accept_languages", language)
    browser = webdriver.Firefox(service = service, options = options)
    yield browser
    print("\nquit browser..")
    browser.quit()
