from playwright.sync_api import sync_playwright
import os

def test_title_screen():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file
        # Assuming the script runs from the repo root
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Wait for the title screen to be visible
        page.wait_for_selector("#titleScreen")

        # Check if the title text is correct
        title_text = page.locator("#titleLogo").inner_text()
        print(f"Title Text: {title_text}")

        # Take a screenshot of the title screen
        page.screenshot(path="verification/title_screen.png")

        # Simulate pressing Enter to start the game
        page.keyboard.press("Enter")

        # Wait for title screen to disappear
        page.wait_for_selector("#titleScreen", state="hidden")

        # Wait a bit for game to start and enemy to spawn (Zone 1)
        page.wait_for_timeout(2000)

        # Take a screenshot of the gameplay
        page.screenshot(path="verification/gameplay_start.png")

        browser.close()

if __name__ == "__main__":
    test_title_screen()
