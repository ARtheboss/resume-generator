# Resume Generator
Use this project to write, create, generate, and manage an unlimited number of versions of your resume with Python (please Fork if you want to use).

## Key Features
 - Resume generation code that creates better-formatted resumes than you could do by hand
 - Comes with preset formatting options and configurations but is fully customizable
 - Resume configs can derive from another config, so changes to one can reflect across all
 - In-built support for easily rewording the bullet points for each of your experiences
 - **Generate as many different variations as you want by running one Python script**

## How to start generating
 1. Fork this repo.
 2. Run `pip install -r requirements.txt` (only need to install FPDF2)
 3. Fill in your base details in `config.py`. Instructions are included in the file.
 4. Use helper functions from `config_helpers.py` to create variations.
 5. Add a destination folder to `generate_variations.py` and run it with `python generate_variations.py`
 6. That's it! Your generated resumes will start appearing in the output folder.

## Additional Customization
### `myfpdf.py`
`myfpdf.py` contains the code for generating the individual blocks of the resume. It creates the `MyFPDF` class which adds functionality to `FPDF`.
### `main.py`
`main.py` uses functions from the `MyFPDF` class to put the resume together based on a given config. Feel free to edit this to put together a resume in a format you like better. For example, you may like putting your SKILLS section at the bottom.
