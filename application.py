import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MARY HEAVEN J - Data Analyst Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }

        h1 {
            font-size: 28px;
        }

        h2 {
            font-size: 24px;
            margin-top: 10px;
        }

        h3 {
            font-size: 20px;
            margin-top: 10px;
        }

        p {
            margin: 5px 0;
        }

        .contact {
            margin-top: 20px;
        }

        .education, .projects, .languages, .interests {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1>MARY HEAVEN J   -  Data Analyst</h1>
  
    <p>Driven and adaptable Data Analyst with a passion for continuous learning and leadership. Skilled in mathematics, statistics, and programming, I excel at solving complex problems and extracting valuable insights from data. Committed to staying updated on industry trends to deliver impactful data-driven solutions.</p>
    
    <div class="contact">
        <h2>Contact Information</h2>
        <p>Email: maryheaven0103@gmail.com</p>
        <p>Phone: 6383206095</p>
        <p>Location: Thangachimadam, India</p>
        <p>LinkedIn: <a href="https://www.https://www.linkedin.com/in/mary-heaven-j-20096a228/">https://www.linkedin.com/in/mary-heaven-j-20096a228/</a></p>
        <p>GitHub: <a href="https://https://github.com/MaryHeaven-J">https://github.com/MaryHeaven-J</a></p>
    </div>

    <div class="education">
        <h2>Education</h2>
        <h3>B.Sc. Computer Science</h3>
        <p>Nirmala College for Women</p>
        <p>06/2019 - 04/2022, Coimbatore</p>
        <p>Graduate with a first-class degree.</p>

        <h3>M.Sc. Data Science</h3>
        <p>Loyola College</p>
        <p>06/2022 - Present, Chennai</p>
        <p>Pursuing degree in data Science with a commendable CGPA.</p>
    </div>

    <div class="projects">
        <h2>Projects</h2>
       <p>Road Accident Analysis through Power BI</p>
        <p>PCOS CLASSIFICATION USING MACHINE LEARNING
ALGORITHM</p>
        <p>INSURANCE CLAIM FRAUD DETECTION USING
MULTIPLE CLASSIFICATION MODELS</p>
    </div>

    <div class="languages">
        <h2>Languages</h2>
        <p>Tamil - Native or Bilingual Proficiency</p>
        <p>English - Full Professional Proficiency</p>
    </div>

    <div class="interests">
        <h2>Interests</h2>
        <p>Data Analysis</p>
        <p>Predictive Modelling</p>
        <p>Natural Language Processing</p>
        <p>Data Visualization</p>
    </div>
</body>
</html>
"""


def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
