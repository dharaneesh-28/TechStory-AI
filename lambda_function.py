
import json
import boto3
import random
from datetime import datetime, timezone, timedelta

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("TechStoryCreations")

CHARACTERS = [
    "A young engineer named Priya",
    "An old scientist named Dr. Rajan",
    "A curious student named Arun",
    "A retired astronaut named Maya",
    "A street-smart hacker named Zara",
    "A village farmer named Karthik",
    "A blind musician named Leela",
    "A 10-year-old coding prodigy named Sam",
    "A firefighter named Alex",
    "A marine biologist named Deepa"
]

TECHNOLOGIES = [
    ("AI + IoT", "Artificial Intelligence combined with Internet of Things"),
    ("Robotics + Drones", "Autonomous robots working with aerial drones"),
    ("Blockchain + Healthcare", "Decentralized systems securing medical records"),
    ("AR + Education", "Augmented Reality transforming how students learn"),
    ("Quantum Computing + Weather", "Quantum processors predicting extreme weather"),
    ("5G + Emergency", "Ultra-fast networks enabling instant emergency response"),
    ("Biotech + Agriculture", "Genetic engineering creating drought-resistant crops"),
    ("Neural Interface + Disability", "Brain-computer interfaces restoring lost abilities"),
    ("Edge Computing + Traffic", "Local processing eliminating city traffic jams"),
    ("Green AI + Energy", "Energy-efficient AI reducing carbon footprints")
]

PROBLEMS = [
    "detected an unusual pattern that no human could see",
    "discovered a hidden danger threatening thousands of lives",
    "found a solution to a problem that puzzled experts for decades",
    "accidentally triggered a chain reaction that changed everything",
    "received a mysterious signal that led to an incredible breakthrough",
    "noticed something strange happening at exactly midnight every day",
    "built a prototype in a garage that outperformed million-dollar systems",
    "connected dots between two unrelated events that saved a community",
    "challenged the conventional wisdom and proved everyone wrong",
    "turned a catastrophic failure into the innovation of the century"
]

SOLUTIONS = [
    "The system now protects over 10,000 people daily and has been adopted by 15 countries.",
    "What started as a small experiment became a global standard within two years.",
    "The technology reduced costs by 90% and made the solution accessible to everyone.",
    "Today, this innovation runs silently in the background, saving lives without anyone knowing.",
    "The open-source version has been downloaded 2 million times and counting.",
    "Three years later, it won the Global Innovation Award and inspired a new generation of builders.",
    "The pilot program was so successful that it expanded to 50 cities within months.",
    "It proved that the best solutions often come from the most unexpected places.",
    "Now taught in universities worldwide, it changed how we think about technology's role in society.",
    "The ripple effect of this invention is still being measured, but early estimates suggest billions saved."
]

LOCATIONS = [
    "in a bustling city in India",
    "in a remote village near the mountains",
    "in an underground research lab",
    "aboard a floating research station",
    "in a converted warehouse turned innovation hub",
    "in a hospital emergency room at 3 AM",
    "in a school classroom during a power outage",
    "at a climate research station in the Arctic",
    "in a crowded train station during rush hour",
    "in a small fishing town facing rising sea levels"
]


def lambda_handler(event, context):
    ist = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(ist)
    today = now.strftime("%Y-%m-%d")
    day_name = now.strftime("%A")

    random.seed(today)

    character = random.choice(CHARACTERS)
    tech_name, tech_desc = random.choice(TECHNOLOGIES)
    problem = random.choice(PROBLEMS)
    solution = random.choice(SOLUTIONS)
    location = random.choice(LOCATIONS)

    title = generate_title(character, tech_name)
    story = generate_story(character, tech_name, tech_desc, problem, solution, location)

    table.put_item(Item={
        "date": today,
        "category": tech_name,
        "title": title,
        "story": story,
        "character": character,
        "technology": tech_name,
        "tech_description": tech_desc,
        "timestamp": now.isoformat(),
        "day_name": day_name
    })

    return {
        "statusCode": 200,
        "body": json.dumps({
            "date": today,
            "day": day_name,
            "title": title,
            "story": story,
            "technology": tech_name,
            "tech_description": tech_desc
        })
    }


def generate_title(character, tech_name):
    templates = [
        "The Day {} Changed Everything with {}",
        "How {} Saved the World Using {}",
        "When {} Discovered the Power of {}",
        "{} and the {} Revolution",
        "The Unexpected Hero: {} and {}"
    ]
    name = character.split("named ")[-1] if "named " in character else character
    return random.choice(templates).format(name, tech_name)


def generate_story(character, tech_name, tech_desc, problem, solution, location):
    story = "{} was working {} when something extraordinary happened. ".format(character, location)
    story += "Using {} - {} - they {}. ".format(tech_name, tech_desc, problem)
    story += "What followed was nothing short of remarkable. "
    story += "Against all odds, a breakthrough emerged. "
    story += solution + "\n\n"
    story += "Technology: {}\n".format(tech_name)
    story += "Real-world application: {}\n".format(tech_desc)
    story += "Key insight: Innovation happens when curiosity meets persistence."
    return story

