from fetch_products import *
from concurrent.futures import ThreadPoolExecutor
import os


def extract_domain(url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?([^\/]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


def extract_products(url, idx):
    domain = extract_domain(url)

    products = []

    if domain == "virgio.com":
        products = fetch_virgio(url)
    elif domain == "tatacliq.com":
        products = fetch_tatacliq(url)
    elif domain == "nykaafashion.com":
        products = fetch_nykaa(url)
    elif domain == "westside.com":
        products = fetch_westside(url)

    with open(f"./products/URL_{idx + 1}.txt", "w") as file:
        for product in products:
            file.write(product + "\n")

    print(f"URL {idx + 1}: {len(products)}")


def run_in_parallel(values):
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(lambda pair: extract_products(pair[1], pair[0]), enumerate(values))


os.makedirs("products", exist_ok=True)

urls = ["https://www.virgio.com/collections/the-office-siren", "https://www.tatacliq.com/mens-clothing/c-msh11",
        "https://www.tatacliq.com/shirts/c-msh1116101?q=%3Arelevance%3Acategory%3AMSH1116101%3AinStockFlag%3Atrue%3Abrand%3AMBH11B26009",
        "https://www.nykaafashion.com/men/footwear/c/6857?f=category_filter=6865_6864_",
        "https://www.westside.com/collections/t-shirts-for-men"]

run_in_parallel(urls)
