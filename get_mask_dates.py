import pandas as pd 
import numpy as np 

def get_date(dataframe, state, item="mask_date"):
    state = dataframe.loc[dataframe['state'] == state]
    date = np.array(state[item])[0].split('-')[::-1]
    return date[0] + '-' + date[1] + '-' + date[2]

def stateData(dataframe, state):
    # Create a copy
    dataframe2 = dataframe.copy()
    # set the index to be this and don't drop
    dataframe2.set_index(keys=['state'], drop=False,inplace=True)
    return dataframe2.loc[dataframe2.state==state]

def mask_date_to_all_states(state, all_states_file, stay_at_home_file, 
                            item="mask_date"):
    # all inputs are strings
    # files must be paths
    stay_at_home_df = pd.read_csv(stay_at_home_file)
    st = stateData(pd.read_csv(all_states_file), state)
    return st.loc[st['date'] == get_date(stay_at_home_df, state, item=item)]


