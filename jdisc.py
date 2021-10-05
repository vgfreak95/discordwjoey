import discord
import json as js


with open("token.json", "r") as js_file:
    creds = js.load(js_file)

x = 5
print(creds['key'])
print(type(creds))


