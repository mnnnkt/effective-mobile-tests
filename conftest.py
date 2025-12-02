from playwright.sync_api import Page
import pytest

from pages.main_page import MainPage


@pytest.fixture
def main_page(page: Page) -> MainPage:
    main_page = MainPage(page)
    main_page.open_main_page()
    return main_page
