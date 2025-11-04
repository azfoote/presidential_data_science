#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:14:11 2025

@author: aaronfoote
"""

#Presidential Speech Analysis

import requests
import bs4


#Create list of web addresses to scrape the text of speehces from the Miller Center at UVA
Washington_URLs = ["https://millercenter.org/the-presidency/presidential-speeches/april-30-1789-first-inaugural-address", "https://millercenter.org/the-presidency/presidential-speeches/october-3-1789-thanksgiving-proclamation", "https://millercenter.org/the-presidency/presidential-speeches/january-8-1790-first-annual-message-congress",
"https://millercenter.org/the-presidency/presidential-speeches/december-8-1790-second-annual-message-congress", "https://millercenter.org/the-presidency/presidential-speeches/december-29-1790-talk-chiefs-and-counselors-seneca-nation", "https://millercenter.org/the-presidency/presidential-speeches/october-25-1791-third-annual-message-congress",
"https://millercenter.org/the-presidency/presidential-speeches/april-5-1792-veto-message-congressional-redistricting", "https://millercenter.org/the-presidency/presidential-speeches/november-6-1792-fourth-annual-message-congress", "https://millercenter.org/the-presidency/presidential-speeches/december-12-1792-proclamation-against-crimes-against-cherokee",
"https://millercenter.org/the-presidency/presidential-speeches/march-4-1793-second-inaugural-address", "https://millercenter.org/the-presidency/presidential-speeches/april-22-1793-proclamation-neutrality", "https://millercenter.org/the-presidency/presidential-speeches/december-3-1793-fifth-annual-message-congress",
"https://millercenter.org/the-presidency/presidential-speeches/august-7-1794-proclamation-against-opposition-execution-laws", "https://millercenter.org/the-presidency/presidential-speeches/september-25-1794-proclamation-militia-service", "https://millercenter.org/the-presidency/presidential-speeches/november-19-1794-sixth-annual-message-congress", 
 "https://millercenter.org/the-presidency/presidential-speeches/july-10-1795-proclamation-pardons-western-pennsylvania", "https://millercenter.org/the-presidency/presidential-speeches/december-8-1795-seventh-annual-message-congress",  "https://millercenter.org/the-presidency/presidential-speeches/march-30-1796-message-house-representatives-declining-submit", 
 "https://millercenter.org/the-presidency/presidential-speeches/august-29-1796-talk-cherokee-nation", "https://millercenter.org/the-presidency/presidential-speeches/september-19-1796-farewell-address", "https://millercenter.org/the-presidency/presidential-speeches/december-7-1796-eighth-annual-message-congress"]

#Corresponding list of dates that each speech was given.  Useful for tracking changes over time
Washington_speech_dates = [[1789, 4, 30], [1789, 10, 3], [1790, 1, 8], [1790, 12, 8], [1790, 12, 29], [1791, 10, 25], [1792, 4, 5], [1792, 11, 6], [1792, 12, 12], [1793, 3, 4], [1793, 4, 22], [1793, 12, 3], [1794, 8, 7], [1794, 9, 25], [1794, 11, 19], 
[1795, 10, 10], [1795, 12, 8], [1796, 3, 30], [1796, 8, 29], [1796, 9, 19], [1796, 12, 7]]

#Create list of web addresses to scrape the text of John Adam's speeches from the Miller Center
Adams_URLs = ['https://millercenter.org/the-presidency/presidential-speeches/march-4-1797-inaugural-address', 'https://millercenter.org/the-presidency/presidential-speeches/may-16-1797-special-session-message-congress-xyz-affair',
              'https://millercenter.org/the-presidency/presidential-speeches/november-22-1797-first-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/march-23-1798-proclamation-day-fasting-humiliation-and-prayer',
              'https://millercenter.org/the-presidency/presidential-speeches/december-8-1798-second-annual-message', 'https://millercenter.org/the-presidency/presidential-speeches/december-3-1799-third-annual-message',
              'https://millercenter.org/the-presidency/presidential-speeches/may-21-1800-proclamation-pardons-those-engaged-fries-rebellion', 'https://millercenter.org/the-presidency/presidential-speeches/november-22-1800-fourth-annual-message'] 
              
Adams_speech_dates = [[1797, 3, 4], [1797, 5, 16], [1797, 11, 22], [1798, 03, 23], [1798, 12, 8], [1799, 12, 3], [1800, 5, 21], [1800, 11, 22]]    

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

#uncomment the statement below to output list of compiled and processed Washington speeches
#washington_speech_list = compile_speeches(Washington_URLS)

