from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    GITHUB_URL="https://github.com/abdullahr-2",
    LINKEDIN_URL="https://www.linkedin.com/in/abdullahr2/",
    CONTACT_EMAIL="abdullahr2.ca@gmail.com",
)

PROJECTS = (
    {
        "name": "Signal",
        "repository": "https://github.com/alijaffary603/HTC-1",
        "stack": ("Python", "React", "TypeScript", "Gemini API", "Google Maps"),
        "about": (
            "At Hack the Change YYC, my team built Signal to help Albertans explore how "
            "planned energy projects could affect demand for their occupation. I built the "
            "regional project map and a career advisor that turns a user’s goals, budget, "
            "and available study time into a step-by-step plan."
        ),
    },
    {
        "name": "Spring Store",
        "repository": "https://github.com/abdullahr-2/spring-store",
        "stack": ("Java", "Spring Boot", "Spring Data JPA", "MySQL"),
        "about": (
            "I’m developing a store backend as part of a Spring Boot course. I’ve worked "
            "on the relationships between products and categories, queried inventory with "
            "pagination, and built user lookups that return just an ID, name, and email."
        ),
    },
    {
        "name": "Vehicle Dealership",
        "repository": "https://github.com/abdullahr-2/vehicle-dealership",
        "stack": ("Java", "JavaFX", "FXML", "JUnit"),
        "about": (
            "My team built a desktop app for managing a simulated dealership’s inventory, "
            "from motorcycles to planes. I implemented the side-by-side comparison of price, "
            "mileage, horsepower, and model year, along with views for finding the newest "
            "and oldest vehicles on the lot."
        ),
    },
    {
        "name": "Finding X",
        "repository": "https://github.com/abdullahr-2/finding-x",
        "stack": ("Python", "Flask", "Jinja", "SQLite"),
        "about": (
            "For my CS50x final project, I built a pre-algebra practice app. Students choose "
            "a quiz length, solve randomly generated equations and word problems, then review "
            "their answers alongside the correct ones to see where they went wrong."
        ),
    },
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/resume")
def resume():
    return render_template("resume.html")
