import time

from selene import browser, have, by, command, be
from model.resourse import path


class RegistrationPage:

    def open(self):
        browser.open('automation-practice-form')

    def remove_banner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("document.querySelector('body').style.position = 'relative'")

    def scroll_page(self):
        browser.element('#submit').perform(command.js.scroll_into_view)

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_nane):
        browser.element("#lastName").type(last_nane)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def choose_gender(self, value):
        browser.element(by.text(value)).perform(command.js.click)

    def fill_phone_number(self, number):
        browser.element("#userNumber").type(number)

    def fill_date_of_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f"option[value='{year}']").click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def choose_subject(self, subject):
        browser.element("#subjectsInput").click().type(subject).press_enter()

    def choose_hobbies(self, value):
        browser.element(f'#hobbies-checkbox-{value}').perform(command.js.click())

    def upload_picture(self, filename):
        browser.element('#uploadPicture').set_value(path(filename))

    def current_adress(self, *args):
        browser.element('#currentAddress').type(*args)

    def state_select(self, state):
        browser.element('#state').click().element(by.text(state)).click()

    def city_select(self, city):
        browser.element('#city').click().element(by.text(city)).click()

    def submit_button(self):
        browser.element('#submit').with_(timeout=5).click()

    def assert_registered_user_info(self, full_name, email, gender, mobile_phone, birthday, subjects, hobbies,
                                    file_name, address, state_and_city):
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_phone,
                birthday,
                subjects,
                hobbies,
                file_name,
                address,
                state_and_city
            )
        )