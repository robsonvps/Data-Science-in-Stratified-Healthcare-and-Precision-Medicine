
# coding: utf-8

# We first need to tell Python that we're going to be using Pandas. We do this with the *import* command.

# In[1]:


import pandas as pd


# # Reading data
# 
# Let's read the dataset within the csv file "physics_students.csv" that is located in the "readonly" folder.  

# In[2]:


df = pd.read_csv('./readonly/physics_students.csv')


# # Getting a sense of the data
# Get the first five rows of the dataset, i.e. its head.

# In[7]:


df.head(10)


# And now get the last five rows of the data, i.e. its tail.

# In[8]:


df.tail(10)


# Get the names of the columns.

# In[5]:


df.columns


# Get the number of rows and columns in the data frame.

# In[6]:


df.shape


# # Working with data
# Get the 'degree' column.

# In[9]:


df['degree']


# Get a subset of rows, e.g. all rows with index number between 5 and 10.

# In[10]:


df[5:11]


# Get the degree information of all rows with index number between 5 and 10.

# In[11]:


df[5:11]['degree']


# Filter the data to get all records of students older than 30.

# In[12]:


df[df.age>30]


# # Summarising and Visualising Data

# ## Summarising data
# Get quick statistical information about all the numeric columns with the use of of the *describe* function.

# In[13]:


df.describe()


# Get the mean of the 'age' column.

# In[14]:


df['age'].mean()


# Get the mean of all numeric columns.

# In[15]:


df.mean()


# Get the standard deviation of the 'age' column.

# In[16]:


df['age'].std()


# Get the maximum value of 'age'.

# In[17]:


df['age'].max()


# Get the minimum value of 'age'.

# In[18]:


df['age'].min()


# ## Visualising data

# In order to visualise our data, we'll be using the matplotlib library. Let's import it.

# In[19]:


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# Get a histogram for 'age'.

# In[20]:


student_ages = df['age']
student_ages.hist(bins=5)


# Get a box plot for 'age'.

# In[21]:


student_ages.plot.box()


# **And now give yourself a _high five_! You deserve it!** <br> <br> <br> <br>

# # Keep practising

# ## Quiz 1 - Question 7
# 
# The following code specifies a DataFrame that captures information about patients. Complete the code so as to get the shape of patients.

# In[25]:


import pandas as pd
data = {'patientID': ['pt8794', 'pt1297', 'pt3350', 'pt5986', 'pt8853'],
        'name': ['Carlos', 'Amy', 'Ewen', 'Lydia', 'Enrico'],
        'city': ['Edinburgh', 'Edinburgh', 'Aberdeen', 'Glasgow', 'Inverness'],
        'age': [32, 50, 36, 42, 83]}
patients = pd.DataFrame(data, columns=['patientID', 'name', 'age', 'city'])
# add your code here
patients.shape


# ## Quiz 1 - Question 8
# 
# The following code specifies a DataFrame that captures information about patients. Complete the code so as to get the mean of the age column.

# In[29]:


import pandas as pd
data = {'patientID': ['pt8794', 'pt1297', 'pt3350', 'pt5986', 'pt8853'],
        'name': ['Carlos', 'Amy', 'Ewen', 'Lydia', 'Enrico'],
        'city': ['Edinburgh', 'Edinburgh', 'Aberdeen', 'Glasgow', 'Inverness'],
        'age': [32, 50, 36, 42, 83]}
patients = pd.DataFrame(data, columns=['patientID', 'name', 'age', 'city'])
# add your code here
patients.age.mean()


# ## Make up your own questions
# 
# Keep practising with the DataFrames specified above or create your own DataFrame and analyse it.

# In[37]:


patients.age.max()

