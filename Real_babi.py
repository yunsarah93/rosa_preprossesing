
# coding: utf-8

# In[205]:


import pandas as pd
import re
import numpy as np
s_num = 1
txt = open("C:/Users/Sora Yun/Desktop/babi_response/a_s" + str(s_num) + "_r1.txt",'r')

lines = txt.readlines()
line = [x.strip() for x in lines]
line_str = ','.join(line)

pattern1 = r'([0-9]{1,2}[A-Z]{4,9})'
regex = re.compile(pattern1, flags=re.IGNORECASE)
exp_type = regex.findall(line_str)

cuts = exp_type = regex.split(line_str)
cuts = [x.strip(',') for x in cuts]

lst = []
ans = []
for each in cuts:
    if 'Text' in each or 'Image' in each:
        lst.append(each) 
    else:
        ans.append(each)

ans= ans[1:] # 공백 제거

df = pd.DataFrame({'lst':lst,'ans':ans}, columns = ['lst','ans'])

temp = []
temp2 = []
for idx,row in df.iterrows():
    if len(df['ans'][idx].split(',')) == 2:
        temp.append(row[0])
        temp2.append(row[1].split(','))

df2 = pd.DataFrame(temp2, columns = ['1st','2nd'])
df2['lst'] = temp
df2 = df2[['lst','1st','2nd']]
df3 = pd.merge(df,df2, how='outer')

df3['temp'] = None
for i in range(len(df3)):
    if pd.isnull(df3['1st'].loc[i]) == True:
        df3['temp'].loc[i] = df3['ans'].loc[i]
    else:
        df3['temp'].loc[i] = df3['1st'].loc[i]

df4 = pd.DataFrame(df3[['lst','temp','2nd']])
df4.columns = ['lst','1st','2nd']

# # ox와 반응 시간 \t 를 기준으로 split 하기
# df4의 ['lst','2nd']를 각각 split한 후 리스트에 담아 df4에 새로운 컬럼['ox','response_time']으로 추가하기

splited_list = []
for combined_list in df4['1st']:
    splited_list.append(combined_list.split('\t'))

df4[['ox1','response_time1']] = pd.DataFrame(splited_list)

splited_list2 = []
for combined_list2 in df4['2nd']:
    try : 
        splited_list2.append(combined_list2.split('\t'))
    except :
        splited_list2.append(['',''])
df4[['ox2','response_time2']] = pd.DataFrame(splited_list2)

# 타입 _T,_I,_M으로 바꾸기
for i in range(len(df4)):
    if 'ImageText' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('ImageText','_M')
    elif 'Image' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Image','_I')
    elif 'Text' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Text','_T')

# 소수점 2번째 자리까지
cnt = 0
for str_num1 in df4['response_time1']:
    df4['response_time1'][cnt] = round(float(str_num1),2)
    cnt += 1

cnt = 0
for str_num2 in df4['response_time2']:
    if df4['response_time2'][cnt] != '':
        df4['response_time2'][cnt] = round(float(str_num2),2)
    else:
        pass
    cnt += 1

df4_1 = df4[['lst','ox1','response_time1']]
df4_2 = df4[['lst','ox2','response_time2']]
df_join = df4_1.set_index('lst').join(df4_2.set_index('lst'))

ddd = df4[['lst','ox1','response_time1','ox2','response_time2']]
d = pd.DataFrame(df_join.values.reshape(40,2),columns=['ox','response_time'])
d['lst'] = (np.repeat(list(ddd['lst']),2))
d1 = d[['lst','ox','response_time']]

writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\result1.xlsx')
d1.to_excel(writer)
writer.save()


# In[206]:


txt = txt = open("C:/Users/Sora Yun/Desktop/babi_response/a_s" + str(s_num) + "_r2.txt",'r')

lines = txt.readlines()
line = [x.strip() for x in lines]
line_str = ','.join(line)

pattern1 = r'([0-9]{1,2}[A-Z]{4,9})'
regex = re.compile(pattern1, flags=re.IGNORECASE)
exp_type = regex.findall(line_str)

cuts = exp_type = regex.split(line_str)
cuts = [x.strip(',') for x in cuts]

lst = []
ans = []
for each in cuts:
    if 'Text' in each or 'Image' in each:
        lst.append(each) 
    else:
        ans.append(each)

ans= ans[1:] # 공백 제거

df = pd.DataFrame({'lst':lst,'ans':ans}, columns = ['lst','ans'])

temp = []
temp2 = []
for idx,row in df.iterrows():
    if len(df['ans'][idx].split(',')) == 2:
        temp.append(row[0])
        temp2.append(row[1].split(','))

df2 = pd.DataFrame(temp2, columns = ['1st','2nd'])
df2['lst'] = temp
df2 = df2[['lst','1st','2nd']]
df3 = pd.merge(df,df2, how='outer')

df3['temp'] = None
for i in range(len(df3)):
    if pd.isnull(df3['1st'].loc[i]) == True:
        df3['temp'].loc[i] = df3['ans'].loc[i]
    else:
        df3['temp'].loc[i] = df3['1st'].loc[i]

df4 = pd.DataFrame(df3[['lst','temp','2nd']])
df4.columns = ['lst','1st','2nd']

# # ox와 반응 시간 \t 를 기준으로 split 하기
# df4의 ['lst','2nd']를 각각 split한 후 리스트에 담아 df4에 새로운 컬럼['ox','response_time']으로 추가하기

splited_list = []
for combined_list in df4['1st']:
    splited_list.append(combined_list.split('\t'))

df4[['ox1','response_time1']] = pd.DataFrame(splited_list)

splited_list2 = []
for combined_list2 in df4['2nd']:
    try : 
        splited_list2.append(combined_list2.split('\t'))
    except :
        splited_list2.append(['',''])
df4[['ox2','response_time2']] = pd.DataFrame(splited_list2)

# 타입 _T,_I,_M으로 바꾸기
for i in range(len(df4)):
    if 'ImageText' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('ImageText','_M')
    elif 'Image' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Image','_I')
    elif 'Text' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Text','_T')

# 소수점 2번째 자리까지
cnt = 0
for str_num1 in df4['response_time1']:
    df4['response_time1'][cnt] = round(float(str_num1),2)
    cnt += 1

cnt = 0
for str_num2 in df4['response_time2']:
    if df4['response_time2'][cnt] != '':
        df4['response_time2'][cnt] = round(float(str_num2),2)
    else:
        pass
    cnt += 1

df4_1 = df4[['lst','ox1','response_time1']]
df4_2 = df4[['lst','ox2','response_time2']]
df_join = df4_1.set_index('lst').join(df4_2.set_index('lst'))

ddd = df4[['lst','ox1','response_time1','ox2','response_time2']]
d = pd.DataFrame(df_join.values.reshape(40,2),columns=['ox','response_time'])
d['lst'] = (np.repeat(list(ddd['lst']),2))
d2 = d[['lst','ox','response_time']]

writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\result2.xlsx')
d2.to_excel(writer)
writer.save()


# In[207]:


txt = open("C:/Users/Sora Yun/Desktop/babi_response/a_s" + str(s_num) + "_r3.txt",'r')

lines = txt.readlines()
line = [x.strip() for x in lines]
line_str = ','.join(line)

pattern1 = r'([0-9]{1,2}[A-Z]{4,9})'
regex = re.compile(pattern1, flags=re.IGNORECASE)
exp_type = regex.findall(line_str)

cuts = exp_type = regex.split(line_str)
cuts = [x.strip(',') for x in cuts]

lst = []
ans = []
for each in cuts:
    if 'Text' in each or 'Image' in each:
        lst.append(each) 
    else:
        ans.append(each)

ans= ans[1:] # 공백 제거

df = pd.DataFrame({'lst':lst,'ans':ans}, columns = ['lst','ans'])

temp = []
temp2 = []
for idx,row in df.iterrows():
    if len(df['ans'][idx].split(',')) == 2:
        temp.append(row[0])
        temp2.append(row[1].split(','))

df2 = pd.DataFrame(temp2, columns = ['1st','2nd'])
df2['lst'] = temp
df2 = df2[['lst','1st','2nd']]
df3 = pd.merge(df,df2, how='outer')

df3['temp'] = None
for i in range(len(df3)):
    if pd.isnull(df3['1st'].loc[i]) == True:
        df3['temp'].loc[i] = df3['ans'].loc[i]
    else:
        df3['temp'].loc[i] = df3['1st'].loc[i]

df4 = pd.DataFrame(df3[['lst','temp','2nd']])
df4.columns = ['lst','1st','2nd']

# # ox와 반응 시간 \t 를 기준으로 split 하기
# df4의 ['lst','2nd']를 각각 split한 후 리스트에 담아 df4에 새로운 컬럼['ox','response_time']으로 추가하기

splited_list = []
for combined_list in df4['1st']:
    splited_list.append(combined_list.split('\t'))

df4[['ox1','response_time1']] = pd.DataFrame(splited_list)

splited_list2 = []
for combined_list2 in df4['2nd']:
    try : 
        splited_list2.append(combined_list2.split('\t'))
    except :
        splited_list2.append(['',''])
df4[['ox2','response_time2']] = pd.DataFrame(splited_list2)

# 타입 _T,_I,_M으로 바꾸기
for i in range(len(df4)):
    if 'ImageText' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('ImageText','_M')
    elif 'Image' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Image','_I')
    elif 'Text' in df4['lst'][i]:
        df4['lst'][i] = df4['lst'][i].replace('Text','_T')

# 소수점 2번째 자리까지
cnt = 0
for str_num1 in df4['response_time1']:
    df4['response_time1'][cnt] = round(float(str_num1),2)
    cnt += 1

cnt = 0
for str_num2 in df4['response_time2']:
    if df4['response_time2'][cnt] != '':
        df4['response_time2'][cnt] = round(float(str_num2),2)
    else:
        pass
    cnt += 1

df4_1 = df4[['lst','ox1','response_time1']]
df4_2 = df4[['lst','ox2','response_time2']]
df_join = df4_1.set_index('lst').join(df4_2.set_index('lst'))

ddd = df4[['lst','ox1','response_time1','ox2','response_time2']]
d = pd.DataFrame(df_join.values.reshape(40,2),columns=['ox','response_time'])
d['lst'] = (np.repeat(list(ddd['lst']),2))
d3 = d[['lst','ox','response_time']]

writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\result3.xlsx')
d3.to_excel(writer)
writer.save()


# In[208]:


tot = pd.concat([d1,d2,d3])


# In[209]:


Ts = []
Is = []
Ms = []
for i in range(len(tot['lst'])):
    if 'T' in tot['lst'].iloc[i]:
        tot['lst'].iloc[i] = int(tot['lst'].iloc[i].strip('_T'))
        Ts.append(list(tot.iloc[i]))
    elif 'I' in tot['lst'].iloc[i]:
        tot['lst'].iloc[i] = int(tot['lst'].iloc[i].strip('_I'))        
        Is.append(list(tot.iloc[i]))
    elif 'M' in tot['lst'].iloc[i]:
        tot['lst'].iloc[i] = int(tot['lst'].iloc[i].strip('_M'))
        Ms.append(list(tot.iloc[i]))


# In[210]:


d_ts = pd.DataFrame(Ts, columns = ['lst','ox','response_time']).reset_index()
d_is = pd.DataFrame(Is, columns = ['lst','ox','response_time']).reset_index()
d_ms = pd.DataFrame(Ms, columns = ['lst','ox','response_time']).reset_index()

d_ts = d_ts.sort_values(['lst','index'])
d_is = d_is.sort_values(['lst','index'])
d_ms = d_ms.sort_values(['lst','index'])


# In[211]:


writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\d_ts.xlsx')
d_ts.to_excel(writer)
writer.save()

writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\d_is.xlsx')
d_is.to_excel(writer)
writer.save()

writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\d_ms.xlsx')
d_ms.to_excel(writer)
writer.save()


# In[274]:


from collections import OrderedDict

order = list(pd.concat([d1,d2,d3])['lst'])
order = list(OrderedDict.fromkeys(order)) # 두 번씩 중복되는 lst 값 제거
d_order = pd.DataFrame(order)


# In[275]:


nums = []
types = []

for num_type in d_order[0]:
    num_temp, type_temp = num_type.split('_')
    nums.append(num_temp)
    types.append(type_temp)
    
d_order['nums'] = nums
d_order['types'] = types


# In[276]:


for k in range(len(d_order['nums'])):
    d_order['nums'].iloc[k] = int(d_order['nums'].iloc[k])


# In[285]:


d_order = d_order.reset_index().sort_values(['nums','index'])


# In[351]:


start = 0
end = 3
l_order = []
for i in range(int(len(list(d_order['types']))/3)):
    l_order.append((list(d_order['types'])[start:end]))
    start += 3
    end += 3
               
        


# In[385]:


last_order = pd.DataFrame(l_order)

empty = []
for s in l_order:
    empty.append('_'.join(s))
    empty.append('')

dorder = pd.DataFrame(empty)


# In[387]:


writer = pd.ExcelWriter('C:\\Users\\Sora Yun\\Desktop\\babi_response\\done\\order.xlsx')
dorder.to_excel(writer)
writer.save()

