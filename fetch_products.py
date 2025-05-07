from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import re


def get_driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


no_of_products = 100


def fetch_virgio(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(7)

    # Define variables for human-like scrolling
    scroll_pause_time = 0.75  # Pause between scrolls (adjust for realism)
    scroll_increment = 300  # Pixels scrolled each time
    max_scroll_attempts = 100  # Max scroll attempts to avoid infinite loop

    # Track scroll progress
    last_scroll_position = 0
    attempts = 0

    product_links = set()

    while True:
        # Get the page source
        page_source = driver.page_source

        # Regular expression to extract product links
        product_link_pattern = re.compile(r'<a[^>]*\bhref=[\'"](/products/[^\'"]*)[\'"]')
        product_links.update(product_link_pattern.findall(page_source))
        # print(len(product_links))

        # Scroll down incrementally
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        attempts += 1

        # Wait for the page to load content
        time.sleep(scroll_pause_time + random.uniform(0.5, 1.5))  # Add random variation for realism

        # Check the new scroll position
        new_scroll_position = driver.execute_script("return window.pageYOffset;")

        # Break if no further scrolling is possible or max attempts are reached
        if new_scroll_position == last_scroll_position or attempts >= max_scroll_attempts or len(
                product_links) >= no_of_products:
            break

        last_scroll_position = new_scroll_position

    return ['https://www.virgio.com' + item for item in product_links]


def fetch_tatacliq(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(7)

    product_links = set()
    popup_closed = False

    for _ in range(20):
        if not popup_closed:
            try:
                # Locate the button using XPATH for a single class name with spaces
                button = driver.find_element(By.XPATH, "//button[contains(@class, 'No thanks')]")
                button.click()
                # print("Pop-up closed!")
                popup_closed = True
            except NoSuchElementException:
                # print("Button does not exist.")
                pass

        try:
            # Wait for 2 seconds before each click
            time.sleep(2)

            # Get the page source
            page_source = driver.page_source

            # Regular expression to extract product links
            product_link_pattern = re.compile(r'https://www\.tatacliq\.com/[a-zA-Z0-9\-]+/p-mp\d+')
            product_links.update(product_link_pattern.findall(page_source))
            # print(len(product_links))

            # Find and click the button
            wait = WebDriverWait(driver, 10)
            button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ShowMoreButtonPlp__button')]")))

            time.sleep(2)

            if button.text != "Show More Products" or len(product_links) >= no_of_products:
                break

            button.click()

            time.sleep(2)
        except NoSuchElementException:
            # print("Button not found. Exiting loop.")
            pass

    # Extract href from the <a> tag within each div
    return product_links


def fetch_nykaa(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(7)

    # Define variables for human-like scrolling
    scroll_pause_time = 0.75  # Pause between scrolls (adjust for realism)
    scroll_increment = 300  # Pixels scrolled each time
    max_scroll_attempts = 100  # Max scroll attempts to avoid infinite loop

    # Track scroll progress
    last_scroll_position = 0
    attempts = 0

    product_links = set()
    popup_closed = False

    while True:
        if not popup_closed:
            try:
                # Locate the button using XPATH for a single class name with spaces
                button = driver.find_element(By.XPATH, "//button[contains(@class, 'No thanks')]")
                button.click()
                # print("Pop-up closed!")
                popup_closed = True
            except NoSuchElementException:
                # print("Button does not exist.")
                pass

        # Get the page source
        page_source = driver.page_source

        # Regular expression to extract product links
        product_link_pattern = re.compile(r'href="([^"]+)"[^>]*data-at="product"')
        product_links.update(product_link_pattern.findall(page_source))
        # print(len(product_links))

        # Scroll down incrementally
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        attempts += 1

        # Wait for the page to load content
        time.sleep(scroll_pause_time + random.uniform(0.5, 1.5))  # Add random variation for realism

        # Check the new scroll position
        new_scroll_position = driver.execute_script("return window.pageYOffset;")

        # Break if no further scrolling is possible or max attempts are reached
        if new_scroll_position == last_scroll_position or attempts >= max_scroll_attempts or len(
                product_links) >= no_of_products:
            break

        last_scroll_position = new_scroll_position

    return ['https://www.nykaafashion.com' + p for p in product_links]


def fetch_westside(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(7)

    # Define variables for human-like scrolling
    scroll_pause_time = 0.75  # Pause between scrolls (adjust for realism)
    scroll_increment = 300  # Pixels scrolled each time
    max_scroll_attempts = 100  # Max scroll attempts to avoid infinite loop

    # Track scroll progress
    last_scroll_position = 0
    attempts = 0

    product_links = set()
    popup_closed = False

    while True:
        if not popup_closed:
            try:
                # Locate the button using XPATH
                button = driver.find_element(By.XPATH, "//button[contains(@id, 'moe-dontallow_button')]")
                button.click()
                # print("Pop-up closed!")
                popup_closed = True
            except NoSuchElementException:
                # print("Button does not exist.")
                pass

        # Get the page source
        page_source = driver.page_source

        # Regular expression to extract product links
        product_link_pattern = re.compile(r'https://www\.westside\.com/products/[a-zA-Z0-9\-]+')
        product_links.update(product_link_pattern.findall(page_source))
        # print(len(product_links))

        # Scroll down incrementally
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        attempts += 1

        # Wait for the page to load content
        time.sleep(scroll_pause_time + random.uniform(0.5, 1.5))  # Add random variation for realism

        # Check the new scroll position
        new_scroll_position = driver.execute_script("return window.pageYOffset;")

        # Break if no further scrolling is possible or max attempts are reached
        if new_scroll_position == last_scroll_position or attempts >= max_scroll_attempts or len(
                product_links) >= no_of_products:
            break

        last_scroll_position = new_scroll_position

    return product_links
