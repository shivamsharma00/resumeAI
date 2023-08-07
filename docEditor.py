from docx import Document
# from docx import Inches
import re
import os
from python_docx_replace import docx_replace
import docxedit

# class init function will call function to separate strings 
# and run function will call function to replace strings
# and than it will make folder to save new resume.
# Error - while reading the resume file, it is not reading the whole professional experience


class DocEditor:


    def __init__(self, resume_path, updatedResume):

        self.document = Document(resume_path)
        self.new_resume = updatedResume
        self.table = self.document.tables[0]
        self.professional_experience = ""
        self.programming_skills = ""
        self.data_frameworks = ""
        self.application_software = ""
        self.tools_and_libraries = ""
        self.main_folder = "curated_resume"

        # checks if folder for curated resume exists, if not then create it.
        self.check_curaetd_resume_folder(self.main_folder)
        # separate text from the string to be used in the resume.
        try:
            self.separate_text()
        except:
            print("Error in separating text from the string to be used in the resume.")

    def check_curaetd_resume_folder(self, folder_path):
        # This checks if fodler for curated resume exists or not.
        if os.path.isdir(folder_path):
            pass
        else:
            os.mkdir(folder_path)

    def separate_text(self):
        # This function will separate the text from the string to be used in the resume.
        prof_exper = "PROFESSIONAL EXPERIENCE"
        skills = "Skills"
        academic_projects = "ACADEMIC PROJECTS"

        # separate indices
        # prof_exper_index = self.new_resume.find("-")
        skills_index = self.new_resume.index(skills)
        # academic_projects_index = self.new_resume.index(academic_projects)

        # get professional experience
        self.professional_experience = self.new_resume[121:skills_index].strip()
        # self.professional_experience = re.sub(r'', '', self.professional_experience, flags=re.MULTILINE)
        
        # get skills
        all_skills = self.new_resume[skills_index:].strip()
        all_skills_lower = all_skills.lower()

        # get programming skills indices
        programming_skills_index = all_skills_lower.index("programming languages") + len("programming languages") + 2
        data_frameworks_index = all_skills_lower.index("data frameworks") + len("data frameworks") + 2
        application_software_index = all_skills_lower.index("application software") + len("application software") + 2
        tools_and_libraries_index = all_skills_lower.index("tools and libraries") + len("tools and libraries") + 2
        
        # get programming skills
        self.programming_skills = all_skills[programming_skills_index:data_frameworks_index].strip()
        self.data_frameworks = all_skills[data_frameworks_index:application_software_index].strip()
        self.application_software = all_skills[application_software_index:tools_and_libraries_index].strip()
        self.tools_and_libraries = all_skills[tools_and_libraries_index:].strip()

        print("Professional Experiencw - ", self.professional_experience)
        
    def edit_work_experience(self, data):
        # This function edits the work experience section of the resume.
        paragraph = self.table.cell(2, 0).paragraphs[0]
        run = paragraph.add_run()
        run.text = data
        # self.document.save("curated_resume/ShivamSharmaCV_ml_new.docx")
    
    def edit_skills_section(self, programming_skills, data_frameworks, application_software, tools_and_libraries):
        # This function edits the skills section of the resume.
        pass
    
    def run(self, company_name):
        # This function will run the whole process of editing the resume.
        # edit work experience section of the resume.
        try:
            self.edit_work_experience(self.professional_experience)
        except:
            print("Error in editing work experience section of the resume.")
        
        # edit skills section of the resume.
        try:
            self.edit_skills_section(self.programming_skills, self.data_frameworks, self.application_software, self.tools_and_libraries)
        except:
            print("Error in editing skills section of the resume.")
        
        self.check_curaetd_resume_folder(os.path.join(self.main_folder, company_name))
        self.document.save(os.path.join(self.main_folder, company_name, "ShivamSharmaCV.docx"))


def edit_resume(data):
    document = Document("resume/ShivamSharmaCV_ml.docx")
    paragraph = document.paragraphs[0]
    table = document.tables[0]
    print(paragraph.text)
    print(table.cell(2, 0).text)


if __name__ == '__main__':
    resume_path = "resume/ShivamSharmaCV.docx"
    updatedResume = ""

    resume = """Professional Experience:

ActiveIQ Pvt. Ltd., Bangalore, IN Sep 2019 – Aug 2021
Data Engineer/ Machine Learning Engineer
• Collaborated with data team to design, build, and maintain data pipelines and data infrastructure using AWS, enhancing the efficiency of data processes and system performance.
• Developed ETL processes for transformation and loading of data from various sources into relational databases such as PostgreSQL and MongoDB.
• Established and maintained data models and database schemas, improving data structure and accessibility for machine learning applications.
• Performed comprehensive data analysis with Python and provided key insights to stakeholders, resulting in informed decision-making and strategic business moves.
• Ensured high data quality by implementing robust data validation and cleaning processes, minimizing data errors and inconsistencies.
• Worked proficiently with cross-functional teams to understand data requirements and delivered data solutions that met specific business needs, improving overall project efficiency and outcomes.

Skills:

Programming languages: SQL, Python, Java, C, C++, Shell Scripting, MATLAB, OOP 

Data frameworks: Apache Spark, TensorFlow, Pytorch, Keras, scikit-learn, PyCharm, GAN, CNN, ANN, Relational DBMS, MongoDB, XGBoost

Database Software: PostgreSQL, MySQL

Application Software: AWS, GCP, Azure ML, Git, CI/CD, Power BI, Jupyter Notebook, IBM Watson

Tools and Libraries: Apache Kafka, OpenCV, Tableau, NumPy, Pandas, SciPy, OpenGL, Matplotlib, Plotly, REST, Flask, Selenium, Docker, Kubernetes, CUDA, Linux"""

    doc = DocEditor(resume_path, resume)
    doc.run("ActiveIQ")
