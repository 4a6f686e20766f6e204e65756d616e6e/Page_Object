import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

# pytest -s -v test_items.py по умолчанию запустится как:
# pytest -s -v --browser_name=firefox --language=es test_items.py

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default='firefox',
					 help="Choose browser: chrome or firefox")
	parser.addoption('--language', action='store', default='ru',
					 help="Choose language: ec or fr")


@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	browser_lang = request.config.getoption("language")
	browser = None
	if browser_name == "chrome":
		print("\nstart chrome browser for test..")
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
		browser = webdriver.Chrome(options=options)
	elif browser_name == "firefox":
		print("\nstart firefox browser for test..")
		options = Options()
		# FirefoxProfile = webdriver.FirefoxProfile()
		options.set_preference("intl.accept_languages", browser_lang)
		browser = webdriver.Firefox(options=options)

	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	print("\nquit browser..")
	browser.quit()