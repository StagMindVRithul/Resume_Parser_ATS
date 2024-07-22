# Resume Parser and ATS using GEMINI API KEY 

## Prerequisites

* VS Code
* GEMINI API KEY

## Overview of the Project

1. **The initial interface of the Resume Parser and ATS application, showing fields to input a job description and upload a resume in PDF format.**
![Screenshot 2024-07-16 at 10 11 27 PM](https://github.com/user-attachments/assets/066afbb7-503d-4ee6-b50d-3cfa0577e88d)

2. **The Resume Parser and ATS application with a job description entered and a resume successfully uploaded.**
![Screenshot 2024-07-16 at 10 12 54 PM](https://github.com/user-attachments/assets/316fc8fa-53f2-4232-b81e-a39a26d042ac)

3. **The Resume Parser and ATS application displaying an analysis of the uploaded resume in response to the job description.**
![Screenshot 2024-07-16 at 10 14 35 PM](https://github.com/user-attachments/assets/28a3ddda-bca2-498b-8ca2-59898eb77fbf)

4. **The Resume Parser and ATS application displaying Job Matching Percentage along with the Keywords Missing.**
![Screenshot 2024-07-16 at 10 14 56 PM](https://github.com/user-attachments/assets/87610a2e-2342-415a-971c-30d8da8607a0)

5. **Finally the Resume Parser and ATS application displaying the major data extracted from the resume for HRMS purpose.**
![Screenshot 2024-07-16 at 10 16 20 PM](https://github.com/user-attachments/assets/e348ab83-08b8-4684-9acb-6c60e3533cd0)
![Screenshot 2024-07-16 at 10 37 57 PM](https://github.com/user-attachments/assets/6c86ea08-09ca-4008-892b-e1501ae934d8)
(with confidential information scribbled over).

## Setup

1. **Create a virtual environment**

Open the terminal in VS Code and run:
```
conda create -p venv python==3.10 -y
  ```
2. **Activate the virtual environment**

    After the environment is created, activate it by running:
    ```
    conda activate venv/
    ```

3. **Install dependencies**

    Make sure you have a `requirements.txt` file with all necessary dependencies listed. Then run:
    ```
    pip install -r requirements.txt
    ```

4. **Install poppler for `pdf2image`**

    The `pdf2image` library requires an additional dependency called `poppler`. Download it from [here](http://blog.alivate.com.au/poppler-windows/) and add it to your system PATH.

5. **Set up your GEMINI API key**

    Create a `.env` file in the root directory of your project and add your GEMINI API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key
    ```

### Running the Program

To run the application, use the following command:
```
streamlit run app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact the project maintainers at vrithul9@gmail.com
