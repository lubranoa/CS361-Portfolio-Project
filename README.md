<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="https://www.linkedin.com/in/lubrano-alexander">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin" alt="linkedin link" />
    </a>
    <a href="https://lubranoa.github.io">
      <img src="https://img.shields.io/badge/Personal_Site-47b51b?style=for-the-badge" alt="personal website link" />
    </a>
    <a href="https://github.com/lubranoa">
      <img src="https://img.shields.io/badge/GitHub-8A2BE2?style=for-the-badge&logo=github" alt="github profile link" />
    </a>
  </p>
  <br />
  <!-- Titles and Subtitles -->
  <h1 align="center">Microservices-Based Password Generator and Strength Tester</h1>
  <p align="center">
    <b>A PySide6 (Qt for Python) Desktop Application Using Microservices to Generate Passwords and Test their Strength</b>
  </p>
  <p align="center">
    Winter 2022 · <a href="https://ecampus.oregonstate.edu/soc/ecatalog/ecoursedetail.htm?subject=CS&coursenumber=361&termcode=ALL">CS 361 Software Engineering I</a> · Oregon State University
  </p>
  <br />
</div>

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
    
  - [Project Description](#project-description)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Usage](#usage)
    - [Main Program Window](#main-program-window)
    - [Password Generation](#password-generation)
    - [Passphrase Generation](#passphrase-generation)
    - [Password Output](#password-output)
    - [Testing Password Strength](#testing-password-strength)
  - [Skills Applied](#skills-applied)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

</details>

<!-- Project Description -->
## Project Description

Password Generator is a Python desktop application designed for generating customizable passwords and testing their strength. Developed as part of a term-long group project, this application employs a microservices architecture and Agile methodologies to ensure scalability and flexibility.

Each team member developed an individual project and contributed a microservice for one or more teammates’ applications. The microservices were implemented as socket server applications, making the main projects their clients.

The development process was organized into sprints, covering tasks such as defining requirements, designing the user interface, and integrating microservices. Additional activities included implementing a minimum viable product (MVP), evaluating and refactoring code, and ensuring successful service integration. The team utilized task management systems like Trello and Asana as scrum boards to manage sprints, spikes, and user stories.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Technologies Used -->
## Technologies Used

  - [![Python][Python]][Python-url]
  - [![pyside6][pyside6]][pyside6-url]
  - [![socket][socket]][socket-url]
  - [![asana][asana]][asana-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Features -->
## Features

  - Provides customizable random-character password generation.

  - Provides customizable random-word passphrase generation.

  - Implements password strength assessment with time-to-crack estimations.

  - Offers a user-friendly interface with informational tooltips.

  - Integrates microservice architecture using Python sockets.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage

This project was designed to use two of my teammates' microservices that I no longer have access to so this project will not run unless I get access to them again or write them myself. The following is how the program could be used when everything was all together.

### Main Program Window

  1. **Overview:** The application features a clean, intuitive GUI, designed to provide a seamless user experience without requiring a tutorial.

<p align="center">
  <img src="./img/361-app-window.png" alt="Screenshot of Password Generator's graphical user interface that includes the sections, Generate Password, Generate Passphrase, Password Output, and Test Password Strength" width="600px"></img>
</p>

  2. **Layout:** The GUI is divided into four logical sections:

     - **Generate Password**
     - **Generate Passphrase**
     - **Password Output**
     - **Test Password Strength**

  3. **User Guidance:** Tooltips are available throughout the interface to help users understand how to utilize various options and features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Password Generation

  1. **Select Password Length:** Choose the desired length of the password using the slider.

  2. **Character Options:** Check boxes to include or exclude:
     - **Uppercase Letters**
     - **Lowercase Letters**
     - **Numbers**
     - **Special Characters**

  3. **Advanced Options:** Optionally, refine your password generation settings by:
     - Excluding similar characters (e.g., 'i' and 'l')
     - Avoiding ambiguous characters (e.g., '{}[]()/\')
     - Setting a minimum number of digits
     - Setting a minimum number of special characters

  4. **Generate Password:** Click **Generate Password** to create your custom password.

  5. **View Results:** The generated password will appear in the **Password Output** section.

  Password Options           | Generated Password
  :-------------------------:|:-------------------------:
  ![Screenshot of the Generate Password section that shows which options were selected under Generate Password](/img/361-password-opts.png)   |  ![Screenshot of the Password Output section that shows a generated password](/img/361-password-gen-2.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Passphrase Generation

  1. **Select Word Count:** Specify the number of words in the passphrase.

  2. **Customize Separators and Formatting:**
     - Choose a character to separate words.
     - Add optional formatting, such as:
       - Numbers appended to words.
       - Capitalization of words.

  3. **Generate Passphrase:** Click **Generate Passphrase** to create your custom passphrase.

  4. **View Results:** The passphrase will be displayed in the **Password Output** section.

  Passphrase Options         | Generated Passphrase
  :-------------------------:|:-------------------------:
  ![Screenshot of the Generate Passphrase section that shows which options were selected under Generate Passphrase](/img/361-phrase-opts-2.png)   |  ![Screenshot of the Password Output section that shows a generated passphrase](/img/361-phrase-gen.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Password Output

  1. **Display Area:** All generated passwords or passphrases appear here.

  2. **Immutable Output:** The displayed password cannot be edited directly to ensure its integrity.

  3. **Available Actions:**
     - **Copy:** Highlight and copy the password manually or use the **Copy** button for accuracy.
     - **Test:** Use the **Calculate Strength** button to send the password to the **Test Password Strength** section.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Testing Password Strength

  1. **Input Password:** Enter a password or passphrase in the input box.

  2. **Calculate Strength:** Click **Calculate Strength** to analyze the password.

  3. **Results:** The application provides:
     - A strength score on a scale from 0 (too guessable) to 4 (very unguessable).
     - The estimated time required to crack the password.

  Strength of Passphrase     | Strength of Easy Password
  :-------------------------:|:-------------------------:
  ![Screenshot of the Test Password Strength section that lets a user input a password to see its strength score and estimated time to crack](/img/361-phrase-test.png)   |  ![Screenshot of the Password Output section that shows a generated passphrase](/img/361-password-test-2.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

  - Python programming with sockets and custom QWidget classes

  - Microservices architecture design and implementation

  - GUI implementation using PySide6 (Qt for Python)

  - Using Agile methods to implement steps of the SDLC

  - Application design via defining requirements and creating user stories

  - Class modeling using Unified Modeling Language and Sequence Diagrams

  - UI/UX Design via paper prototyping and cognitive style heuristics

  - Collaborative teamwork in a software engineering project

  - Code evaluation and refactoring

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Project Link: [https://github.com/lubranoa/CS361-Portfolio-Project][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Acknowledgments -->
## Acknowledgments

  - [Qt for Python (PySide6) Documentation][pyside6-url]
  - [zxcvbn Password Strength Estimator by Dropbox][zxcvbn-url]
  - [Asana Task Management System][asana-url]
  - [Shields.io][shields-url]
  - [Simple Icons][icons-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[Python-url]: https://www.python.org/

[pyside6]: https://img.shields.io/badge/PySide6_(Qt_for_Python)-grey?style=for-the-badge&logo=qt
[pyside6-url]: https://doc.qt.io/qtforpython-6/index.html

[socket]: https://img.shields.io/badge/Python_sockets-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[socket-url]: https://docs.python.org/3/library/socket.html

[asana]: https://img.shields.io/badge/Asana_TSM-grey?style=for-the-badge&logo=asana
[asana-url]: https://asana.com/

[trello-url]: https://trello.com/
[zxcvbn-url]: https://github.com/dropbox/zxcvbn
[shields-url]: https://shields.io/
[icons-url]: https://simpleicons.org/

[email]: mailto:lubrano.alexander@gmail.com
[linkedin-url]: https://www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/CS361-Portfolio-Project