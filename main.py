import sys
sys.path.append('./backend')

from reddit_scrapper import scrape_subreddit
import json

if __name__ == "__main__":
    subreddit = "food"
    data = scrape_subreddit(subreddit, limit=50)

    print(f"Scraped {len(data)} posts from r/{subreddit}")
    
    # Save to a file
    with open("reddit_data_food.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
