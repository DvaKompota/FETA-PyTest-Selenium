# Pytest Front-end Test Automation Framework prototype 
<br/>

## Installation and running instructions:
#### 1. To install the framework on your local machine:
- clone the repo from GitHub to your local machine
- run setup.sh file in your local repo directory:<br/>
`./setup.sh`<br/>
#### 2. To run tests
- to run all the tests in the repo run test.sh file:<br/>
`./test.sh`
- to run only tests for a specific feature add a test mark to the run command, e.g.:<br/>
`./test.sh home_page`
- by default tests are running in headless browser mode; if you want to actually see the browser window, open `resources/test_data/data.yaml` file and change `web_driver_settings.headless` to `False`<br/>
<br/>

---
## Things to be added:
#### 1. Makefile to ease up the setup process within a pyenv
#### 2. Jenkins file to use this test automation from a server
#### 3. Proper docstrings, in-line comments, and configuration documentation to provide easier transition for further development
