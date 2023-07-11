# Geo code Api- data extraction
I am a motorsport fan,  I wanted to visualize the locations of different race tracks around the world on Powerbi. I created tracks.py a program that scraps race tracks names from https://www.racingcircuits.info/a-to-z-circuit-list.html. The program also geo_codes the race circuit names using google maps API and stores the track names, track country, longitude and latitude information on an SQLite database. I converted the SQLite database to an Excel file and named it race_tracks.xlsx'

I also wanted to classify the track location based on the continent they are located in. The problem was I did not have the continent data. I created the world.py program to scrape a table of countries and the continents they belonged to from https://statisticstimes.com/geography/countries-by-continents.php I created a worksheet named World_map within the race_tracks workbook and stored the scraped data there then saved the excel files as race_track_World_map.

Using the Vlookup function in Excel I was able to view which specific continent a race track belonged in this made it easier to visualise the information on Powerbi. 
