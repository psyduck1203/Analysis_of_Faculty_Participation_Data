import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title('Workshop')

    st.write('This page will show the graphs and tables based on the Faculty Particpation in Workshops, STTP, FDP, etc')

    data = st.file_uploader("Upload your relevant excel file")
    df = pd.ExcelFile(data)
    name = df.sheet_names
    
    for i in name:
        df1 = pd.read_excel(df, sheet_name=i)
        
        st.title(i)

        st.write('**Table based on Criteria**')
        st.table(df1.groupby('Criteria :=> Workshop / STTP / Training Program / FDP').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))
        
        st.write('**Bar Graph based on Criteria**')
        u1 = df1['Criteria :=> Workshop / STTP / Training Program / FDP'].value_counts()
        st.bar_chart(u1)

        st.write('**Table based on Organizer**')
        st.table(df1.groupby('Organizer').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

        st.write('**Bar Graph based on Organizer**')
        u1 = df1['Organizer'].value_counts()
        st.bar_chart(u1)

        st.write('**Table based on Level**')
        st.table(df1.groupby('Local / State / National / International').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

        st.write('**Bar Graph based on Level**')
        u1 = df1['Local / State / National / International'].value_counts()
        st.bar_chart(u1)

        st.write('**Table based on Source of Funding**')
        st.table(df1.groupby('Source of Funding').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

        st.write('**Bar Graph based on Source of Funding**')
        u1 = df1['Source of Funding'].value_counts()
        st.bar_chart(u1)
    
    # f = []
    # numberOfSheets = len(df.sheet_names)

    # for i in range(0,numberOfSheets):    
    #     data = pd.ExcelFile(df, sheetname = i , header=None) 
    #     f.append(data)

    # f = pd.concat(f)

    # u1 = f['Criteria :=> Workshop / STTP / Training Program / FDP'].value_counts()
    # st.bar_chart(u1)