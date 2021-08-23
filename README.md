# PremiershipPlayerAnalysis
Using Python to scrape some basic player information from www.premierleague.com and then use Pandas to analyse said data.
Note : My understanding is the squad data on this site can change at any time so your results might be different

***Improvement : Calculate age to finer degree than just years***

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

*** A total of 578 player. ***

6 without shirt number

16 without nationality listed

16 without dob listed

78 without height listed

104 without weight listed




## Cleanup Data ##
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
 
 
 
### 10 Oldest Players ###

        df2.sort_values('age',ascending=False).head(10)
        
![image](https://user-images.githubusercontent.com/4700433/130436618-358f99d4-fbe7-493b-8b74-4cb6e696f4d0.png)


### 10 Youngest Players ###

        df2.sort_values('age',ascending=True).head(10)
        
![image](https://user-images.githubusercontent.com/4700433/130437043-3be3caf6-ee97-4f6a-bcfc-40ab364cf57c.png)


### Squad Sizes ###

        df2.groupby(['club'])['club'].count().sort_values(ascending=False)
        
![image](https://user-images.githubusercontent.com/4700433/130437398-693b09f5-ea69-4b1e-a3c4-80ff3b8692e8.png)


### Team's Average Player Age ###

        plt.ylim([20, 30])
        df2.groupby(['club'])['age'].mean().sort_values(ascending=False).plot.bar()
        
![image](https://user-images.githubusercontent.com/4700433/130438078-0d0cbd54-15d8-433d-b4c5-057bacf831b0.png)


### Burnley appear to not only have one of the highest average player ages but also the owest number of registered players ###


### Top 10 Premiership Appearances ###
        df2.sort_values('appearances',ascending=False).head(10)
        
![image](https://user-images.githubusercontent.com/4700433/130438782-3e282917-f50e-4b23-b484-e56b6f8db58d.png)


### Collective Premiership Appearances per Club ###
        df2.groupby(['club'])['appearances'].sum().sort_values(ascending=False)
        
![image](https://user-images.githubusercontent.com/4700433/130439559-31c3f20e-8a7d-4609-9ae3-03da86f3efb3.png)

        df2.groupby(['club'])['appearances'].sum().sort_values(ascending=False).plot.bar()
        
![image](https://user-images.githubusercontent.com/4700433/130439689-e9507bf7-4c8d-4c2e-b79f-210c41b9b1ca.png)


### 10 Tallest Playes ###
        df2.sort_values('height',ascending=False).head(10)
![image](https://user-images.githubusercontent.com/4700433/130440008-647df661-9475-4b8a-8237-671dceff6624.png)

        
        
        
### 10 Shortest Playes ###
        df2.sort_values('height',ascending=True).head(10)
![image](https://user-images.githubusercontent.com/4700433/130440077-7c5fde84-2eca-4a52-8a47-78d397bdef1e.png)


### Nationality totals of Players ###
        pd.set_option('display.max_rows', 100)
        df.groupby(['nationality'])['club'].count().sort_values(ascending=False)
        
        
        
        
 ### Nationality totals per club ###       
        pd.set_option('display.max_rows', 500)
        df.groupby(['club','nationality'])['nationality'].count()
        
        
