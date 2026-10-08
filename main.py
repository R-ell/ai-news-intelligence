import json

import topic_utility
import test_api
#import database
import llm
import db




#database.setup_db()

with open("catalog.json", "r") as file:
    catalog = json.load(file)


topics = catalog["topics"]
articles = catalog["articles"]
questions = catalog["questions"]



q1 = input(
    "Would you like to read a news article (press y) "
    "or add an article (press a): "
)


if q1.lower() == "y":

    topic_name = input(
        "What topic would you like to learn about?\n"
        "AI\n"
        "Robotics\n"
        "LLMs\n"
        "Topic: "
    )

    topic = topic_utility.find_topic(topic_name, topics)

    if topic is None:
        print("That topic does not exist.")

    else:

        user_question = input(
            "What would you like to know about "
            + topic["name"] + "?\n"
        )

        print("You asked:", user_question)

        api_articles=test_api.get_news(topic["name"])
        #database.save_article(api_articles)
        print(len(api_articles))
        """

        for articles in api_articles[0:3]:
            article_title=articles.title
            article_source=articles.source
            print(article_title)
            print(article_source)
        """

        new_question = {
            "id": len(questions) + 201,
            "topic_id": topic["id"],
            "question": user_question
        }

        questions.append(new_question)

        with open("catalog.json", "w") as file:
            json.dump(catalog, file, indent=4)

        print(f"\nProcessing the top 3 articles for {topic['name']}...")

        for article in api_articles[0:3]:
            article_title = article.title
            print("\nAsking AI to analyse:", article_title)
            
            ai_summary = llm.analyze_article(article_title)
            print("AI summary:", ai_summary)
            
            db.save_data(
                title=article_title, 
                source=article.source, 
                url=article.url, 
                published_date=article.date_pub, 
                ai_summary=ai_summary
            )
        """

        sample_text=api_articles[0].title
        print("\nAsking AI to analyse",sample_text)
    
        ai_summary=llm.analyze_article(sample_text)
    
        print("\nAI summary:")
        print(ai_summary)
        """
    
        db.save_data(
           title=api_articles[0].title, 
            source=api_articles[0].source, 
            url=api_articles[0].url, 
            published_date=api_articles[0].published_date, 
            ai_summary=ai_summary
        )

        #topic_utility.article_search(topic["id"], topic["name"], articles)

elif q1.lower() == "a":

    topic_name = input(
        "What topic is this article related to?\n"
        "AI\n"
        "Robotics\n"
        "LLMs\n"
        "Topic: "
    )

    topic = topic_utility.find_topic(topic_name, topics)

    if topic is None:
        print("That topic does not exist.")

    else:

        new_article = {
            "id": len(articles) + 101,
            "topic_id": topic["id"],
            
            "source": input(
                "What institution did you get this information from: "
            ),
            "title": input(
                "What is the headline of this article: "
            )
        }

        articles.append(new_article)

        with open("catalog.json", "w") as file:
            json.dump(catalog, file, indent=4)

        print("Article added successfully.")



#database.view_article()
    """

    sample_text=api_articles[0].title
    print("\nAsking AI to analyse",sample_text)

    ai_summary=llm.analyze_article(sample_text)

    print("\nAI summary:")
    print(ai_summary)
"""
   





        


