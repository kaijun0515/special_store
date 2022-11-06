import streamlit as st
import requests
headers = {"accept": "application/json"}

def getAllBookstore():
	url='https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res=response.json()
	return res

def getSpecificBookstore(items, county):
	specificBookstoreList = []
	for item in items:
		name = item['cityName']
		if name not in specificBookstoreList:
			specificBookstoreList.append(name)

	# 如果 name 不是我們選取的 county 則跳過
	# hint: 用 if-else 判斷並用 continue 跳過
	return specificBookstoreList

def getCountyOption(items):
	optionList = []
	for item in items:
		headers.get('cityname')
		name = item['cityName'][0:3]
		if name not in optionList :
			optionList.append(name)
	return optionList

def app():
	bookstorelist = getAllBookstore()
	countyOption = getCountyOption(bookstorelist)
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstorelist))
	county = st.selectbox('請選擇縣市', countyOption)
	specificBookstore = getSpecificBookstore(bookstorelist,county)
	num = len(specificBookstore)
	st.write(f'總共有{num}間書店')

if __name__ == '__main__':
    app()