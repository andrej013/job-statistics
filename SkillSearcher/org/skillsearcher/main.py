'''
Created on Oct 30, 2014

@author: Andrej
'''
import daily_downloader as d
# from jobs_parser import download_jobs
from org.skillsearcher import jobs_parser

downloader = d.DailyDownloader()
locations = downloader.get_locations()
jobs = downloader.get_job_keywords()

for job in jobs:
    for location in  locations:
        jobs_parser.download_jobs(job, location)