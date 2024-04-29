# BestMovieDetailsAnalyticsUsingTableau-main-

Tableau Dashboard view ---[Here](https://public.tableau.com/app/profile/md.kawser.islam/viz/BestMovieDetails/Dashboard1?publish=yes)<br/>
Scraping Website--[website](https://www.imdb.com/list/ls000634294/?sort=list_order,asc&st_dt=&mode=detail&page=1)<br/>

![image](https://github.com/UtshoData/BestMovieDetailsAnalyticsUsingTableau/assets/157609050/6f7c71ea-3058-4e32-b86d-d50e013c7106)

#Problem Statement:

#1. A barchart of movies with maximum rate with duration and Movie Name <br>
#2.Star actor actress with Maximum rating (above 8)(depends on release date)(1997-2020)<br>
#3. Time Series Graph of Star actor actress with Maximum rating (depends on release date)<br>
#4. Circle graph of  Genre vs Rate (size of circle depends on the count of released movie per year)<br>
#5.Gross and Rate according to Name and Genre<br>

## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone [https://github.com/UtshoData/BestMovieDetailsAnalyticsUsingTableau-main-.git]
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads 
5. Run the scraper
```bash
python selenium_scraper/scraper.py --chromedriver_path <path_to_chromedriver>
```

