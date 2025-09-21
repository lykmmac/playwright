import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(3000) # Wait to ensure the page is fully loaded
    
    # Navigate to the Google page
    page.goto("https://www.google.com/ncr")

    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except:
        print("No popup")

    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.INGORECASE))
