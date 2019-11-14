### Background Quote Generator
This repository has scripts to first scrape quotes from a list of authors off of Good Reads. Then, the quotes can be used to create desktop backgrounds.

## Installation
1. `git clone https://github.com/Connorpar/background_quotes.git`
2. Install Dependencies

## Dependencies
* pandas
* Pillow
* BeautifulSoup
* requests

## Running
1. Edit the Authors list in quote_scraper.py 
2. Run `python quote_scraper.py`
3. Store background images in a folder named "background_images" (Can Download mine from link below)
4. Store fonts in a folder named "fonts" (Can Download mine from link below)
5. Edit the Number of desired backgrounds and the location of the produced backgrounds in write_background.py
6. Run `python write_background.py`

## Images and Fonts links
* Images: http://connorparish.com/extra_files/background_images.zip
* Fonts: http://connorparish.com/extra_files/fonts.zip