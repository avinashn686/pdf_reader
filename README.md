# pdf_reader
Requirements:
------------------
    Python 3.8.2
    Virtual Enviornment
    python pdfplumber


Steps:
-------------
    1) Install Python3
        sudo apt-get install python3

    2) create an Virtual Environment
        sudo apt-get install python3-venv
        python3 -m venv environmentName

    3) Install all the requirements in the environment
        pip3 install -r requirements.txt

    4) Run the pdf_reader.py
        python3 pdf_reader.py pdf_name.pdf output_fliename.json

    5) Inputs are:
        input_file_name.pdf output_file_name.json


Example:
----------------

    RUN : python3 pdf_reader.py Interview_sample_data.pdf output_fliename.json


    OUTPUT:
    
        {
            "name": "Burk Lee",
            "address": "(XXX) XXX-XXX,City, State Zip Code",
            "email": "burk.lee@gmail.com",
            "Education": "University of California, Berkeley May 2023 Intended: Bachelor of Arts in Psychology GPA: 3.7 Balboa High School, San Francisco June 2019 High School Diploma Relevant Coursework: data analysis, child development and adolescence, public services, administration, ​ program development, research methods",
            "Leadership Experience": "ASUC Student Union Event Services – Berkeley, CA August 2019-Present Event Planning Assistant ● Assist with the quality of services for students and staff at UC Berkeley campus. ● Organize and prepare the materials and equipment needed for events serving over 100+ guests. ● Maintain a positive guest experience by ensuring all event requests were met in a timely manner. Barany Consulting- Berkeley, CA December 2019-January 2020 Externship ● Explored work environments aligned to personal career and educational goals in social services by participating in training, presentations, and workshops to enhance communication skills. ● Assisted staff to complete administrative projects: emails, phone transfers, printing, scanning. ● Connected with alumni to explore opportunities for personal and professional growth within the consulting industry.",
            "Professional Experience": "Target- San Francisco, CA May 2018- June 2019 Sales Associate ● Monitored inventory and restocked items as requested by store manager and team. ● Provided memorable customer service by assisting with merchandise to meet demands of company. ● Multitasked in a face pace environment to produce high volume of sales to meet weekly benchmarks. ● Operated computerized cash register and processed membership accounts.",
            "Additional Projects": "Child Development Research June 2018 ● Collected data from online reports to analyze the findings to present a 15-page research paper. ● Interviewed with students on campus to record over 50 responses to gain insight of their perceptions on the developmental stages of children. ● Presented a 10-minute presentation while facilitating a Q&A panel regarding research results.",
            "Skills & Interests": "Technical: Proficient with Microsoft Suite, Adobe Photoshop and Illustrator, Google Platforms ​ Language: Basic Tagalog (written and verbal) ​ Interests: Community Service with over 100+ volunteer hours, traveler to over 5 countries in Asia."
        }
