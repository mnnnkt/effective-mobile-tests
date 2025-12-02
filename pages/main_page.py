from playwright.sync_api import Page, expect
import allure


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.main_header = page.get_by_text("Ваша карьера в IT")
        self.about_section = page.locator("section").filter(has=page.get_by_role("heading", name="О компании"))
        self.specializations_section = page.locator("section").filter(has=page.get_by_role("heading", name="Кого мы ищем"))
        self.testimonials_section = page.locator("section").filter(has=page.get_by_role("heading", name="Отзывы специалистов"))
        self.contact_section = page.locator("section").filter(has=page.get_by_role("heading", name="Свяжитесь с нами"))
        self.services_section = page.locator("section").filter(has=page.get_by_role("heading", name="Форматы сотрудничества"))
        self.about_link = page.get_by_role("link", name="О нас")
        self.vacancies_link = page.get_by_role("link", name="Вакансии", exact=True)
        self.testimonials_link = page.get_by_role("link", name="Отзывы")
        self.contact_link = page.get_by_role("link", name="Контакты")
        self.outstaff_link = page.get_by_role("link", name="Аутстафф")
        self.employment_link = page.get_by_role("link", name="Трудоустройство")
        self.consultation_link = page.get_by_role("link", name="Консультация")
        self.main_link = "https://www.effective-mobile.ru/"
        self.about_postfix = "#about"
        self.vacancies_postfix = "#specializations"
        self.testimonials_postfix = "#testimonials"
        self.contact_postfix = "#contact"
        self.outstaff_postfix = "#services"
        self.employment_postfix = "#services"
        self.consultation_postfix = "#contact"

    def open_main_page(self):
        with allure.step("Переход на главную страницу"):
            self.page.goto(self.main_link)
            expect(self.main_header).to_be_visible()

    def move_to_any_section(self, link, postfix, section):
        with allure.step("Нажатие на ссылку"):
            link.click()
        with allure.step("URL правильный"):
            expect(self.page).to_have_url(self.main_link + postfix)
        with allure.step("Раздел в области видимости"):
            expect(section).to_be_in_viewport()

    def move_to_about_section(self):
        self.move_to_any_section(
            self.about_link,
            self.about_postfix,
            self.about_section
        )

    def move_to_vacancies_section(self):
        self.move_to_any_section(
            self.vacancies_link,
            self.vacancies_postfix,
            self.specializations_section
        )

    def move_to_testimonials_section(self):
        self.move_to_any_section(
            self.testimonials_link,
            self.testimonials_postfix,
            self.testimonials_section
        )

    def move_to_contact_section(self):
        self.move_to_any_section(
            self.contact_link,
            self.contact_postfix,
            self.contact_section
        )

    def move_to_outstaff_section(self):
        self.move_to_any_section(
            self.outstaff_link,
            self.outstaff_postfix,
            self.services_section
        )

    def move_to_employment_section(self):
        self.move_to_any_section(
            self.employment_link,
            self.employment_postfix,
            self.services_section
        )

    def move_to_consultation_section(self):
        self.move_to_any_section(
            self.consultation_link,
            self.consultation_postfix,
            self.contact_section
        )
