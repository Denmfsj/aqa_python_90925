import time
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # browser.contexts[0].set_default_timeout(3000)  # для всіх page буде 3 sec

    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com")
    page.set_default_timeout(7000) # 7 sec зазамовчуванням якщо іншого не сказано

    broken_image_link_loc = page.locator('//a[text() = "Broken Images"]')
    broken_image_link_loc.click(timeout=15000)  # 15 sec

    broken_image_text_loc = page.locator('//h3[text() = "Broken Images"]')
    print(broken_image_text_loc.text_content(timeout=2000))

    page.goto("https://the-internet.herokuapp.com")
    page.wait_for_timeout(1000)

    # page.get_by_text('Form Authentication').click()  # <a href=>
    #
    # inputs = page.locator('//input')
    #
    # inputs.nth(0).fill('Den')
    # page.wait_for_timeout(2000)
    #
    # inputs.nth(0).fill('Den23')  # стирає все і пише
    # page.wait_for_timeout(2000)
    #
    # inputs.nth(0).press('Backspace')  # press - спец клавіші
    # page.wait_for_timeout(2000)
    # inputs.nth(0).type('gg')  # друкування
    #
    # page.get_by_role('button').click()  # натиснув едину кнопку на сторінці, це login
    #
    # expected_element = page.get_by_text('Your username is invalid!')  # вказав який локатор шукати
    #
    # expect(expected_element).to_be_visible(timeout=3000)  # первіряю, що локато з'явився на сторінці
    print('done')


    page.goto("https://the-internet.herokuapp.com")

    page.get_by_text('checkboxes').click()

    checkbox_1 = page.get_by_role('checkbox').nth(0)
    checkbox_2 = page.get_by_role('checkbox').nth(1)


    print('checkbox_2 is checked: ', checkbox_2.is_checked())
    page.wait_for_timeout(500)
    checkbox_2.click()
    print('checkbox_2 is checked: ', checkbox_2.is_checked())
    page.wait_for_timeout(500)
    checkbox_2.click()
    print('checkbox_2 is checked: ', checkbox_2.is_checked())

    # page.mouse.move()

    page.goto("https://the-internet.herokuapp.com")

    page.get_by_text('Dropdown').click()
    page.wait_for_timeout(1000)

    page.select_option('#dropdown', index=2)
    page.wait_for_timeout(1000)
    page.select_option('#dropdown', value='1')
    page.wait_for_timeout(1000)
    print('Selected is')
    print(page.eval_on_selector(
        "#dropdown",
        "el => el.options[el.selectedIndex].text"
    ))

    page.select_option('#dropdown', label='Option 2')
    page.wait_for_timeout(1000)

    print('Selected is')
    print(page.eval_on_selector(
        "#dropdown",
        "el => el.options[el.selectedIndex].text"
    ))







    # page.mouse.wheel(0, 1000)  # скрол вниз на 1000  пікселів
    # page.wait_for_timeout(1000)
    # page.mouse.wheel(0, -1000)  # скрол вгору на 1000  пікселів

    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # evaluate - виконати js код
    # page.wait_for_timeout(1000)

    page.wait_for_timeout(5000)  # час очікування. Лишати коментар для чого це потрібно == time.sleep(5)


