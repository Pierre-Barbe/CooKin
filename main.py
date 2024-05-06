import requests
import customtkinter as ctk
from openai import OpenAI


# City name import
city = input('Please input the city name : ')

# Corresponding wttr.in url for selected city
url = 'https://wttr.in/{}'.format(city)

# Weather ASCII answer from wttr url request
weather_res = requests.get(url)

print(weather_res.text)

# OpenAI key for requests (warning : do not exceed subscription requests !)
client = OpenAI(api_key="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")

# ChatGPT request
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    # Defining Assistant as a proficient cooking recipy provider to guide future answer.
    {"role": "system", "content": "You are a cooking assistant, skilled in prociding detailed recipies based on local weather."},
    {"role": "user", "content": "Provide a cooking recipe matching the following weather conditions and geographical coordinates." + weather_res.text}
  ]
)

# Printing results in pretty window
app = ctk.CTk()
label = ctk.CTkLabel(app, text=completion.choices[0].message.content, fg_color="transparent", anchor="w", justify="left")
label.grid(row=0, column=0, padx=20, pady=20)
app.mainloop()