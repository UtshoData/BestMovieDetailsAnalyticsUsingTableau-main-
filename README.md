# BestMovieDetailsAnalyticsUsingTableau-main-
## Introduction
IMDb stands for the Internet Movie Database. It is an online database of information related to films, television programs, home videos, video games, and streaming content.
I have scraped more than 700 data from 7 pages of this [website](https://www.imdb.com/list/ls000634294/?sort=list_order,asc&st_dt=&mode=detail&page=1) to find somw interesting findings.
## Dataset:
The dataset used for this analysis is the IMDB Dataset of top 700 movies .It contains information regarding top 700 movies .
Contents of the dataset are:<br/>
Series_Title = Name of the movie<br/>
Released_Year — Year at which that movie released<br/>
Certificate — Certificate earned by that movie<br/>
Runtime — Total runtime of the movie<br/>
Genre — Genre of the movie<br/>
IMDb_Rating — Rating of the movie at IMDB site<br/>
Overview — mini story/ summary<br/>
Meta_score — Score earned by the movie<br/>
Director — Name of the Director<br/>
Star1,Star2,Star3,Star4 — Names of the cast<br/>
No_of_votes — Total number of votes<br/>
Gross — Money earned by that movie<br/>
## Problem Statement:

1.A barchart of movies with maximum rate with duration and Movie Name <br>
2.Star actor actress with Maximum rating (above 8)(depends on release date)(1997-2020)<br>
3.Time Series Graph of Star actor actress with Maximum rating (depends on release date)<br>
4.Circle graph of  Genre vs Rate (size of circle depends on the count of released movie per year)<br>
5.Gross and Rate according to Name and Genre<br>

## Tableau Dashboard view ---[Here](https://public.tableau.com/app/profile/md.kawser.islam/viz/BestMovieDetails/Dashboard1?publish=yes)<br/>


![image](https://github.com/UtshoData/BestMovieDetailsAnalyticsUsingTableau-main-/assets/157609050/bc53b600-b298-43a0-9eba-ae77423c5ea5)
## Important Findings


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

