import time

from behave import *
from features.pages.ContactPage import ContactPage


@given(u'user is on the homepage')
def step_impl(context):
    contact_page = ContactPage(context.driver)


@when(u'user clicks on contact menu it will open the pop-up of contact us')
def step_impl(context):
    contact_page = ContactPage(context.driver)
    contact_page.contact_page_nav()


@when(u'user enters the required details')
def step_impl(context):
    contact_page = ContactPage(context.driver)
    contact_page.enter_name("keerthana")
    contact_page.enter_email("keerthana.s@thinkinifnity.co.in")
    contact_page.enter_phone("9087690876")
    time.sleep(10)


@then(u'clicks on submit button')
def step_impl(context):
    time.sleep(10)
    contact_page = ContactPage(context.driver)
    contact_page.click_submit()
    time.sleep(10)

