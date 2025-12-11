#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:14:11 2025

@author: aaronfoote
"""

#Presidential Speech Analysis

import requests
import bs4
import datetime
import pandas as pd


#Create list of web addresses to scrape the text of speehces from the Miller Center at UVA
washington_URLs = ["https://millercenter.org/the-presidency/presidential-speeches/april-30-1789-first-inaugural-address", "https://millercenter.org/the-presidency/presidential-speeches/october-3-1789-thanksgiving-proclamation", "https://millercenter.org/the-presidency/presidential-speeches/january-8-1790-first-annual-message-congress",
                   "https://millercenter.org/the-presidency/presidential-speeches/december-8-1790-second-annual-message-congress", "https://millercenter.org/the-presidency/presidential-speeches/december-29-1790-talk-chiefs-and-counselors-seneca-nation", "https://millercenter.org/the-presidency/presidential-speeches/october-25-1791-third-annual-message-congress",
                   "https://millercenter.org/the-presidency/presidential-speeches/april-5-1792-veto-message-congressional-redistricting", "https://millercenter.org/the-presidency/presidential-speeches/november-6-1792-fourth-annual-message-congress", "https://millercenter.org/the-presidency/presidential-speeches/december-12-1792-proclamation-against-crimes-against-cherokee", 
                   "https://millercenter.org/the-presidency/presidential-speeches/august-7-1794-proclamation-against-opposition-execution-laws", "https://millercenter.org/the-presidency/presidential-speeches/september-25-1794-proclamation-militia-service", "https://millercenter.org/the-presidency/presidential-speeches/november-19-1794-sixth-annual-message-congress", 
                   "https://millercenter.org/the-presidency/presidential-speeches/july-10-1795-proclamation-pardons-western-pennsylvania", "https://millercenter.org/the-presidency/presidential-speeches/december-8-1795-seventh-annual-message-congress",  "https://millercenter.org/the-presidency/presidential-speeches/march-30-1796-message-house-representatives-declining-submit", 
                   "https://millercenter.org/the-presidency/presidential-speeches/august-29-1796-talk-cherokee-nation", "https://millercenter.org/the-presidency/presidential-speeches/september-19-1796-farewell-address", "https://millercenter.org/the-presidency/presidential-speeches/december-7-1796-eighth-annual-message-congress"]

#Corresponding list of dates that each speech was given.  Useful for tracking changes over time
washington_speech_dates = [[1789, 4, 30], [1789, 10, 3], [1790, 1, 8], [1790, 12, 8], [1790, 12, 29], [1791, 10, 25], [1792, 4, 5], [1792, 11, 6], [1792, 12, 12], [1793, 3, 4], [1793, 4, 22], [1793, 12, 3], [1794, 8, 7], [1794, 9, 25], [1794, 11, 19], 
[1795, 10, 10], [1795, 12, 8], [1796, 3, 30], [1796, 8, 29], [1796, 9, 19], [1796, 12, 7]]



#Create list of web addresses to scrape the text of John Adam's speeches from the Miller Center
adams_URLs = ['https://millercenter.org/the-presidency/presidential-speeches/march-4-1797-inaugural-address', 'https://millercenter.org/the-presidency/presidential-speeches/may-16-1797-special-session-message-congress-xyz-affair',
              'https://millercenter.org/the-presidency/presidential-speeches/november-22-1797-first-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/march-23-1798-proclamation-day-fasting-humiliation-and-prayer',
              'https://millercenter.org/the-presidency/presidential-speeches/december-8-1798-second-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/december-3-1799-third-annual-message',
              'https://millercenter.org/the-presidency/presidential-speeches/may-21-1800-proclamation-pardons-those-engaged-fries-rebellion', 'https://millercenter.org/the-presidency/presidential-speeches/november-22-1800-fourth-annual-message'] 
#corresponding dates of each speech in order              
adams_speech_dates = [[1797, 3, 4], [1797, 5, 16], [1797, 11, 22], [1798, 3, 23], [1798, 12, 8], [1799, 12, 3], [1800, 5, 21], [1800, 11, 22]] 

#list of web addresses to scrape text of Thomas Jefferson's speeches 
jefferson_URLs = ['https://millercenter.org/the-presidency/presidential-speeches/march-4-1801-first-inaugural-address', 'https://millercenter.org/the-presidency/presidential-speeches/july-12-1801-reply-new-haven-remonstrance', 'https://millercenter.org/the-presidency/presidential-speeches/december-8-1801-first-annual-message',
                  'https://millercenter.org/the-presidency/presidential-speeches/january-1-1802-response-danbury-baptist-association', 'https://millercenter.org/the-presidency/presidential-speeches/november-3-1802-address-brother-handsome-lake',
                  'https://millercenter.org/the-presidency/presidential-speeches/december-15-1802-second-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/january-18-1803-special-message-congress-indian-policy',
                  'https://millercenter.org/the-presidency/presidential-speeches/june-20-1803-instructions-captain-lewis', 'https://millercenter.org/the-presidency/presidential-speeches/october-17-1803-third-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/december-17-1803-address-brothers-choctaw-nation',
                  'https://millercenter.org/the-presidency/presidential-speeches/november-8-1804-fourth-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/march-4-1805-second-inaugural-address', 'https://millercenter.org/the-presidency/presidential-speeches/december-3-1805-fifth-annual-message',
                  'https://millercenter.org/the-presidency/presidential-speeches/december-6-1805-special-message-congress-foreign-policy', 'https://millercenter.org/the-presidency/presidential-speeches/january-10-1806-address-chiefs-cherokee-nation', 'https://millercenter.org/the-presidency/presidential-speeches/november-27-1806-proclamation-spanish-territory',
                  'https://millercenter.org/the-presidency/presidential-speeches/december-2-1806-sixth-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/december-30-1806-address-wolf-and-people-mandan-nation', 'https://millercenter.org/the-presidency/presidential-speeches/january-22-1807-special-message-congress-burr-conspiracy',
                  'https://millercenter.org/the-presidency/presidential-speeches/february-10-1807-special-message-congress-gun-boats', 'https://millercenter.org/the-presidency/presidential-speeches/july-2-1807-proclamation-response-chesapeake-affair',
                  'https://millercenter.org/the-presidency/presidential-speeches/october-27-1807-seventh-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/november-8-1808-eighth-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/april-3-1809-message-inhabitants-albemarle-county']

jefferson_speech_dates = [[1801, 3, 4], [1801, 7, 12], [1801, 12, 8], [1802, 1, 1], [1802, 11, 3], [1802, 12, 5], [1803, 1, 18], [1803, 6, 20], [1803, 10, 17], [1803, 12, 17], [1804, 11, 8], [1805, 3, 4], [1805, 12, 3], [1805, 12, 6], [1806, 1, 10], [1806, 11, 27], [1806, 12, 2], [1806, 12, 30], [1807, 1, 22], [1807, 2, 10], [1807, 7, 2],
                          [1807, 10, 27], [1808, 11, 8], [1809, 4, 3]]




#Function used to scape speech text from each URL, extract relevant text, output text as a list where each
#element corresponds to a speech.  There are 21 speeches total
def compile_speeches(president_URLs):
    speech_list = []
    for url in president_URLs:
        current_speech = requests.get(url)
        current_soup = bs4.BeautifulSoup(current_speech.text, "lxml")
        #select for the specific part of the website that contains the speech text
        current_speech_text = current_soup.find_all('div', class_="view-transcript")[0].getText()
        #processing step to remove the word "Transcript" from the beginning of each speech
        current_speech_text = current_speech_text[10:]
        speech_list.append(current_speech_text)
    return speech_list

washington_formatted_speech_dates = []
for date in washington_speech_dates:
    formatted_date = datetime.date(date[0], date[1], date[2])
    washington_formatted_speech_dates.append(formatted_date)

adams_formatted_speech_dates = []
for date in adams_speech_dates:
    formatted_date = datetime.date(date[0], date[1], date[2])
    adams_formatted_speech_dates.append(formatted_date)

jefferson_formatted_speech_dates = []
for date in jefferson_speech_dates:
    formatted_date = datetime.date(date[0], date[1], date[2])
    jefferson_formatted_speech_dates.append(formatted_date)    

washington_speech_list = compile_speeches(washington_URLs)
adams_speech_list = compile_speeches(adams_URLs)
jefferson_speech_list = compile_speeches(jefferson_URLs)

washington_df = pd.DataFrame(list(zip(washington_formatted_speech_dates, washington_speech_list)), columns=['Speech_Date', 'Speech_Text'])
adams_df = pd.DataFrame(list(zip(adams_formatted_speech_dates, adams_speech_list)), columns=['Speech_Date', 'Speech_Text'])
jefferson_df = pd.DataFrame(list(zip(jefferson_formatted_speech_dates, jefferson_speech_list)), columns=['Speech_Date', 'Speech_Text'])

def output_president_dfs(washington_df, adams_df, jefferson_df, washington_file_path="washington_speeches.csv", adams_file_path="adams_speeches.csv", jefferson_file_path="jefferson_speeches.csv"):
    washington_df.to_csv(washington_file_path, index=False)
    adams_df.to_csv(adams_file_path, index=False)
    jefferson_df.to_csv(jefferson_file_path, index=False)
    print(f"DataFrames saved to {washington_file_path, adams_file_path, jefferson_file_path}")

if __name__=="__main__":
    output_president_dfs(washington_df, adams_df, jefferson_df)
    

    


