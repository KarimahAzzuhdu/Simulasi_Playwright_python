import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    #before each
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    yield

    #after each

def test_login_process(page: Page):
    #Check Login Page's Attibutes
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_text("Forgot your password?")).to_be_visible()

    #Login Process
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #Check user successfully logs in
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

def test_logout_process(page: Page):
    #Prerequisites : User already logs in
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #Logout Process
    page.locator('.oxd-userdropdown-tab').click()
    page.get_by_role("menuitem", name="Logout").click()

    #Check user successfully logs out
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

def test_invalid_creds(page: Page):
    #Login with invalid creds Process
    page.get_by_placeholder("Username").fill("Invalid")
    page.get_by_placeholder("Password").fill("invalid")
    page.get_by_role("button", name="Login").click()

    #Check invalid creds alert message
    expect(page.get_by_role("alert")).to_be_visible()

def test_blank_field(page: Page):
    #Login with blank field Process
    page.get_by_role("button", name="Login").click()

    #Check required message
    expect(page.get_by_text("UsernameRequired")).to_be_visible()
    expect(page.get_by_text("PasswordRequired")).to_be_visible()

def test_forgot_pass_process(page: Page):
    page.get_by_text("Forgot your password?").click()

    #Check Forgot Password Page's Attribute
    expect(page.get_by_role("button", name="Cancel")).to_be_visible()
    expect(page.get_by_role("button", name="Reset Password")).to_be_visible()
    expect(page.get_by_placeholder("Username")).to_be_visible()

    #Forgot Password Process
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_role("button", name="Reset Password").click()
    
    #Check user successfully reset their password
    expect(page.get_by_text("Reset Password link sent successfullyA reset password link has been sent to you")).to_be_visible()