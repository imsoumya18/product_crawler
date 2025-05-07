# Product Crawler

This project is a Python-based product crawler that scrapes product URLs from specific e-commerce websites, using
Selenium for browser automation. The project targets the following domains:

* [Virgio](https://www.virgio.com/)
* [TataCliq](https://www.tatacliq.com/)
* [Nykaa Fashion](https://www.nykaafashion.com/)
* [Westside](https://www.westside.com/)

The output is saved in a `Products` folder, with each file named sequentially as `URL_1.txt`, `URL_2.txt`, etc.

## Features

1. **Customizable Product Limit**: The crawler fetches up to 100 product URLs per given link by default, but this value
   can be adjusted by modifying the `no_of_products` parameter.
2. **Output Format**: Each file contains the product URLs scraped from the corresponding input webpage.
3. **Domain-Specific Logic**: The scraper is designed to handle the specific structure of the targeted e-commerce
   websites.
4. **No Proxies Used**: Due to the absence of paid proxy services, the project does not use proxy rotation.

## Notes

* **Proxies**: The project does not use proxies to avoid IP bans, as no paid proxies were available.
* **Headless Mode**: Although Selenium supports headless mode for running the browser in the background, this feature
  was not implemented due to time constraints.
* **Device Limitations**: Running the crawler on too many URLs simultaneously may strain devices with limited processing
  power.

## Parameters

* `no_of_products`: Default is 100. You can change this value to limit the number of products fetched per URL.

## Limitations

1. No proxy support.
2. Limited URL input due to hardware constraints.
3. No headless mode for reduced resource consumption.

## Future Enhancements

1. Add proxy support for better scalability.
2. Implement headless mode for resource efficiency.
3. Optimize the script for parallel processing to handle more URLs efficiently.