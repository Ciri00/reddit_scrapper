
import praw
import datetime
import config

def connect_to_reddit():
    try:
        reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=config.REDDIT_USER_AGENT
        )
        return reddit
    except Exception as e:
        print("Failed to connect to Reddit API:", e)
        return None

def scrape_subreddit(subreddit_name, limit=50, time_filter="week"):
    reddit = connect_to_reddit()
    if not reddit:
        return []

    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts_data = []

        for post in subreddit.top(limit=limit, time_filter=time_filter):
            post_info = {
                "id": post.id,
                "title": post.title,
                "score": post.score,
                "author": str(post.author),
                "created_utc": datetime.datetime.fromtimestamp(post.created_utc).isoformat(),
                "url": post.url,
                "num_comments": post.num_comments,
                "selftext": post.selftext,
                "comments": []
            }

            post.comments.replace_more(limit=0)
            for comment in post.comments.list()[:15]:
                post_info["comments"].append({
                    "author": str(comment.author),
                    "body": comment.body,
                    "score": comment.score,
                    "created_utc": datetime.datetime.fromtimestamp(comment.created_utc).isoformat()
                })

            posts_data.append(post_info)

        return posts_data

    except Exception as e:
        print(f"Error while scraping r/{subreddit_name}: {e}")
        return []
