import requests
import psycopg2

url = 'https://randomuser.me/api/?nat=us&randomapi'
i = 0

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}
try:
    conn = psycopg2.connect(database='db',
                        user='postgres',
                        password='1111',
                        host="postgres")
    print("Succesful")
except:
    print("Error")
i = 0
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Info(ID INTEGER, Gender TEXT, Title TEXT, First_Name TEXT, Last_Name TEXT, Street_Number TEXT, Street_Name TEXT, City TEXT, State TEXT, Country TEXT, Postcode TEXT, Email TEXT, Username TEXT, Password TEXT, Date_Of_B TEXT, Age TEXT, Phone TEXT, Cell TEXT, URL_Of_Photo TEXT, Nationality TEXT)")
while (i < 100):
    responce = requests.get(url, headers=headers, params=None)
    data = responce.json()
    data['results'] = data['results'][0]
    if (data['results']['gender'] == "male"):
        cursor.execute(
            "INSERT INTO Info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                           i,
                           data['results']['gender'],
                           data['results']['name']['title'],
                           data['results']['name']['first'],
                           data['results']['name']['last'],
                           data['results']['location']['street']['number'],
                           data['results']['location']['street']['name'],
                           data['results']['location']['city'],
                           data['results']['location']['state'],
                           data['results']['location']['country'],
                           data['results']['location']['postcode'],
                           data['results']['email'],
                           data['results']['login']['username'],
                           data['results']['login']['password'],
                           data['results']['dob']['date'],
                           data['results']['dob']['age'],
                           data['results']['phone'],
                           data['results']['cell'],
                           data['results']['picture']['large'],
                           data['results']['nat']
                        )
                       )
        i += 1
conn.commit()
conn.close()
