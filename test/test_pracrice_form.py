import allure

from model.pages.registration_form import RegistrationPage


def test_complete_and_submit_form():
    with allure.step("Открываем браузер и переходим на форму для заполнения"):
        registration_page = RegistrationPage()
        registration_page.open()
    with allure.step("Убрать баннеры и просколлить страницу"):
        registration_page.remove_banner()
        registration_page.scroll_page()
    with allure.step("Заполение фамилии и имени"):
        registration_page.fill_first_name('Fedor')
        registration_page.fill_last_name('Bubnov')
    with allure.step("Заполнение мыла"):
        registration_page.fill_email('fedor.bubnov_test@gmail.com')
    with allure.step("Выбор пола"):
        registration_page.choose_gender('Male')
    with allure.step("Заполнение телефона"):
        registration_page.fill_phone_number('9035033528')
    with allure.step("Заполнение даты рождения"):
        registration_page.fill_date_of_birthday(1990, 2, 18)
    with allure.step("Выбор предмета"):
        registration_page.choose_subject('Maths')
    with allure.step("Выбор хобби"):
        registration_page.choose_hobbies('1')
    with allure.step("Загрузка фото"):
        registration_page.upload_picture('foto.jpg')
    with allure.step("Заполенения адреса"):
        registration_page.current_adress('Test, 14/2')
    with allure.step("Выбор штата и города"):
        registration_page.state_select('Haryana')
        registration_page.city_select('Karnal')
    with allure.step("Клик на кнопку"):
        registration_page.submit_button()

    with allure.step("Проверка заполненой формы"):
        registration_page.assert_registered_user_info(
            full_name='Fedor Bubnov',
            email='fedor.bubnov_test@gmail.com',
            gender='Male',
            mobile_phone='9035033528',
            birthday='18 March,1990',
            subjects='Maths',
            hobbies='Sports',
            file_name='foto.jpg',
            address='Test, 14/2',
            state_and_city='Haryana Karnal'
        )