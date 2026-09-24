def find_topic(topic_name, topics):
    for topic in topics:
        if topic["name"].lower() == topic_name.lower():
            return topic

    return None



def article_search(topic_id, topic_name, articles):
    found = False

    for article in articles:
        if article["topic_id"] == topic_id:
            print("\nTopic found")
            print("Topic:", topic_name)
            print("Title:", article["title"])
            print("Source:", article["source"])
            found = True

    if not found:
        print("Article not found")
