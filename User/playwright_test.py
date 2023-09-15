import time

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        dir_path = fr"/home/instagramstory/instagram-story/Profile"
        try:
            browser = p.chromium.launch_persistent_context(
                channel="chrome",
                user_data_dir=dir_path,
                headless=True,
            )
        except Exception as e:
            print(f'browser error = {e}')
            return

        website = f'https://web.telegram.org/k/'
        pages = browser.pages
        default_page = pages[0]

        default_page.goto(website, timeout=60000)

        time.sleep(10)
        try:
            default_page.locator('//div[@class="input-search"]/input').type('', timeout=120000)
        except Exception as e:
            print(f'input error = {e}')

        try:
            default_page.screenshot(path='screenshot.png', full_page=True)
        except Exception as e:
            print(f'screenshot error = {e}')
        browser.close()


if __name__ == '__main__':
    main()
