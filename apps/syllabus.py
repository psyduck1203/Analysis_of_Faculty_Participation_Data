import streamlit as st
import pandas as pd

import datetime 

def app():
    st.title('Syllabus')

    st.write('This page will show the graphs and tables based on the Faculty Particpation in Syllabus')

    data = st.file_uploader("Upload your relevant excel file")
    df = pd.read_csv(data)

    page_names = ["Department", "Faculty"]
    page = st.radio("", page_names, index=0)

    if page == "Department":
        col1, col2, col3 ,col4 = st.beta_columns(4)
        with col1:
	        temp1 = st.button("Semester wise")
        with col2:
	        temp2 = st.button("Year wise")
        with col3:
            temp3 = st.button("Venue")
        with col4:
            temp7 = st.button("University wise")
		

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
            st.write('**Table based on Sem-Wise Count for whole Department**')
                
            st.table(df1)
            st.write('**Graph based on Sem-Wise Count for whole Department **')
            
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
            st.write('**Table based on Year-Wise Count for whole Department**')
                
            st.table(df2)
            st.write('**Graph based on Year-Wise Count for whole Department **')
            
            st.bar_chart(df2) 
            
    if page == "Department":
        if temp3 == True:
            df2=pd.DataFrame(data=None,columns=['Count'])

            
            totalr=len(df[df['Venue'] == 'RAIT'])
            totalr=totalr

            totall=len(df['Venue'])

            totald=totall-totalr
            t1=pd.DataFrame([totalr],columns=['Count'],index=['RAIT'])
            df2=df2.append(pd.DataFrame(t1))

            t1=pd.DataFrame([totald],columns=['Count'],index=['Other Universities'])
            df2=df2.append(pd.DataFrame(t1))
            st.write('**Table based on Venue-Wise Count for whole Department**')
            st.table(df2)
            st.write('**Graph based on Venue-Wise Count for whole Department **')
            
            st.bar_chart(df2) 
             

    if page == "Department":
        if temp7 == True:
            df2=pd.DataFrame(data=None,columns=['Count'])

            
            totalm=len(df[df['NameofUniversity'] == 'University of Mumbai'])
            totalr=len(df[df['NameofUniversity'] == 'RAIT'])
            totall=len(df['NameofUniversity'])

            totald=totall-totalm-totalr
            
            t1=pd.DataFrame([totalm],columns=['Count'],index=['Mumbai University'])
            df2=df2.append(pd.DataFrame(t1))

            t1=pd.DataFrame([totalr],columns=['Count'],index=['RAIT'])
            df2=df2.append(pd.DataFrame(t1))

            t1=pd.DataFrame([totald],columns=['Count'],index=['Other Universities'])
            df2=df2.append(pd.DataFrame(t1))
            st.write('**Table based on University-Wise Count for whole Department**')
                
            st.table(df2)
            st.write('**Graph based on Univers-Wise Count for whole Department **')
            
            st.bar_chart(df2) 
                    
    
    if page == "Faculty":
        col_one_list = df['NameOfFaculty'].tolist()

        col_one_list=list(set(col_one_list))
        
        df2=pd.DataFrame(data=None,columns=['Count'])
        df1=df
        faculties = df1["NameOfFaculty"].unique()
        faculty = st.selectbox('Select the name of the faculty:',faculties)
        j=col_one_list.index(faculty)
        
        df['Date'] = df['Date'].astype('datetime64[ns]')
        df_1 = df['Date'].dt.year
                
        col = []
        for i in df_1:
            col.append(i)
        col=list(set(col))

        for i in col: 
            mask = (df['Date'] > str(i)+'0615') & (df['Date'] <= str(i+1)+'0615')  & (df['NameOfFaculty']==str(col_one_list[j])) 
          
            test5=df.loc[mask]
            c1=test5['Date']
            t1=c1.shape[0]
            t1=pd.DataFrame([t1],columns=['Count'],index=[str(i)+'-'+str(i+1)])
            df2=df2.append(pd.DataFrame(t1))
        st.write('**Table based on Year-Wise Count for Faculty**')
                
        st.table(df2)
        st.write('**Graph based on Year-Wise Count for Faculty **')
            
        st.bar_chart(df2) 
            
        
      
        
        
        
        
        df4=pd.DataFrame(data=None,columns=['Count'])
        
        for i in col:
            mask = (df['Date'] > str(i)+'0615') & (df['Date'] <= str(i)+'1215') & (df['NameOfFaculty']==str(col_one_list[j])) 
            mask1 = (df['Date'] > str(i)+'1215') & (df['Date'] <= str(i+1)+'0615') & (df['NameOfFaculty']==str(col_one_list[j])) 
            test5=df.loc[mask]
            test6=df.loc[mask1]
            c1=test5['Date']
            c2=test6['Date']
            t1=c1.shape[0]
            t2=c2.shape[0]
            t1=pd.DataFrame([t1],columns=['Count'],index=['ODD sem '+str(i)])
            df4=df4.append(pd.DataFrame(t1))
            t2=pd.DataFrame([t2],columns=['Count'],index=['EVEN sem '+str(i)])
            df4=df4.append(pd.DataFrame(t2))
        st.write('**Table based on Sem-Wise Count for Faculty**')
                
        st.table(df4)
        st.write('**Graph based on Sem-Wise Count for Faculty **')
            
        st.bar_chart(df4) 
        
        
        
        
        
        data1=df.loc[df['NameOfFaculty'] == str(col_one_list[j])]
        df5=pd.DataFrame(data=None,columns=['Count'])

        totalm=len(data1[data1['NameofUniversity'] == 'University of Mumbai'])
        totalr=len(data1[data1['NameofUniversity'] == 'DYPU'])
        totall=len(data1['NameofUniversity'])
        totald=totall-totalm-totalr
        
        t1=pd.DataFrame([totalm],columns=['Count'],index=['Mumbai University'])
        df5=df5.append(pd.DataFrame(t1))

        t1=pd.DataFrame([totalr],columns=['Count'],index=['RAIT'])
        df5=df5.append(pd.DataFrame(t1))

        t1=pd.DataFrame([totald],columns=['Count'],index=['Other Universities'])
        df5=df5.append(pd.DataFrame(t1))

        st.write('**Table based on University-Wise Count for Faculty**')
                
        st.table(df5)
        st.write('**Graph based on University-Wise Count for Faculty **')
            
        st.bar_chart(df5) 
        
        
        
        
        
        df6=pd.DataFrame(data=None,columns=['Count'])

        data1=df.loc[df['NameOfFaculty'] == str(col_one_list[j])]

        totalr=len(data1[data1['Venue'] == 'RAIT'])
        totalo=len(data1[data1['Venue'] == 'Online'])
        totalr=totalr+totalo

        totall=len(data1['Venue'])

        totald=totall-totalr

        t1=pd.DataFrame([totalr],columns=['Count'],index=['RAIT'])
        df6=df6.append(pd.DataFrame(t1))

        t1=pd.DataFrame([totald],columns=['Count'],index=['Other Universities'])
        df6=df6.append(pd.DataFrame(t1))

        st.write('**Table based on Venue-Wise Count for Faculty**')
                
        st.table(df6)
        st.write('**Graph based on Venue-Wise Count for Faculty **')
            
        st.bar_chart(df6) 
        