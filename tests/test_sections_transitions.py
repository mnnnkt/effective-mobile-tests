import pytest
import allure

from pages.main_page import MainPage


@pytest.mark.regress
@allure.title("Ссылка 'О нас' ведёт в раздел о компании")
def test_about_transition(main_page: MainPage):
    main_page.move_to_about_section()


@pytest.mark.regress
@allure.title("Ссылка 'Вакансии' ведёт в раздел специализаций")
def test_vacancies_transition(main_page: MainPage):
    main_page.move_to_vacancies_section()


@pytest.mark.regress
@allure.title("Ссылка 'Отзывы' ведёт в раздел отзывов специалистов")
def test_testimonials_transition(main_page: MainPage):
    main_page.move_to_testimonials_section()


@pytest.mark.regress
@allure.title("Ссылка 'Контакты' ведёт в раздел контактов")
def test_contact_transition(main_page: MainPage):
    main_page.move_to_contact_section()


@pytest.mark.regress
@allure.title("Ссылка 'Аутстафф' ведёт в раздел форматов сотрудничества")
def test_outstaff_transition(main_page: MainPage):
    main_page.move_to_outstaff_section()


@pytest.mark.regress
@allure.title("Ссылка 'Трудоустройство' ведёт в раздел форматов сотрудничества")
def test_employment_transition(main_page: MainPage):
    main_page.move_to_employment_section()


@pytest.mark.regress
@allure.title("Ссылка 'Консультация' ведёт в раздел контактов")
def test_consultation_transition(main_page: MainPage):
    main_page.move_to_consultation_section()
