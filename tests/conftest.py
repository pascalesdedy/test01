import pytest
from utils.driver_factory import get_driver
from datetime import datetime

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{timestamp}.html"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot)

            # Attach to HTML report
            if hasattr(item.config, "_html"):
                extra = getattr(item.config, "extra", [])
                extra.append(pytest_html.extras.png(screenshot))
                item.config._html.extras = extra