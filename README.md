# My Discord Bot for Vinted Automation

This project is a Discord bot designed to automate interactions with the Vinted website, allowing users to buy and sell clothes, shoes, and accessories. The bot provides functionalities for user authentication, item filtering, real-time search, and automated purchases.

## Project Structure

```
my-discord-bot
├── cogs
│   ├── auth.py          # Manages user authentication
│   ├── filter.py        # Allows users to configure item filters
│   ├── search.py        # Implements continuous item search
│   ├── purchase.py      # Automates purchases and handles proxies
│   └── __init__.py      # Initializes the cogs package
├── requirements.txt      # Lists project dependencies
├── main.py               # Entry point of the bot
└── README.md             # Documentation for the project
```

## Features

- **User Authentication**: 
  - `/log-in`: Link your Vinted account.
  - `/log-out`: Unlink your Vinted account.

- **Filter Configuration**: 
  - `/filter-edit`: Set up item filters based on size, category, condition, etc.

- **Real-time Item Search**: 
  - `/search-start`: Start a continuous search for items and receive notifications via DM.

- **Automated Purchases**: 
  - Buy items directly through the bot with a "Buy" button in item embeds.
  - Proxy support and anti-bot/captcha handling for secure transactions.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-discord-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your bot token and other settings in `main.py`.

4. Run the bot:
   ```
   python main.py
   ```

## Usage Guidelines

- Use the commands in your Discord server where the bot is active.
- Ensure your Vinted account is properly linked for authentication features.
- Adjust filters as needed to refine your item search.

## Contributing

Feel free to submit issues or pull requests to enhance the functionality of the bot.