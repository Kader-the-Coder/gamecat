<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/Kader-the-Coder/gamecat">
    <img src="static/images/favicon.ico" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">GAMECAT</h3>
  <p align="center">
    Tracks clicks
  </p>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About The Project
<span style="display:block;text-align:center">![screenshot1]</span>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

This is a Django webapp that currently has the following features:
- Registering a new user
- Logging in with an existing user account
- Clicking a button

The app tracks the number of times the button was clicked and displays some statisitcs regarding the clicking of the button (Example: Who clicked the button last).

## Getting Started

In order to make use of this project, follow the steps below:

### Prerquisites
  - python
  - pip
### Installation

#### Running on <a href="https://labs.play-with-docker.com" target="_blank">Docker Playground<a>
  - Click start
  - Click Create new instance
  - Run the comman:
     ```sh
     docker run -it -p 8080:8000 kaderthecoder/gamecat
     ```
#### Building the project locally
  - Clone the repository
  - Create a virtual enviroment
    - Install django
      ```sh
      pip install django
      ```
    - Install sphinx
      ```sh
      pip install -U sphinx
      ```
    - Install a sphinx theme (optional)
       ```sh
      pip install sphinx-rtd-theme
       ```
    - Install requirements:
       ```sh
      pip install -r requirements.txt
       ```
       ```sh
      python -m pip freeze -l
       ```
    - To run the app locally, exectue the manage.py file in the local directory
      ```sh
      python manage.py runserver
      ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

This app can be used to exercise your index finger by clicking the button a lot of times...

###


## License

None
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[screenshot1]: static/images/screenshot1.png
[screenshot2]: static/images/screenshot2.png
[screenshot3]: static/images/screenshot3.png
[screenshot4]: static/images/screenshot4.png
[screenshot5]: static/images/screenshot5.png
