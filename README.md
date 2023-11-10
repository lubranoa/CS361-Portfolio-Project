<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="www.linkedin.com/in/lubrano-alexander">
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
  <h1 align="center">Password Generator App</h1>
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
  - [Skills Applied](#skills-applied)
  - [Acknowledgments](#acknowledgements)

</details>

<!-- Project Description -->
## Project Description

Password Generator is a Python desktop application for users to generate passwords and test password strength. It is the culmination of a term-long group project using Agile methodologies to design and develop an application implemented using a microservices architecture. Each person on the team had to create their own individual project as well as a microservice for one or more of the team's applications. The microservices were implemented as socket server applications, which meant that our main projects were their clients. Project development was organized into sprints, covering tasks such as defining requirements, designing UI, team collaboration, minimum viable products, service integration, and evaluation and revision.

<!-- Technologies Used -->
## Technologies Used

  - [![Python][Python]][Python-url]
  - [![pyside6][pyside6]][pyside6-url]
  - [![qt-style][qt-style]][qt-style-url]
  - [![socket][socket]][socket-url]

<!-- Features -->
## Features

Password Generator offers an array of features for a user to interact with.
  - **Custom Password Generation**: Allows a user to generate a custom random-character password with customization options like length and the characters that will be used in generation.
  - **Passphrase Generation with Options**: Provides a way for users to generate passphrases, a string of random words, with options like number of words and a separator character for adding or removing complexity.
  - **Strength Testing**: Provides password strength estimation for users to test any password or passphrase for a strength score and an estimated time to crack.
  - **Clean and Simple GUI**: The application's user interface is uncomplicated and easy to use and understand so that any user can understand the application.
  - **Informational Tooltips**: Tooltips throughout the application guide users on the use of the application as well as how making certain selections can impact passwords.
  - **Microservice Architecture**: TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage

This project was designed to use two of my teammates' microservices that I no longer have access to so this project will not run unless I get access to them again or write them myself. The following is how the program could be used when everything was all together.

  - Main Program Window
    - A simple and intuitive GUI that gives the user plenty of useful information on program use without the need for a tutorial. The app's GUI is broken into four logical sections, Generate Password, Generate Passphrase, Password Output, and Test Password Strength. Each of those sections allow a user to do exactly as they are titled.
      ![Screenshot of Password Generator's graphical user interface that includes the sections, Generate Password, Generate Passphrase, Password Output, and Test Password Strength](/img/361-app-window.png)
  
  - Password Generation
    - Before generating a password, choose a length, make character inclusion selections, and optionally add advanced options, then click on generate password to get a password. Hover over tooltips and options to get more information.
      ![Screenshot of the Generate Password and Password Output sections that shows which options were selected under Generate Password and the generated password in the Password Output section](/img/361-password-gen.png)

  - Passphrase Generation
    - TODO

  - Password Output
    - TODO

  - Testing Password Strength
    - TODO

  - Tooltips on Hover
    - TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Project Link: [https://github.com/lubranoa/<repo-name>][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Acknowledgements -->
## Acknowledgments

  - [Shields.io][shields-url]
  - [Simple Icons][icons-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[Python-url]: https://www.python.org/

[pyside6]: https://img.shields.io/badge/PySide6_(Qt_for_Python)-grey?style=for-the-badge&logo=qt
[pyside6-url]: https://pypi.org/project/PySide6/

[qt-style]: https://img.shields.io/badge/Qt_Style_Sheets-grey?style=for-the-badge&logo=qt
[qt-style-url]: https://doc.qt.io/qt-6/stylesheet.html

[socket]: https://img.shields.io/badge/Python_sockets-grey?style=for-the-badge&logo=python&logoColor=ffd343
[socket-url]: https://docs.python.org/3/library/socket.html

[shields-url]: https://shields.io/
[icons-url]: https://simpleicons.org/

[email]: mailto:lubrano.alexander@gmail.com
[linkedin-url]: www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/