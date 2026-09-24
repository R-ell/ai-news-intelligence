import json

import topic_utility





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

        new_question = {
            "id": len(questions) + 201,
            "topic_id": topic["id"],
            "question": user_question
        }

        questions.append(new_question)

        with open("catalog.json", "w") as file:
            json.dump(catalog, file, indent=4)

        topic_utility.article_search(topic["id"], topic["name"], articles)

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












        


