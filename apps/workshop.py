import streamlit as st
import pandas as pd

def app():
    st.title('Workshop')

    st.write('This page will show the graphs and tables based on the Faculty Particpation in Workshops, STTP, FDP, etc')

    data = st.file_uploader("Upload your relevant excel file")
    df = pd.ExcelFile(data)
    name = df.sheet_names

    page = st.select_slider( '', options=["Department", "Faculty"])

    if page == "Department":
        time = ["Semester wise", "Year wise", "Cumulative years"]
        temp = st.selectbox('Select the time period:', time)
        if temp == "Semester wise":
            for i in range(6):
                df1 = pd.read_excel(df, sheet_name=name[i])
                
                st.title(name[i])

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
    
        elif temp == "Year wise":
            for i in range(6,9):
                df1 = pd.read_excel(df, sheet_name=name[i])
                
                st.title(name[i])

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

        else:
                df1 = pd.read_excel(df, sheet_name=name[9])
                
                st.title("Cumulative Years Combined")

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
        z = st.selectbox('Select the time period:', name)
        df1 = pd.read_excel(df, sheet_name=z)
        col_one_list = df1['NAME OF FACULTY']

        faculties = df1["NAME OF FACULTY"].unique()
        faculty = st.selectbox('Select the name of the faculty:',faculties)

        data = []
        for k in range(len(col_one_list)):
            if(faculty==col_one_list[k]):
                if(df1["Criteria :=> Workshop / STTP / Training Program / FDP"][k]=="Workshop"):
                    data.append("Workshop")
                elif(df1["Criteria :=> Workshop / STTP / Training Program / FDP"][k]=="STTP"):
                    data.append("STTP")
                elif(df1["Criteria :=> Workshop / STTP / Training Program / FDP"][k]=="FDP"):
                    data.append("FDP")
                else:
                    data.append("Others")
        
        temp1 = pd.DataFrame(data,columns=["Criteria :=> Workshop / STTP / Training Program / FDP"])
        
        st.write('**Table based on Criteria** for ' + faculty)
        st.table(temp1["Criteria :=> Workshop / STTP / Training Program / FDP"].value_counts())
        
        st.write('**Bar Graph based on Criteria** for '+ faculty)
        st.bar_chart(temp1["Criteria :=> Workshop / STTP / Training Program / FDP"].value_counts())

        data = []
        for k in range(len(col_one_list)):
            if(faculty==col_one_list[k]):
                if(df1["Organizer"][k]=="RAIT"):
                    data.append("RAIT")
                elif(df1["Organizer"][k]=="IIT"):
                    data.append("IIT")
                else:
                    data.append("Others")
        
        temp2 = pd.DataFrame(data,columns=["Organizer"])
        
        st.write('**Table based on Organizer** for '+ faculty)
        st.table(temp2["Organizer"].value_counts())
        
        st.write('**Bar Graph based on Organizer** for '+ faculty)
        st.bar_chart(temp2["Organizer"].value_counts())

        data = []
        for k in range(len(col_one_list)):
            if(faculty==col_one_list[k]):
                if(df1["Local / State / National / International"][k]=="Local"):
                    data.append("Local")
                elif(df1["Local / State / National / International"][k]=="State"):
                    data.append("State")
                elif(df1["Local / State / National / International"][k]=="National"):
                    data.append("National")
                elif(df1["Local / State / National / International"][k]=="International"):
                    data.append("International")
                else:
                    data.append("Others")
        
        temp3 = pd.DataFrame(data,columns=["Local / State / National / International"])
        
        st.write('**Table based on Level** for '+ faculty)
        st.table(temp3["Local / State / National / International"].value_counts())
        
        st.write('**Bar Graph based on Level** for '+ faculty)
        st.bar_chart(temp3["Local / State / National / International"].value_counts())

        data = []
        for k in range(len(col_one_list)):
            if(faculty==col_one_list[k]):
                if(df1["Source of Funding"][k]=="RAIT"):
                    data.append("RAIT")
                elif(df1["Source of Funding"][k]=="Self"):
                    data.append("Self")
                else:
                    data.append("NIL")
        
        temp4 = pd.DataFrame(data,columns=["Source of Funding"])
        
        st.write('**Table based on Source of Funding** for '+ faculty)
        st.table(temp4["Source of Funding"].value_counts())
        
        st.write('**Bar Graph based on Source of Funding** for '+ faculty)
        st.bar_chart(temp4["Source of Funding"].value_counts())