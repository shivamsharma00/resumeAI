# resumeAI
# AI-Assistant for Resume Making

Hey there! Just got a new job application that you need to build a resume for? I've got you covered with a quick and simple AI assistant for resume making.

Here's how it works:

![resume/img.png](placeholder_for_image)

We'll be working with a predefined format of a resume and then employ chatGPT-4 for generating the job description and the key skills. Once everything is done, the updated resume will be saved as a pdf - neat, right?

## Let's dive deeper

The tool is essentially a Python script revolving around three libraries - `docx` for reading and writing Microsoft Word documents, `os` for file and directory operations and `docx2pdf` for converting your new resume from `.docx` to `.pdf`. 

The action happens inside a class named `DocEditor`, which constitutes of several methods for editing and saving your resume.

```python
if __name__ == '__main__':
    resume = """Shivam Sharma"""
    doc = DocEditor(resume)
    doc.run("Acti")
```

We kick the code off by initializing our `DocEditor` with a `resume`. The `run()` method calls other functions for check the resume directory, separate the text in resume, edit the work experience, and then modify the skills section.

If it faces any hiccups along the way, you'll be notified by an error message indicating the part of the process that failed.

## How it operates

Our AI assistant uses a predefined template of a resume in the format `resume/ShivamSharmaCV.docx`. It works its magic by first creating a new directory to store the edited resumes (if it doesn't already exist). Then, it neatly splits your experiences and skills from the text string using the `separate_text()` method.

The `edit_work_experience()` method slots in your work experience history into the template, while the `edit_skills_section()` replaces the skills segment with your updated proficiencies.

Finally, the `run()` method ties everything together, executing each function diligently, saving the document and converting it into a pdf.

And voila! Your comprehensive and professional resume is ready for action!

Give this AI-assistant a whirl and say goodbye to exhausting resume edits for each job application!
