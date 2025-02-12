# 📈 Best Hashtags

**Best Hashtags** is a Python tool that helps you find the most popular hashtags for a given word. It’s perfect for content creators, marketers, and social media enthusiasts looking to boost their reach with relevant hashtags.

## 🚀 Features

- **Retrieve Top Hashtags**: Instantly find the most popular hashtags for any keyword.
- **Customizable Results**: Get a specific number of hashtags based on your needs.
- **Randomized Option**: Shuffle the hashtags for more variety.

## ⚙️ Installation

You can install **Best Hashtags** in two ways:

### 1️⃣ Install via PyPI (Recommended)

The easiest way to get started is by installing the package from [PyPI](https://pypi.org/project/best-hashtags/0.1.0/):

```pip install best-hashtags```

## 💡 Usage

You can use **Best Hashtags** directly in your Python code.

### Example 1: Using from the Command Line

```python src/best_hashtags.py music```

This will display the top 30 hashtags related to **"music"**.

### Example 2: Using in Python Scripts

```from best_hashtags import BestHashtags

# Initialize the BestHashtags class
hashtag_finder = BestHashtags()

# Search for hashtags related to "music"
hashtags = hashtag_finder.get_hashtags('music', quantity=30, ordered=True)

# Display the results
print(hashtags)```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

💡 *Contributions and feedback are always welcome!*
