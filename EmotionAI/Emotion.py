import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import datetime

classifier = pipeline("sentiment-analysis")

conn = sqlite3.connect('emotion_history.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS emotions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    text TEXT,
    sentiment TEXT
)
''')

def save_emotion_to_db(text, sentiment):
    saved = ""

    if sentiment == 'POSITIVE':
        saved = "ﻝﺎﺤﺷﻮﺧ"
    elif sentiment == 'NEGATIVE':
        saved = "ﺖﺣﺍﺭﺎﻧ"
    else:
        saved = "ﻡﻮﻠﻌﻣﺎﻧ"
    cursor.execute('''
    INSERT INTO emotions (date, text, sentiment)
    VALUES (?, ?, ?)
    ''', (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), text, saved))
    conn.commit()

def analyze_sentiment(text):
    result = classifier(text)
    sentiment = result[0]['label']
    print(sentiment)
    return sentiment

def get_response_based_on_sentiment(sentiment):
    responses = {
        'POSITIVE': "خیلی عالیه، ادامه بده",
        'NEGATIVE': "نگران نباش، همه چیز بهتر می‌شود",
        'NEUTRAL': "می‌خواهی بیشتر درباره‌اش صحبت کنی؟"
    }
    return responses.get(sentiment, ".لطفا بیشتر توضیح بده")

def analyze():
    user_input = input_text.get("1.0", tk.END).strip()  

    if not user_input:
        messagebox.showerror("خطا", "لطفا یک متن وارد کنید!")
        return

    sentiment = analyze_sentiment(user_input) 
    response = get_response_based_on_sentiment(sentiment) 

    save_emotion_to_db(user_input, sentiment)

    tempSentiment = ""

    if sentiment == 'POSITIVE':
        tempSentiment = "خوشحال"
    elif sentiment == 'NEGATIVE':
        tempSentiment = "ناراحت"
    else:
        tempSentiment = "نامعلوم"

    output_label.config(text=f"احساس شما: {tempSentiment}\nپاسخ سیستم: {response}")
    
    plot_emotions()

def plot_emotions():
    cursor.execute('SELECT sentiment, COUNT(*) FROM emotions GROUP BY sentiment')
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=['Sentiment', 'Count'])

    plt.figure(figsize=(6, 4))
    plt.bar(df['Sentiment'], df['Count'], color=['red', 'green', 'blue'])
    plt.xlabel('ﺕﺎﺳﺎﺴﺣﺍ')
    plt.ylabel('ﺩﺍﺪﻌﺗ')
    plt.title('ﻥﺍﺮﺑﺭﺎﮐ ﺕﺎﺳﺎﺴﺣﺍ ﻞﯿﻠﺤﺗ')
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("تحلیل احساسات با هوش مصنوعی")
root.iconbitmap("icons8-ai-100.ico")
root.geometry("400x400")

tk.Label(root, text=":متن خود را وارد کنید", font=('Arial', 12)).pack(pady=10)
input_text = tk.Text(root, height=5, width=40, font=('Arial', 12))
input_text.pack(pady=10)

analyze_button = tk.Button(root, text="تحلیل احساسات", command=analyze, font=('Arial', 12), bg="blue", fg="white")
analyze_button.pack(pady=10)

output_label = tk.Label(root, text=".نتیجه در اینجا نمایش داده می‌شود", font=('Arial', 12))
output_label.pack(pady=10)

root.mainloop()
