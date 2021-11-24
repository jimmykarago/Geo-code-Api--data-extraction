# race_track_visualizations
I am a motorsport fan,  I wanted to visualize the locations of different race tracks around the world on powerbi. I created tracks.py a program that scraps race tracks names from https://www.racingcircuits.info/a-to-z-circuit-list.html. The program also geo_codes the race circuits names using the google maps api and stores the track names,track country ,longitude and lattitude information on an sqlite database. I converted the sqlite database to an excel file and named it race_tracks.xlsx'

I also wanted to classify the track location based on the contintnent they are located at. The problem was I did not have the continenet data. I created the world.py program to scrape table of countries and the continents they belonged to from https://statisticstimes.com/geography/countries-by-continents.php I created a worksheet named World_map within the race_tracks workbook and stored the scraped data there then saved the excel files as race_track_World_map.

Using the vlookup function I was able to view which specific continent a race track belonged in this made it easier to visulise the information on powerbi. 
