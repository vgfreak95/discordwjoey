import discord
import json as js


with open("token.json", "r") as js_file:
    creds = js.load(js_file)

print(creds['key'])
print(type(creds))


