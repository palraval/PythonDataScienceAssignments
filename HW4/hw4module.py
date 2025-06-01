# importing important libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_actor_page(dataframe, link):
    """
    This function complies the actor name and all of the items in their filmography. 
    Args:
        dataframe (pandas dataframe) and link (string)
    Returns:
        dataframe (updated dataframe containing new rows with actor name and filmography
        as a pandas dataframe)
    """

    
# text for the html code from the provided link
    soup = BeautifulSoup(requests.get(link).text)
    

# creates two empty lists to be used later
    filmography_list = []
    filtered_filmography_list = []


# isolates the location of the table in the html link containing filmography information
    acting_table_values = soup.select_one('h3.zero')
    full_values = acting_table_values.find_next('table')


# adds each item in the actor's filmography table into the list called 'filmography_list'
    for entry in full_values.select('a.tooltip'):
        filmography_list.append(entry.text)


# removes any possible duplicate items from 'filmography_list' and saves it 
# into another list called 'filtered_filmography_list'
    for fil in filmography_list:
        if fil in filtered_filmography_list:
            continue
        else:
            filtered_filmography_list.append(fil)
    
# extracts the actor's name from the provided link
    for act in soup.select('h2.title a'):
        actor = act.text

# creates a dataframe containing the actor's name in one column and the items in their 
# filmography, with each item being its own row
    new_row = pd.DataFrame({'actor': actor,
                            'movie_or_TV_name': filtered_filmography_list})
    
    
# updates the original dataframe by adding the new dataframe to it in a row-wise fashion
    dataframe = pd.concat([dataframe, new_row], axis = 0)

# returns this newly updated dataframe
    return dataframe  


def parse_full_credits(link):
    """
    This function complies all of the actors' names and all of the items in their filmographies. 
    Args:
        link (string)
    Returns:
        dataframe (dataframe containing rows with actors' names and their filmographies
        as a pandas dataframe)
    """


# defines an empty list to be used later
    cast_link_list = []

# creates an empty dataframe that has two columns: 'actor' and 'movie_or_TV_name' 
    df = pd.DataFrame(columns= ['actor', 'movie_or_TV_name'])

# text for the html code from the provided link
    soup = BeautifulSoup(requests.get(link).text)
    
# isolates location of the cast's information
    cast_info = soup.select_one("section.panel.pad")


# adds unique href links to the list called 'cast_link_list' 
    for cast in cast_info.select("li a"):
        if cast.attrs['href'] in cast_link_list:
            continue
        else:
            cast_link_list.append(cast.attrs["href"])
        
        
# combines each href link with the base url to get the full url
# each full url is then given to the parse_actor_page() to get all the actors and their filmographies
# saves the finished dataframe given by parse_actor_page() as 'df'
    for cast_link in cast_link_list:
        new_link = "https://themoviedb.org" + cast_link
        df = parse_actor_page(df, new_link)
    
    
    # df['first_listing'] = df['movie_or_TV_name'].apply(lambda x:x[0])
    # df = df.sort_values(by = ['actor', 'first_listing']).drop(columns = 'first_listing')


# the dataframe 'df' is sorted alphabetically based on actor's name first and then item in their filmography
    df = df.sort_values(by = ['actor', 'movie_or_TV_name'])

# returns the completed dataframe     
    return df