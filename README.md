# Analysis_of_Faculty_Participation_Data

<!-- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psyduck1203/Analysis_of_Faculty_Participation_Data/HEAD?filepath=%2Fvoila%2Frender%2FAnalysis_of_Faculty_Participation_Data_Workshop.ipynb)
-->

# Demo

Launch the web app:

<!-- [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/multi-page-app/main/app.py)
-->

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *afpdenv*
```
conda create -n afpdenv python=3.7.9
```
Secondly, we will login to the *afpdenv* environement
```
conda activate afpdenv
```
### Install prerequisite libraries

Download requirements.txt file

```
https://github.com/psyduck1203/Analysis_of_Faculty_Participation_Data/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

### Download and unzip this repo

Download [this repo](https://github.com/psyduck1203/Analysis_of_Faculty_Participation_Data/archive/main.zip) and unzip as your working directory.

###  Launch the app

```
streamlit run app.py
```
