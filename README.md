# Scraping Amazon	

With this code, you can gather a few pieces of information about [Amazon Website](http://www.dropwizard.io/1.0.2/docs/) products using [Scrapy](https://scrapy.org/) spiders.

## Getting Started

To get product's information, this project seeks ASIN product codes on HTML response. Nevertheless, some changes in the Amazon Website layout can break the Scrapy spider.

### Prerequisites

To run this code, download Python 3 from [Python.org](https://www.python.org/). After install, download scrapy using pip installer:

```
pip install scrapy
```
### Usage

Inside project's folder, run:
```
scrapy crawl products -a keyword="samsung galaxy"
```
To save the results, use -o parameter:
```
scrapy crawl products -a keyword="samsung galaxy" -o samsung_galaxy.csv
```
You can add sponsored products in search:
```
scrapy crawl products -a keyword="samsung galaxy" -a sponsored=True -o samsung_galaxy.csv
```

## Built With

* [Scrapy](https://scrapy.org/) - A Fast and Powerful Scraping and Web Crawling Framework

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.