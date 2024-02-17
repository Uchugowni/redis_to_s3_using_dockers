from util.constants import CLIENT_ID, SECRET

def reddit_pipeline(filename:str,subreddit:str,time_filter:str,limit:str):
    #Conneting to reddit instance
    instance=connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #Extraction

    #trasformation
    
    #loading to csv
