# Reddit Scraper

A Python-based Reddit scraper to collect and store posts and comments from a specified subreddit using the [PRAW](https://praw.readthedocs.io/en/latest/) (Python Reddit API Wrapper). This tool is useful for data analysis, research, sentiment tracking, and more.

## 🚀 Features

- Scrapes posts and comments from a given subreddit  
- Collects post metadata (title, score, ID, URL, number of comments, creation time)  
- Stores output as structured CSV files  
- Uses Reddit API via PRAW  
- Simple and customizable configuration

---

## 📁 Project Structure

```
reddit_scrapper/
├── .gitignore
├── README.md
├── requirements.txt
├── reddit_scrapper.py         # Main script to initiate scraping
├── config.py                  # Subreddit and scraping parameters
└── output/                    # Folder where CSV results are stored
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ciri00/reddit_scrapper.git
cd reddit_scrapper
```

### 2. Create a Reddit App & Get Credentials

- Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)  
- Create an app with **script** type  
- Note your:
  - `client_id`
  - `client_secret`
  - `username`
  - `password`
  - `user_agent`

### 3. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Configure `config.py`

Replace placeholder values with your Reddit credentials and set the target subreddit:

```python
REDDIT_CONFIG = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "username": "your_username",
    "password": "your_password",
    "user_agent": "your_custom_user_agent"
}

TARGET_SUBREDDIT = "your_target_subreddit"
LIMIT = 100  # Number of posts to scrape
```

---

## 🧠 How to Use

To run the scraper:

```bash
python reddit_scrapper.py
```

This will scrape the specified number of posts from the configured subreddit and save them (including comments) in the `output/` directory as CSV files.

---

## 📝 Output Format

- **posts.csv** — Includes fields like:
  - Title  
  - Post ID  
  - URL  
  - Score  
  - Number of Comments  
  - Date Created

- **comments.csv** — Includes:
  - Comment body  
  - Score  
  - Parent post ID  
  - Author  
  - Timestamp

---

## 📊 Use Cases

- Sentiment Analysis  
- Trend Tracking  
- Keyword Extraction  
- NLP Projects  
- Academic Research  

---

## 🛠️ Built With

- Python 3.8+  
- [PRAW](https://praw.readthedocs.io/en/latest/)  
- `pandas`  
- `csv`  
- Reddit API  

---

## 📌 To-Do / Future Enhancements

- Add sentiment analysis pipeline  
- Include keyword extraction using NLP libraries (e.g., spaCy or NLTK)  
- Store output in databases (MongoDB, PostgreSQL)  
- Interactive dashboard for visualization (Plotly / Dash)  
- Option to scrape specific flair or post types (e.g., questions, media)  

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests to improve functionality or fix bugs.

---

## 📬 Contact

For questions or collaboration opportunities, reach out via GitHub Issues or email: [your_email@example.com]
