import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def app():
    st.title('Orientation')

    st.write('**This page will show the graphs and tables based on the Faculty Particpation in Orientation**')

    data = st.file_uploader("Upload your relevant excel file")
    df = pd.read_csv(data)

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
            df['Date'] = df['Date'].astype('datetime64[ns]')
            df_1 = df['Date'].dt.year
            col = []
            for i in df_1:
                col.append(i)
            col=list(set(col))

            df1=pd.DataFrame(data=None,columns=['Count'])
            for i in col:
                mask = (df['Date'] > str(i)+'0615') & (df['Date'] <= str(i)+'1215')
                mask1 = (df['Date'] > str(i)+'1215') & (df['Date'] <= str(i+1)+'0615')
                test5=df.loc[mask]
                test6=df.loc[mask1]
                c1=test5['Date']
                c2=test6['Date']
                t1=c1.shape[0]
                t2=c2.shape[0]
                t1=pd.DataFrame([t1],columns=['Count'],index=['ODD sem '+str(i)])
                df1=df1.append(pd.DataFrame(t1))
                t2=pd.DataFrame([t2],columns=['Count'],index=['EVEN sem '+str(i)])
                df1=df1.append(pd.DataFrame(t2))
            st.write('**Graph of Semester-Wise Count of Teacher attending Orientation**')
            
            st.bar_chart(df1) 

    if page == "Department":
        if temp2 == True:
            df['Date'] = df['Date'].astype('datetime64[ns]')
            df_1 = df['Date'].dt.year
            col = []
            for i in df_1:
                col.append(i)
            col=list(set(col))
            df2=pd.DataFrame(data=None,columns=['Count'])
            for i in col:
                mask = (df['Date'] > str(i)+'0615') & (df['Date'] <= str(i+1)+'0615')
                test5=df.loc[mask]
                c1=test5['Date']
                t1=c1.shape[0]
                t1=pd.DataFrame([t1],columns=['Count'],index=[str(i)+'-'+str(i+1)])
                df2=df2.append(pd.DataFrame(t1))
            st.write('**Graph of Year-Wise Count of Teacher attending Orientation**')
            
            st.bar_chart(df2)