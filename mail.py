import pandas as pd
import yagmail
yag = yagmail.SMTP('fisadisciplinei@gmail.com',
                   oauth2_file="client_secret_638768354585-o5htu0p3patctp2im6bh2d86kilhfv3u.apps.googleusercontent.com.json")


df_curs = pd.read_csv('tabel_materii.csv', dtype=str)
df_curs.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = pd.read_csv('adrese_mail.csv', dtype=str)
df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


for i in range(20):
    # in if we have to check if the email address is empty
    if df["email"][i] == df["email"][i]:
        nrdisc = df["nrdisc"][i]
        email = df["email"][i]
        contents = [
            f'Buna ziua, \n Va trimit atasat fisa disciplinei pentru cursul {nrdisc} pentru anul universitar 2022-2023. \n Va multumesc, \n Vlad']
        print(df["nrdisc"][i], df["email"][i])
        try:
            yag.send('fisadisciplinei@gmail.com',
                     f'Fisa Disciplinei {nrdisc}', contents, attachments=[f'files/curs_{nrdisc.replace(".","_")}.docx'])
        except:
            print(f"Did not work for {nrdisc}")
