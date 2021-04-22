import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Orientation')

    st.write("This page will show the graphs and tables based on the Faculty Particpation in Orientation")

    files = st.file_uploader("Upload your relevant excel file", accept_multiple_files = True)
    
    for data in files:
        bytes_data = data.read()
        st.write("filename:", data.name)
        st.write(bytes_data)
    
    
    df = pd.read_csv(data)


# stock_files=sorted(glob('CSV/Universit_Orientation_*.csv'))
# stock_files

# data=pd.concat((pd.read_csv(file) for file in stock_files),ignore_index=True)
# data



# for fn in data.keys():
#   print('User uploaded file "{name}" with length {length} bytes'.format(
#       name=fn, length=len(data[fn])))



# import pandas as pd

# data['Date'] = data['Date'].astype('datetime64[ns]')
# print("Original Dataframe:")
# data['Year'] = data['Date'].apply(lambda x: "%d" % (x.year))
# plt=data['Year'].value_counts()
# plt

# df_1 = data['Date'].dt.year

# # df_1
# col = []
# for i in df_1:
#     col.append(i)
# col=list(set(col))
# col

# #from jan15 to may 15 and june15 to dec 15 ka count plot karna hae for each year
# import datetime 
# df1=pd.DataFrame(data=None,columns=['Count'])


# for i in col:
#   mask = (data['Date'] > str(i)+'0615') & (data['Date'] <= str(i)+'1215')
#   mask1 = (data['Date'] > str(i)+'1215') & (data['Date'] <= str(i+1)+'0615')
#   test5=data.loc[mask]
#   test6=data.loc[mask1]
#   c1=test5['Date']
#   c2=test6['Date']
#   t1=c1.shape[0]
#   t2=c2.shape[0]
#   t1=pd.DataFrame([t1],columns=['Count'],index=['ODD sem '+str(i)])
#   df1=df1.append(pd.DataFrame(t1))
#   t2=pd.DataFrame([t2],columns=['Count'],index=['EVEN sem '+str(i)])
#   df1=df1.append(pd.DataFrame(t2))

# df1.plot(color="#6c3376", linewidth=3,kind="bar",ylim=(0,25),title='Semester wise teachers attending Orientation',xlabel='Semester', ylabel='Count')

# df1.to_excel('UniversityOrientation(Semester_wise).xlsx')



# #from jan15 to may 15 and june15 to dec 15 ka count plot karna hae for each year
# import datetime 
# df2=pd.DataFrame(data=None,columns=['Count'])

# for i in col:
#   mask = (data['Date'] > str(i)+'0615') & (data['Date'] <= str(i+1)+'0615')
#   test5=data.loc[mask]
#   c1=test5['Date']
#   t1=c1.shape[0]
#   t1=pd.DataFrame([t1],columns=['Count'],index=[str(i)+'-'+str(i+1)])
#   df2=df2.append(pd.DataFrame(t1))

# df2.plot(color="#6c3376", linewidth=3,kind="bar",ylim=(0,25),title='Day')


# df2.to_excel('UniversityOrientation(Year wise).xlsx')



# #saving and downloadind th graph

# import matplotlib.pyplot as plt
# from google.colab import files

# ax=df1.plot(color="#6c3376", linewidth=3,kind="bar",title='Count of teachers attending orientation per Semester',ylim=(0,25))
# ax.set(xlabel='Year', ylabel='Count')
# plt.savefig('FinalUniversity (Year wise).png',bbox_inches='tight')

# files.download('FinalUniversity (Year wise).png')

# #saving and downloadind th graph

# import matplotlib.pyplot as plt
# from google.colab import files

# ax=df2.plot(color="#6c3376", linewidth=3,kind="bar",title='Count of teachers attending orientation per year',ylim=(0,25))
# ax.set(xlabel='Year', ylabel='Count')
# plt.savefig('FinalUniversity (Semester_wise).png',bbox_inches='tight')


# files.download('FinalUniversity (Semester_wise).png')

