# Dragon-Nest-Patch-Discord-Notifier

This is a simple Discord bot designed to track and announce patch updates for the Dragon Nest SEA game in a designated Discord channel. The bot periodically checks the game’s patch version from a specified URL and notifies the channel when a new update is detected.

**Features**
- Checks for updates to Dragon Nest SEA patch version from a specified URL.
- Sends an embedded message to a Discord channel when a new patch is available.
- Automatically updates the patch version locally once announced.

**Project Structure**
- `main.py`: Contains the main bot code, including update checks and Discord channel message handling.
- `update.pyv: Manages patch version fetching, storage, and parsing.
- `PatchVersionInfo.cfg`: Stores the current patch version number to compare against the latest version.

**Requirements**
- Python 3.8+
- [discord.py](https://discordpy.readthedocs.io/) library
- Other required libraries are specified below.
## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Install the required Python packages:
```bash
pip install discord.py requests
```

3. Set up environment variables:
     - `TOKEN`: Your Discord bot token.
     - `CHANNEL_ID`: The ID of the Discord channel to send updates.
     - `URL`: The URL to fetch the latest patch version from.
       
(**Important!**) Create a file named .env in your project’s root directory and add the following:
```env
# Your Discord bot token
TOKEN=your_discord_bot_token_here

# The ID of the Discord channel where the bot will send update notifications
CHANNEL_ID=your_discord_channel_id_here

# URL to check for the latest Dragon Nest SEA patch version
URL=https://example.com/patch/version/PatchInfoServer.cfg
```
```bash
pip install python-dotenv
```

4. Create the `PatchVersionInfo.cfg` file in the project directory if not present, and add:
```yaml
version 1100
```

5. Run the bot:
```bash
python main.py
```
## Usage

The bot will automatically begin checking for updates every 10 seconds once it’s online. When a new patch version is detected, it will send an embedded message in the specified Discord channel, including the new and old version numbers.
