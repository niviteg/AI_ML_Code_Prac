#It will first 5 and last 5 rows
import pandas
import pandas as pd
df=pd.read_csv('data.csv')
print(df)

#Head() will print first 5 data and Tail() will print last 5 rows
import pandas as pd
df=pd.read_csv('data.csv')
print(df.head())
print(df.tail())

#It will print Entire Data table
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())

#Check the number of maximum returned rows
import pandas as pd
print("maximun rows",pd.options.display.max_rows)

#Increase the maximum number of rows to display the entire DataFrame
import pandas as pd
#pd.options.display.max_rows = 9999
df=pd.read_csv('data.csv')
print(df)

#Load the JSON file into a DataFrame
import pandas as pd
df=pd.read_json('data.js')
print(df)

#Load a Python Dictionary into a DataFrame
import pandas as pd
data = {
  "Duration":{"0":60,"1":60,"2":60,"3":45,"4":45, "5":60 }, "Pulse":{"0":110,"1":117,"2":103,"3":109,"4":117,"5":102},
  "Maxpulse": {"0": 130,"1": 145,"2": 135,"3": 175,"4": 148,"5": 127},
  "Calories":{"0":409,"1":479,"2":340,"3":282,"4":406,"5":300}
  }

df=pd.DataFrame(data)
print(df)
print(df.info())




