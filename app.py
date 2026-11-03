from flask import Flask, render_template, request, session, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = "quizmaster-secret-key"

# ==============================
# QUIZ QUESTIONS - 40 QUESTIONS
# ==============================

questions = [

    # PYTHON QUESTIONS
    {"category": "Python", "question": "Which language is used for data analysis?", "options": ["HTML", "Python", "CSS", "XML"], "answer": "Python", "explanation": "Python is widely used for data analysis."},
    {"category": "Python", "question": "Which symbol starts a Python comment?", "options": ["//", "#", "/*", "&"], "answer": "#", "explanation": "Python uses # for comments."},
    {"category": "Python", "question": "Which data type stores True or False?", "options": ["String", "Integer", "Boolean", "List"], "answer": "Boolean", "explanation": "Boolean stores True or False."},
    {"category": "Python", "question": "Which function displays output?", "options": ["input()", "print()", "show()", "display()"], "answer": "print()", "explanation": "print() displays output."},
    {"category": "Python", "question": "Which keyword defines a function?", "options": ["function", "define", "def", "fun"], "answer": "def", "explanation": "def defines functions."},
    {"category": "Python", "question": "Which brackets create a list?", "options": ["()", "{}", "[]", "<>"], "answer": "[]", "explanation": "Lists use square brackets."},
    {"category": "Python", "question": "Which operator is used for exponentiation?", "options": ["*", "**", "//", "%"], "answer": "**", "explanation": "** is the exponentiation operator."},
    {"category": "Python", "question": "Which keyword is used for a loop?", "options": ["repeat", "for", "loop", "iterate"], "answer": "for", "explanation": "for creates a loop."},
    {"category": "Python", "question": "What is the extension of a Python file?", "options": [".html", ".css", ".py", ".java"], "answer": ".py", "explanation": "Python files use .py."},
    {"category": "Python", "question": "Which function gets user input?", "options": ["scan()", "get()", "input()", "read()"], "answer": "input()", "explanation": "input() accepts user input."},

    # HTML QUESTIONS
    {"category": "HTML", "question": "Which tag creates a hyperlink?", "options": ["<p>", "<h1>", "<a>", "<img>"], "answer": "<a>", "explanation": "The anchor tag creates hyperlinks."},
    {"category": "HTML", "question": "Which tag creates a paragraph?", "options": ["<p>", "<div>", "<br>", "<h1>"], "answer": "<p>", "explanation": "The p tag creates paragraphs."},
    {"category": "HTML", "question": "Which tag inserts an image?", "options": ["<image>", "<img>", "<pic>", "<src>"], "answer": "<img>", "explanation": "The img tag inserts images."},
    {"category": "HTML", "question": "Which tag creates the largest heading?", "options": ["<h6>", "<head>", "<h1>", "<title>"], "answer": "<h1>", "explanation": "h1 is the largest heading."},
    {"category": "HTML", "question": "Which attribute specifies an image path?", "options": ["href", "src", "alt", "link"], "answer": "src", "explanation": "src specifies the image source."},
    {"category": "HTML", "question": "Which tag creates an unordered list?", "options": ["<ol>", "<li>", "<ul>", "<list>"], "answer": "<ul>", "explanation": "ul creates an unordered list."},
    {"category": "HTML", "question": "Which tag creates a line break?", "options": ["<break>", "<br>", "<lb>", "<hr>"], "answer": "<br>", "explanation": "br creates a line break."},
    {"category": "HTML", "question": "Which tag creates a table row?", "options": ["<td>", "<th>", "<tr>", "<table>"], "answer": "<tr>", "explanation": "tr defines a table row."},
    {"category": "HTML", "question": "Which attribute provides alternative image text?", "options": ["src", "alt", "href", "title"], "answer": "alt", "explanation": "alt provides alternative text."},
    {"category": "HTML", "question": "Which tag creates a form?", "options": ["<input>", "<form>", "<button>", "<label>"], "answer": "<form>", "explanation": "form creates an HTML form."},

    # CSS QUESTIONS
    {"category": "CSS", "question": "Which language styles webpages?", "options": ["Python", "CSS", "SQL", "C"], "answer": "CSS", "explanation": "CSS styles webpages."},
    {"category": "CSS", "question": "Which property changes text color?", "options": ["background", "font", "color", "size"], "answer": "color", "explanation": "color changes text color."},
    {"category": "CSS", "question": "Which property changes background color?", "options": ["color", "background-color", "font-size", "margin"], "answer": "background-color", "explanation": "background-color sets background color."},
    {"category": "CSS", "question": "Which symbol selects a class?", "options": ["#", ".", "*", "&"], "answer": ".", "explanation": "A dot selects a CSS class."},
    {"category": "CSS", "question": "Which symbol selects an ID?", "options": [".", "#", "@", "$"], "answer": "#", "explanation": "A hash selects an ID."},
    {"category": "CSS", "question": "Which property changes text size?", "options": ["font-size", "text-color", "size", "font-style"], "answer": "font-size", "explanation": "font-size changes text size."},
    {"category": "CSS", "question": "Which property adds space outside an element?", "options": ["padding", "margin", "border", "width"], "answer": "margin", "explanation": "margin creates outer spacing."},
    {"category": "CSS", "question": "Which property adds space inside an element?", "options": ["margin", "padding", "outline", "display"], "answer": "padding", "explanation": "padding creates inner spacing."},
    {"category": "CSS", "question": "Which property makes text bold?", "options": ["font-weight", "font-size", "text-align", "font-color"], "answer": "font-weight", "explanation": "font-weight controls text thickness."},
    {"category": "CSS", "question": "Which display value enables Flexbox?", "options": ["block", "inline", "flex", "none"], "answer": "flex", "explanation": "display: flex enables Flexbox."},

    # GENERAL KNOWLEDGE QUESTIONS
    {"category": "General Knowledge", "question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars", "explanation": "Mars is known as the Red Planet."},
    {"category": "General Knowledge", "question": "What is the capital of France?", "options": ["London", "Paris", "Rome", "Berlin"], "answer": "Paris", "explanation": "Paris is the capital of France."},
    {"category": "General Knowledge", "question": "How many days are in a leap year?", "options": ["365", "366", "364", "360"], "answer": "366", "explanation": "A leap year has 366 days."},
    {"category": "General Knowledge", "question": "Which is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific", "explanation": "The Pacific is the largest ocean."},
    {"category": "General Knowledge", "question": "Which animal is known as King of the Jungle?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "answer": "Lion", "explanation": "The lion is commonly called King of the Jungle."},
    {"category": "General Knowledge", "question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7", "explanation": "There are seven continents."},
    {"category": "General Knowledge", "question": "Which gas do plants absorb?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Carbon dioxide", "explanation": "Plants absorb carbon dioxide during photosynthesis."},
    {"category": "General Knowledge", "question": "Which is the fastest land animal?", "options": ["Lion", "Horse", "Cheetah", "Tiger"], "answer": "Cheetah", "explanation": "The cheetah is the fastest land animal."},
    {"category": "General Knowledge", "question": "What is the currency of Japan?", "options": ["Dollar", "Yen", "Euro", "Rupee"], "answer": "Yen", "explanation": "Japan uses the Yen."},
    {"category": "General Knowledge", "question": "Which organ pumps blood?", "options": ["Brain", "Lungs", "Heart", "Kidney"], "answer": "Heart", "explanation": "The heart pumps blood throughout the body."}
]


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    session.clear()

    categories = sorted(set(q["category"] for q in questions))

    return render_template(
        "index.html",
        categories=categories
    )


# ==============================
# START QUIZ
# ==============================

@app.route("/start", methods=["POST"])
def start():

    name = request.form.get("student_name", "").strip()
    category = request.form.get("category", "")

    if not name:
        return redirect(url_for("home"))

    if category not in {q["category"] for q in questions}:
        return redirect(url_for("home"))

    selected_questions = [
        q for q in questions
        if q["category"] == category
    ]

    session["student_name"] = name
    session["category"] = category
    session["questions"] = selected_questions
    session["start_time"] = time.time()

    return render_template(
        "index.html",
        quiz_questions=selected_questions,
        student_name=name,
        category=category,
        quiz_started=True
    )


# ==============================
# SUBMIT QUIZ
# ==============================

@app.route("/submit", methods=["POST"])
def submit():

    quiz_questions = session.get("questions")

    if not quiz_questions:
        return redirect(url_for("home"))

    elapsed = time.time() - session.get(
        "start_time", time.time()
    )

    time_up = elapsed >= 60

    score = 0
    results = []

    for i, question in enumerate(quiz_questions):

        selected_answer = request.form.get(f"q{i}", "")

        if selected_answer not in question["options"] or time_up:
            selected_answer = ""

        is_correct = selected_answer == question["answer"]

        if is_correct:
            score += 1

        results.append({
            "question": question["question"],
            "selected": selected_answer or "Not answered",
            "answer": question["answer"],
            "correct": is_correct,
            "explanation": question["explanation"]
        })

    total = len(quiz_questions)

    percentage = (score / total) * 100

    status = "PASS" if percentage >= 50 else "FAIL"

    student_name = session.get("student_name", "Student")
    category = session.get("category", "")

    session.clear()

    return render_template(
        "result.html",
        student_name=student_name,
        category=category,
        score=score,
        total=total,
        percentage=percentage,
        status=status,
        results=results,
        time_up=time_up
    )


# ==============================
# RUN FLASK APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)