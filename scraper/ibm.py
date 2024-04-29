
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ["Name", "Release Date", "Certificate", "Duraton", "Genre", "Rate", "Metascore", "Overview", "Directors","Stars","Gross"]

def get_movie_details(row):
    details = row.text.split('\n')
    contents={}
    contents["Name"] = details[0].split('.')[1].split('(')[0]
    contents["Release Date"] = details[0].split('(')[1].strip(')')
    try:
         contents["Certificate"] = details[1].split('|')[0]
    except:
         contents["Certificate"] =" "
  
    contents["Duration"] = details[1].split('|')[1]
    try:
        contents["Genre"] = details[1].split('|')[2]
    except:
        contents["Genre"]= details[1].split('|')[1]   
    contents["Rate"] = details[2]
    contents["Metascore"] = details[4].split(' ')[0]
    contents["Overview"] = details[5]
    try:
        contents["Directors"] = details[6].split('|')[0].split(':')[1]
    except:
        contents["Directors"] = ""
    try:
        contents["Stars"] = details[6].split('|')[1].split(':')[1]
    except:
        contents["Stars"] = details[6].split(':')[1]

    try:
         contents["Gross"] = details[7].split('|')[1].split(':')[1]
    except:
         contents["Gross"]= ""
    print(contents["Duration"])
    return contents  


def main():
    webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
    movie_data = []
    for page_id in range(1,8): 
        driver = webdriver.Chrome()
        url = f"https://www.imdb.com/list/ls000634294/?sort=list_order,asc&st_dt=&mode=detail&page={page_id}"
        driver.get(url)
        time.sleep(5)
        movie = driver.find_element(By.ID, 'main')
        rows = movie.find_elements(By.CLASS_NAME, 'lister-item-content')
        row_contents=[]
        for idx, row in enumerate(rows):
            movie_data.append(get_movie_details(row))
    
        
    df = pd.DataFrame(data=movie_data, columns=columns)
    df.to_csv("best_movie_details.csv", index=False)
    
    driver.close()
    return

if __name__ == "__main__":
    main()