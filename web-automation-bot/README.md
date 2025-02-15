# Web Automation Bot

This project is a web automation bot built using Python and Selenium. It automates tasks on a specified website, including logging in, navigating to sections, and performing actions on available tasks.

## Project Structure

```
web-automation-bot
├── src
│   ├── aviso_bot.py        # Main logic for the web automation bot
│   └── utils
│       └── __init__.py    # Utility functions and classes
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd web-automation-bot
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Configure your credentials**:
   Open `src/aviso_bot.py` and replace the placeholder email and password with your actual credentials.

2. **Run the bot**:
   Execute the following command to start the bot:
   ```
   python src/aviso_bot.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.