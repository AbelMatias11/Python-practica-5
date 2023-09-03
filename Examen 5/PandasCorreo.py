import pandas as pd
import sqlite3
import smtplib
from email.mime.text import MIMEText

data = pd.read_csv('Examen 5/candidates.csv')

conn = sqlite3.connect('candidates.db')

data.to_sql('candidates', conn, if_exists='replace', index=False)

conn.close()

average_experience = data['Yoe'].mean()
total_applications = len(data)

report = f"Informe de candidatos:\n\n- Experiencia promedio: {average_experience} años\n- Total de aplicaciones: {total_applications}"

print(report)

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'abelmatiasrocadelgado@gmail.com'
sender_password = 'njlwrsvnzxgiawya'
recipient_email = 'abelmatiasrocadelgado@gmail.com'

msg = MIMEText(report)
msg['Subject'] = 'Informe de candidatos'
msg['From'] = sender_email
msg['To'] = recipient_email

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Correo enviado exitosamente')
except Exception as e:
    print('Error al enviar el correo:', str(e))