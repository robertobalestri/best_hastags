# Best Hashtags

Best Hashtags is a Python tool that helps you find the best hashtags for a given word. It retrieves popular hashtags from the website `https://best-hashtags.com/hashtag/{search_word}/`.

## Features

- Retrieve top hashtags for any given word.
- Option to get a specific number of hashtags.
- Option to get hashtags in a random order.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/robertobalestri/best_hashtags.git
   cd best_hashtags
   ```

2. **Create a Python virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To get the best hashtags for a given word, you can use the following command:

```bash
python src/best_hashtags.py <search_word>
```

Replace `<search_word>` with the word you want to search for hashtags.

### Example

```bash
python src/best_hashtags.py music
```

This will print the top 30 hashtags related to the word "music".

## Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.

## License

This project is licensed under the MIT License.
```

robertobalestri: ok, modify the file

GitHub Copilot: Sure, here is the updated README.md file:

```markdown
# Best Hashtags

Best Hashtags is a Python tool that helps you find the best hashtags for a given word. It retrieves popular hashtags from the website `https://best-hashtags.com/hashtag/{search_word}/`.

## Features

- Retrieve top hashtags for any given word.
- Option to get a specific number of hashtags.
- Option to get hashtags in a random order.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/robertobalestri/best_hashtags.git
   cd best_hashtags
   ```

2. **Create a Python virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To get the best hashtags for a given word, you can use the following command:

```bash
python src/best_hashtags.py <search_word>
```

Replace `<search_word>` with the word you want to search for hashtags.

### Example

```bash
python src/best_hashtags.py music
```

This will print the top 30 hashtags related to the word "music".

## Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.

## License

This project is licensed under the MIT License.