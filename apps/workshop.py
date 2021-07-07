import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title('Workshop')

    st.write('This page will show the graphs and tables based on the Faculty Particpation in Workshops, STTP, FDP, etc')

    data = st.file_uploader("Upload your relevant excel file")
    df = pd.ExcelFile(data)
    name = df.sheet_names

    page_names = ["Department", "Faculty"]
    page = st.radio("", page_names, index=0)

    if page == "Department":
        col1, col2, col3 = st.beta_columns(3)
        with col1:
	        temp1 = st.button("Semester wise")
        with col2:
	        temp2 = st.button("Year wise")
        with col3:
            temp3 = st.button("Cumulative years")
			
    elif page == "Faculty":
        col1, col2, col3 = st.beta_columns(3)
        with col1:
	        temp4 = st.button("Semester wise")
        with col2:
	        temp5 = st.button("Year wise")
        with col3:
            temp6 = st.button("Cumulative years")

    if page == "Department":
        if temp1 == True:
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
    
    if page == "Faculty":
        if temp4 == True:
            df1 = pd.read_excel(df, sheet_name=0)
            faculties = df1["NAME OF FACULTY"].unique()
            faculty = st.selectbox('Select the name of the faculty:', faculties)

            st.write(df1["NAME OF FACULTY"][faculty])

            # st.write('**Table based on Criteria** for ' + faculty)
            # st.table(df1.groupby('Criteria :=> Workshop / STTP / Training Program / FDP', faculty).size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))
                

            # st.write('**Bar Graph based on Criteria** for '+ faculty)
            # u1 = df1['Criteria :=> Workshop / STTP / Training Program / FDP'][faculty].value_counts()
            # st.bar_chart(u1)

            # st.write('**Table based on Organizer** for'+ faculty)
            # st.table(df1[faculty].groupby('Organizer').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

            # st.write('**Bar Graph based on Organizer** for'+ faculty)
            # u1 = df1[faculty]['Organizer'].value_counts()
            # st.bar_chart(u1)

            # st.write('**Table based on Level** for'+ faculty)
            # st.table(df1[faculty].groupby('Local / State / National / International').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

            # st.write('**Bar Graph based on Level** for'+ faculty)
            # u1 = df1[faculty]['Local / State / National / International'].value_counts()
            # st.bar_chart(u1)

            # st.write('**Table based on Source of Funding** for'+ faculty)
            # st.table(df1[faculty].groupby('Source of Funding').size().sort_values(ascending=True).reset_index(name='No. of Faculties participated in Workshop'))

            # st.write('**Bar Graph based on Source of Funding** for'+ faculty)
            # u1 = df1[faculty]['Source of Funding'].value_counts()
            # st.bar_chart(u1)