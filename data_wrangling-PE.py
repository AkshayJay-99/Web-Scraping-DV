from bs4 import BeautifulSoup
import requests
import pandas as pd  

url1 = 'https://companiesmarketcap.com/tata-consultancy-services/pe-ratio/#google_vignette'
company1 = 'TCS'
url2 = 'https://companiesmarketcap.com/infosys/pe-ratio/'
company2 = 'Infosys'
url3 = 'https://companiesmarketcap.com/wipro/pe-ratio/'
company3 = 'Wipro'
url4 = 'https://companiesmarketcap.com/hcl-technologies/pe-ratio/'
company4 = 'HCL Tech'
url5 = 'https://companiesmarketcap.com/tech-mahindra/pe-ratio/'
company5 = 'Tech-Mahindra'
url6 = 'https://companiesmarketcap.com/larsen-toubro-infotech/pe-ratio/'
company6 = 'LTI infotech'
url7 = 'https://companiesmarketcap.com/persistent-systems/pe-ratio/'
company7 = 'Persistent Systems'
url8 = 'https://companiesmarketcap.com/tanla/pe-ratio/'
company8 = 'Tanla Platforms'
url9 = 'https://companiesmarketcap.com/tata-elxsi/pe-ratio/'
company9 = 'Tata Elxsi'
url10 = 'https://companiesmarketcap.com/coforge/pe-ratio/'
company10 = 'Coforge'



def load_data(url,company):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')
    table = soup.find('table')
    columns = table.find_all('th')

    column_titles = [column.text for column in columns]

    df = pd.DataFrame(columns = column_titles)
    column_data = table.find_all('tr')[1:]
    for row in column_data:
        row_data = row.find_all('td')
        individual_row_data = [data.text for data in row_data]
        
        length = len(df)
        df.loc[length] = individual_row_data

    df['Company'] = company
    return df


df1 = load_data(url1,company1)
df2 = load_data(url2,company2)
df3 = load_data(url3,company3)
df4 = load_data(url4,company4)
df5 = load_data(url5,company5)
df6 = load_data(url6,company6)
df7 = load_data(url7,company7)
df8 = load_data(url8,company8)
df9 = load_data(url9,company9)
df10 = load_data(url10,company10)

it_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10])
it_df['industry'] = 'Tech'
it_df.to_csv('it_pe_ratio.csv', index=False)
