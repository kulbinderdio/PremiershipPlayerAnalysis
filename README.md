# PremiershipPlayerAnalysis
Using Python to scrape some basic player information from www.premierleague.com and then use Pandas to analyse said data.
Note : My understanding is the squad data on this site can change at any time so your results might be different

The was developed in Jupyter Notebook and this walkthrough willl assume you are doing the same

Once you have ran the scraping 


    original = pd.DataFrame(playersList) # Convert the data scraped into a Pandas DataFrame 

    original.to_csv('premiershipplayers.csv') # Keep a back up of the data to save time later if required 

    df2 = original.copy() # Working copy of the DataFrame (just in case) 


    df2.info()
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 578 entries, 0 to 577
    Data columns (total 11 columns):
     #   Column       Non-Null Count  Dtype 
    ---  ------       --------------  ----- 
     0   club         578 non-null    object
     1   name         578 non-null    object
     2   shirtNo      572 non-null    object
     3   nationality  562 non-null    object
     4   dob          562 non-null    object
     5   height       500 non-null    object
     6   weight       474 non-null    object
     7   appearances  578 non-null    object
     8   goals        578 non-null    object
     9   wins         578 non-null    object
     10  losses       578 non-null    object
    dtypes: object(11)
    memory usage: 49.8+ KB

***A total of 578 player.***

6 without shirt number

16 without nationality listed

16 without dob listed

78 without height listed

104 without weight listed




***Cleanup Data***
1. Remove spaces and newline from dob, appearances, goals, wins and losses columns
2. Change type of dob to date
3. change type of appearances, goals, wins, losses to int

        df2['dob'] = df2['dob'].str.replace('\n','').str.strip(' ')
        df2['appearances'] = df2['appearances'].str.replace('\n','').str.strip(' ')
        df2['goals'] = df2['goals'].str.replace('\n','').str.strip(' ')
        df2['wins'] = df2['wins'].str.replace('\n','').str.strip(' ')
        df2['losses'] = df2['losses'].str.replace('\n','').str.strip(' ')

        # change type of dob, appearances, goals, wins, losses
        from datetime import  date

        df2['dob'] = pd.to_datetime(df2['dob'],format='%d/%m/%Y').dt.date
        df2["appearances"] = pd.to_numeric(df2["appearances"])
        df2["goals"] = pd.to_numeric(df2["goals"])
        df2["wins"] = pd.to_numeric(df2["wins"])
        df2["losses"] = pd.to_numeric(df2["losses"])
        df2['height'] = df2['height'].str[:-2]
        df2["height"] = pd.to_numeric(df2["height"])
        
        
        # Create age column

        today = date.today()

        def age(born):
            if born:
                return today.year - born.year - ((today.month, 
                                              today.day) < (born.month, 
                                                            born.day))
            else:
                return np.nan

        df2['age'] = df2['dob'].apply(age)
 
 
 
 *** 10 Oldest Players ***
        df2.sort_values('age',ascending=False).head(10)
        
        

