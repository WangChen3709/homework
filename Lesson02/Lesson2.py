from bs4 import BeautifulSoup
import requests
import random
import pandas as pd



def page_content(url):

	header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 '}
	response = requests.get(url,headers=header,timeout=10)
	soup = BeautifulSoup(response.text,'html.parser')
	return soup

def analysis_data(soup):
	tousu_page = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc','problem', 'datetime', 'status'])
	temp_data = soup.find('div',class_="tslb_b")
	tr_list = temp_data.find_all('tr')

	for tr in tr_list:
		temp={}
		td_list=tr.find_all("td")
		if len(td_list)>0:
			temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], temp['datetime'], temp['status']=td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
			tousu_page = tousu_page.append(temp, ignore_index=True)
	return tousu_page

Result=pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc','problem', 'datetime', 'status'])


def main():
	page_number = int(input("How many pages you want to check?"))
	for number in range(page_number):
		url_part = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-' 
		url=url_part+str(number+1)+'.shtml'
		Soup = page_content(url)
		Tousu_Page = analysis_data(Soup)
		Result = Result.append(Tousu_Page, ignore_index=True)
	Result.to_csv('result.csv',index=False)

if __name__ =='__mian__':
	main()

