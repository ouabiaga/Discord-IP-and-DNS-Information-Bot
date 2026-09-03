# Discord IP and DNS Information Bot

A simple Discord bot built with Python and `discord.py`. The bot provides a basic connection check and sends IP/DNS information to a Discord channel using the `ip-api.com` service.

## Features

- Responds to `ping` with `pong`.
- Displays the city, region, and country for an IP address with `!ip <address>`.
- Displays DNS and EDNS information with `!dns <address>`.
- Does not respond to its own messages.

## Requirements

- Python 3.9 or later
- A Discord application and bot account
- The `discord.py` and `requests` packages

## Installation

1. Clone the project and move into its directory:

   ```bash
   git clone https://github.com/ouabiaga/Discord-IP-and-DNS-Information-Bot
   cd Discord-IP-and-DNS-Information-Bot
   python bot.py
   ```

2. Install the required packages:

   ```bash
   pip install discord.py requests
   pip install discord
   ```

3. Create an application in the [Discord Developer Portal](https://discord.com/developers/applications), add a bot from the **Bot** section, and copy its token.

4. Replace the value in the following line in `bot.py` with your bot token:

   ```python
   token = 'YOUR_BOT_TOKEN_HERE'
   ```

   Never upload your token to GitHub or any other public location. If the token is accidentally exposed, regenerate it through the Developer Portal.

5. Enable **Message Content Intent** in the bot settings. Grant the bot permission to read and send messages when adding it to your server.

## Running the Bot

```bash
python bot.py
```

When the bot connects successfully, the logged-in account name is printed in the terminal.

## Commands

| Command | Description | Example |
| --- | --- | --- |
| `ping` | Checks whether the bot is running. | `ping` |
| `!ip <IP>` | Returns location information for an IP address. | `!ip 8.8.8.8` |
| `!dns <address>` | Returns DNS and EDNS information. | `!dns 8.8.8.8` |

## Data Source

IP and DNS queries are sent to the [IP-API](http://ip-api.com/) service. Follow the service's terms of use and rate limits. Do not share sensitive information, such as users' IP addresses, without permission.

## License

This project is subject to the terms in the repository's [LICENSE](LICENSE) file.
