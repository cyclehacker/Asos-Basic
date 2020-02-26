# Skeleton Asos product category crawler

Configured to scrape the mens shoes categories product names and prices.

Change or add top level product category url(s) in the 'start_url' list to crawl different categories, e.g.:

'https://www.asos.com/men/jeans/cat/?cid=4208&nlid=mw|clothing|shop+by+product'

Dump to .csv, .json, xml etc using scrapy -o command line argument:

scrapy crawl asos_shoes -o output_filename.csv

# Future updates:

- Expand range of data crawled to include all available data.
- Write tests to Travis
- Add user input to select product categories to be crawled.
- Add support for different market domains.
- Add Flask based web app to receive user input.
- Add crawled data to database.
- Create output files and email to user.
- Make categories stored in the database available for download.
- Add daily monitoring tests to ensure continuity of service.

