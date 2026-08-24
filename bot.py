import discord
import requests

token = 'YOUR_BOT_TOKEN_HERE'  # Replace with your bot token
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content.startswith('!ip'):
            try:
                ip=message.content.split(' ')[1]
                response= requests.get(f'http://ip-api.com/json/{ip}')
                data=response.json()
                await message.channel.send(f'IP: {data["query"]}\nCity: {data["city"]}\nRegion: {data["regionName"]}\nCountry: {data["country"]}')
            except Exception as e:
                await message.channel.send(f'Error: {str(e)}')
        if message.content.startswith('!dns'):
            try:
                dns=message.content.split(' ')[1]
                response= requests.get(f"http://edns.ip-api.com/json{dns}")
                data=response.json()
                dns_ip = data['dns']['ip']
                dns_geo = data['dns']['geo']
                edns_ip = data['edns']['ip']
                edns_geo = data['edns']['geo']
                await message.channel.send(f'DNS IP: {dns_ip}\nDNS Geo: {dns_geo}\nEDNS IP: {edns_ip}\nEDNS Geo: {edns_geo}')
            except Exception as e:
                await message.channel.send(f'Error: {str(e)}')
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)