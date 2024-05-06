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

1.What are the top 10 movies based on the number of votes on IMDb?<br>
2.How many movies were released in each year according to IMDb’s database<br/>
3.Top 10 Genre count
4.Circle graph of  Genre vs Rate (size of circle depends on the count of released movie per year)<br>
5.Gross and Rate according to Name and Genre<br>
6.How many movies have each certificate (e.g., G, PG, PG-13, R, etc.) on IMDb<br/>
7.Which are the top 10 genres based on Metascore, and what are their average Metascore ratings<br/>

## Tableau Dashboard view ---[Here](https://public.tableau.com/app/profile/md.kawser.islam/viz/BestMovieDetails/Dashboard1?publish=yes)<br/>

![image](https://github.com/UtshoData/BestMovieDetailsAnalyticsUsingTableau-main-/assets/157609050/19759045-1574-45db-9c55-d3bd221ac928)

## Important Findings
1.Analyzing movies with the highest number of votes can provide an understanding of which films have garnered the most attention and engagement from the IMDb user community.Shawshank Redemption is the most top rated (9.3) compared to others.<br/>
2. Examining the distribution of movie certificates can offer insights into the audience demographics and preferences. For example, a higher number of movies with a " R " certificate may indicate a focus on aa dult audience.Most rated movies are mostly under R certification and then  PG-13 certificate.<br/>
3.Observing the distribution of movies over the years can reveal trends in the film industry. A spike in a particular year might be associated with a significant cultural or technological shift after 1998.<br/>
4.Analyzing the total gross for movies each year can highlight the financial success of the film industry over time. Avarter in the gross may coincide with major blockbuster releases or economic factors and the gross was $720M  and in The Dark Night was in the second position.<br/>
5.Audiances love the Action, Adventure and Science Fiction genre of movies. Cz the maximum rate was 8.80 and also more 30 movies is being produced in this sector.<br/>
6.Comparing Metascore ratings with for top 10 genres can offer a perspective on how critical reviews align with audience opinions. Consistency or divergence between the two metrics may indicate interesting dynamics in genre preferences.

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

