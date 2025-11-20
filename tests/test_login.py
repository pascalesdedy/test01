from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    login.login("student", "Password123")
    assert "logged-in-successfully" in driver.current_url
    assert "Logged In Successfully" in dashboard.get_greeting_text()

def test_login_failure(driver):
    login = LoginPage(driver)
    login.login("wronguser", "wrongpass")
    error_message = login.get_error_message()   
    assert error_message == "Your username is invalid!"