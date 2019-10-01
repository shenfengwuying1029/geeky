import requests
# import pyodbc
import pymssql
from pandas import  DataFrame
templist1 = []
templist2 = []
templist3 = []
templist4 = []
templist5 = []
templist6 = []
templist7 = []
dic={}
params={
    'type': 'HSGTZJZS',
    'token': '70f12f2f4f091e459a279469fe49eca5' ,
    'ps': 5000,
    'js': 'var%20twQXGhyR=({data:[(x)]'
}
url= 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get'
response = requests.get(url, params=params).text
response = response[25:len(response)-3].split('},{')
for i in range(0,len(response)):
    response[i] = response[i].split(',')
for x in range(0,len(response)):
    for y in range(0,len(response[x])):
        if response[x][y].find('"DateTime"') != -1 :
            templist1.append(response[x][y][12:22])
        elif response[x][y].find('"HSMoney"') != -1:
            templist2.append(round(float(response[x][y][10:len(response[x][y])]), 2) if response[x][y][10:len(response[x][y])] != '"-"' else response[x][y][11:len(response[x][y])-1])
        elif response[x][y].find('"SSMoney"') != -1:
            templist3.append(round(float(response[x][y][10:len(response[x][y])]), 2) if response[x][y][10:len(response[x][y])] != '"-"' else response[x][y][11:len(response[x][y])-1])
        elif response[x][y].find('"NorthMoney"') != -1:
            templist4.append(round(float(response[x][y][13:len(response[x][y])]), 2) if response[x][y][13:len(response[x][y])] != '"-"' else response[x][y][14:len(response[x][y])-1])
        elif response[x][y].find('"GGHSMoney"') != -1:
            templist5.append(round(float(response[x][y][12:len(response[x][y])]), 2) if response[x][y][12:len(response[x][y])] != '"-"' else response[x][y][13:len(response[x][y]) - 1])
        elif response[x][y].find('"GGSSMoney"') != -1:
            # print(response[x][y][13:len(response[x][y]) - 1])
            templist6.append(round(float(response[x][y][12:len(response[x][y])]), 2) if response[x][y][12:len(response[x][y])] != '"-"' else response[x][y][13:len(response[x][y]) - 1])
        elif response[x][y].find('"SouthSumMoney"') != -1:
            templist7.append(round(float(response[x][y][16:len(response[x][y])]), 2) if response[x][y][16:len(response[x][y])] != '"-"' else response[x][y][17:len(response[x][y]) - 1])
dic['DateTime'] = templist1
dic['沪股通'] = templist2
dic['深股通'] = templist3
dic['北向资金'] = templist4
dic['港股通(沪)'] = templist5
dic['港股通(深)'] = templist6
dic['南向资金'] = templist7
ds = DataFrame(dic)
cols = ['DateTime', '沪股通', '深股通','北向资金','港股通(沪)','港股通(深)','南向资金']
ds = ds.ix[:, cols]
# conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=PC-201704111647;DATABASE=TempStockData;UID=r4;PWD=shenfeng10; host 1433')
# cursor = conn.cursor()
# myserver = ''
# myuser = 'r4'
# mypassword = 'Aa.1111111111'
# mydbname = 'StockTickData'
# conn= pymssql.connect(host='196.168.1.4', user=myuser, password=mypassword,  database='TempStockData', port=1433, charset= 'utf8')
# for i in ds.index:
#     Script ='insert into tempHSMoney (ExchangeDateTime,HSMoney,SSMoney,NorthMoney,GGHSMoney,GGSSMoney,SouthSumMoney) VALUES ('
#     se=(',')
#     ds.iloc[i,0] = "'" + ds.iloc[i,0].replace('-', '')
#     ds.iloc[i,1] = str(ds.iloc[i,1])
#     ds.iloc[i,2] = str(ds.iloc[i,2])
#     ds.iloc[i,3] = str(ds.iloc[i,3])
#     ds.iloc[i,4] = str(ds.iloc[i,4])
#     ds.iloc[i,5] = str(ds.iloc[i,5])
#     ds.iloc[i,6] = str(ds.iloc[i,6])+"'"
#     s=(ds.iloc[i,0],ds.iloc[i,1],ds.iloc[i,2],ds.iloc[i,3],ds.iloc[i,4],ds.iloc[i,5], ds.iloc[i,6])
#     Script = Script + se.join(s)+')'
#     try:
#         cursor.execute(Script)
#         conn.commit()
#     except pyodbc.IntegrityError as e:
#         print(e)
#         continue
# conn.close
ds = ds.reindex(index=list(range(1,ds.shape[0])))
ds.reset_index(drop = True)
# ds.to_excel('C:/各类原创/工作簿1.xlsx')
print(ds)