snap firefox creating the problem. To fix, refer below link when free to run in mozilla:
https://support.mozilla.org/en-US/kb/install-firefox-linux#w_install-firefox-from-mozilla-builds-for-advanced-v'

***********************************************************************************************************************

To print values using reference or %. example print("this is %s. my age is %d" %(a, b)). where a=janani and b=32

to print last value of the list:
mylist = [1,2,3, "h", 8, 2.5]
print(mylist)
print("last value of mylist is", mylist[-1])

list deletion is done when the index of a list element (del list[0]) is known. If  index is not known and only value is known, remove function is used.

continue keyword in while loop is used to stop current iteration and proceed with next iteration.

In class, self keyword is mandatory while calling or using variables into methods.
For class variables, either self or class name (self.classvariablename or classname.classvariablename) can be used. But for instant variables assigned under constructor, should be used under method as self.instantvariablename.
Inheriting parent's class: 
from "filename.py" import "parentclassname"
pass parentclassname as argument while creating child class. class childclassname (parent'scalssname)
now you can see all the parent class variables and method autosuggested.
if there are any run time arguments (i.e) parameter passed while creating object in parent's class, then, parent class isn't having default constructor, whereas it has valid declarations like self.parameter = parameter. In such case, child constructor needs to invoke parent's constructor. syntax: parentclassname.__init(auto suggested)

reverse vs reversed

reverse will directly reverse the list or content. It will not return anything.
eg: list1 = [1, 2, 3]
    list1.reverse()
    print(list1)
    
reversed() will reverse the content and it is used to iterate. VALUES CAN BE PRINTED THROUGH ITERATION ONLY.

list1 = [1, 2, 3]
mylist = reversed(list1)
for chumma in mylist:
    print(chumma)
    
another option without for loop could be:
list1 = [1, 2, 3]
print(list(reversed(list1)))
-------------------------------------------------
exception:

When you want to validate an output of a test case, exception is used.
for eg: if the dropdown selected should be hyderabad. Output of the test case is hyderabad.
If the output is chennai, then test case should be failed with an error message.

dropdownvalue = "hyderabad"

if dropdownvalue != "hyderabad":
    raise Exception("incorrect dropdownvalue")
	
difference between try catch(or exception - in python instead of catch you call it as exception) and exception.

if you want to fail the test case but it will not actually fail, raise Exception (refer above)
But if system gonna throw error, still you want to continue the execution, do, try and except method. 
In this try and except method, even if it fails, except block will catch the failure and send the customized message we ask to print.

if it not fails, control will remain in try block and codes in try block will be executed.

Invoke browser:

Service object is a class which has the capability to invoke browser hence it is imported

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com")
----------------------------------------------------------
Locators: find_element(s)_by_:

id
name
xpath
css
classname
linkText
Partiallinktext
tag name

CSS:
----------------------------------------------------------------
tagname[attribute="value"] or [attribute="value"] or #ID or .classname
eg: input[name="valuename"
in console:
$("tagname[attribute="value"])



            Your provided Email 123@123.com has already been used. Please use another Email address.
          

xpath:
----------------------------------------------------------------------
//tagname[@attribute="value"]

in console: $x("//tagname[@attribute="value"]")

$x("//div[@id='auth-error-message-box']")

$x("//li[contains(@id,'p_n_feature_nineteen_browse-bin/')]")

<a class="product-item-link" href="https://www.ulamart.com/sugar-salt/raw-natural-seasalt-non-iodised">
 
$x("//a[@href="https://www.ulamart.com/sugar-salt/raw-natural-seasalt-non-iodised"]")                                                                                                                                                                                                  

if there is only text in html, webelement can be identified using text as below:

//span[contains(text(),'Sign up')] or //tagname[text() = "text"]

if multiple class names present in html for a single web element, pick one class name and write in regular expression(RegEx) as below:

css:
tagname[class*='anyone classname']

xpath:
//tagname[contains(@attribute, 'value')]

traversing through tags if no proper attribute is present:

xpath: parent xpath/child tag
css: parent xpath child tag

plain traverse with only grand parents present:
xpath: grandparent xpath/parent tagname[1](based on which number of element)/child tagname
css: grandparent xpath/parent tagname:nth-child(1)(based on which number of element)/child tagname


traversing from child to parent:

childxpath/parent::parenttagname/parent::parenttagname.....until the required parent tag is arrived.


traversing to sibling:

syntax:
childxpath/following-sibling::siblingtagnname


addToCart = webdriverObj.find_elements(By.XPATH, '//a[@href="javascript:void(0)"]')
for eachAddToCart in addToCart:
    print(eachAddToCart.find_element(By.XPATH, "parent::div/parent::figcaption/parent::div/parent::div/following-sibling::div/strong/a").text)
    eachAddToCart.click()


----------------------------------
To display all the options in a dropdown if the drop down has select tag this is more advantageous as select object is already created and can be used multiple times. in the "other case" mentioned below, one more object is created exclusively

categories = Select(webdriverObj.find_element(By.ID, 'searchDropdownBox'))
for values in categories.options:
    print(values.text)
    
if there is no select tag:

other case:

mylist = webdriverObj.find_elements(By.ID, 'searchDropdownBox')
for values in mylist:
    print(values.text)
    
if a web element text couldn't be identified by selenium usin find_element(by id, "id").text,
then use below option:
find_element(By ID, "ID").get_attribute("value") where value is inbuilt in selenium, not from html. This is a DOM method inherited by selenium.

get_attribute is used get the values of an attribute in html tag.

for eg:
<tagname attribute='value'>

to extract the value, find_Element(By.ID, "ID").get_attribute("value")

this will retrieve the value from html in given eg.

This is used to extract title values, 
text etc from html.
----------------------------------
Waits:

Implicit wait
Explicit wait
Pause or sleep.

Implicit wait:
syntax: webdriverObj.implicitly_wait(4)

 Requesting the script or coding or webdriver to stop executing next code until the expected element is identified in given mention time (within implicit argument) eg: webdriver.implicitly_wait(5)
 
 if element is found before mentioned time say 2 secs, driver will continue execution instead of waiting for mentioned 5 secs.


explicit wait:

requesting a particular webelement alone to wait to get loaded until the time mentioned.
nth
syntax:

expWait = WebDriverWait(webdriverObj, 5)
expWait.until(expected_conditions.presence_of_element_located( (By.PARTIAL_LINK_TEXT, "shopping cart") ))



Note: webelement should be insided a tuple () to avoid getting below error:

"TypeError: presence_of_element_located() takes 1 positional argument but 2 were given"

also please note that only locator is passed not the webelement like webdriverObj.****.......as expWait variable already carries the webdriver knowledge.
----------------------------------------------------
SWITCH_TO:

To switch between windows:

webdriverObj.switch_to.window(webdriverObj.window_handles[0])

where 0 is parent window and 1 is child window or second window and goes on....


switch to frames:

frames are tagged in HTML as, 

iframe
frameset
frame

If any parent tag has one of the above options, then, driver cannot find that webelement. You should switch to frames to access it.

syntax:

webdriverObj.switch_to.frame("frameID or name or index")

To come back to html content from frames:

webdriverObj.switch_to.default_content()


switch to alerts:

myAlert = webdriverObj.switch_to.alerts()
myAlert.accept()
myAlert.dismiss()
myAlert.text()
myAlert.send_keys()


Mousehover:

.perform() is mandatory to do all the actions mentioned in a single line of code.

MouseHover = ActionChains(webdriverObj)
MouseHover.move_to_element(webdriverObj.find_element(By.ID, "nav-link-accountList")).perform()
MouseHover.move_to_element(webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Create")).click().perform()

context_click is right mouse click.

---------------------------------

isdisplayed():

webelement.isdiplayed()

element should be present in DOM/HTML but hidden only in the webpage. In this case, isdisplayed() can be used to verify if the element is hidden or not. otherwise this method cannot be used.

--------------
if expected output is false for a test case, then assertion should be like below:

assert not webelement.isdisplayed()

this will return true and test case will be passed.

-------------------------------------------------
Advantage of using java script executor is it will work directly in html code level so that, if any popups hiding a button/textbox to be accessed,
selenium will work only if the popup gets closed, but in javascript, without closing popup which is hiding only the front end, it will have direct access to hidden button/textbox

syntax:

driver.execute_script(javascript)

example:
print(webdriverObj.find_element(By.ID, "email").get_attribute("value"))  - js
print(webdriverObj.execute_script('return document.getElementById("email").value')) - js

shopButton = driver.find_element_by_css_selector("a[href*='shop']") - selenium
driver.execute_script("arguments[0].click();",shopButton) - js using seleium webelement

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") - js

----------------------------------------------------

ChromeOptions is used to setup chrome before launching like, headless, maximised, certificate errors ignored etc.

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--ignore-certificate-errors")
serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj, options=chromeOptions)

---------------------------------------------------------

PYTEST framework:

Pytest enables you to create marks, or custom labels, for any test you like. A test may have multiple labels, and you can use them for granular control over which tests to run.

both file name and method names should start with test_. Note: Method name is nothing but TEST CASE NAME.
to execute: pytest for summary or pytest -v -s for detailed output.

-s for detailed output
-v details about python
-k keyword of test case

--Execute test case using a common keyword among the selected test cases for eg: demo is the common name in two test cases which you want to execute. 
then,

pytest -k demo -v -s

--To execute one file alone,

eg:
file name is basics.py

pytest basics.py -v -s

--To tag or mark selected test cases for regression or smoke or any other purpose:

syntax:
@pytest.mark.smoke(or regression etc)
test case follows...

in terminal, execute above as: pytest -m smoke -v -s

--If a test case has known bug which should not be displayed in pytest report but it should run as that particular test case has pre-requisites
precisely, a test case should run though it fails, but it should not be reported. It will neither pass of fail the test case. It will just run.

syntax:

@pytest.mark.xfail

--If a pre-requisite test case (browser invocation) to be assigned to a normal test case, use fixtures. 
--yield is used to execute steps at last. eg: browser close or quit.

syntax:

@pytest.fixture()
def test_first_last():
    print("Browser invocation steps")
    yield
    print("browser closing steps")


def test_check(test_first_last):
    print("regular test cases")
    
--If fixtures are required in multiple files, above code can be written in a file name "conftest" and pass the method name as argument to avoid
redundancy.

NOTE: Both class and method name should start with test. VERY IMPORTANT.

eg:

python file:
import pytest


@pytest.mark.usefixtures("test_setup")
class TestExample:
    def test_demo1(self):
        print("hello")



conftest:
import pytest


@pytest.fixture(scope="class")
def test_setup():
    print("I will be executing first")
    yield
    print(" I will execute last")
    
--fixtures can also be used as data setup grid to give login details like name, email id as input.
To do this, the fixture method name should also be given as argument in calling method though it is present in class argument.
class level argumenting is a pre-requisite before running the test case. method level argumenting is to receive data from called method in conftest file. so, it is ok to only pass method argument if there is no prerequisites.

fixtures are overall used to:
1. apply pre and post requisites to a test case
2. to pass credentials and other values and it can be used as datagrid.
3. run a test case multiple times with different datasets

Note: conftest method names or any data supplying method names is not required to name as test_.
test that should only execute using pytest should be named as test_*.

syntax: 
 
    def test_login_details(self, test_data_setup): # here test_data_setup is the fixture method name. It is also parameterised in clasa level
        print(test_data_setup)
        
--Above theory can also be done in an alternate effective way. In this way, we can avoid parameterising the fixture method name with the help of ****request***: This is widely used because yield and return statment cannot get along together.

syntax:

conftest file:

pytest.fixture(scope="class")
def test_data_setup(request):
    login_details = ("janani", "dinesh", "darshini", "sanjeevkrish")
    request.cls.login = login_details
        
this can be called as:

@pytest.mark.usefixtures("test_data_setup")
class TestCheck:
    def test_demo(self):
        print("Sarvam Krishnarpanam")
        print(self.login[0])
        
output will be: janani.

Note: when you type, self. the next word login will not be auto populated. It has to be typed manually. Still, output will be successfully.
        

--multiple runs can be parameterised under fixture as follows:

@pytest.fixture(params=("chrome", "firefox"))
def test_browsers(request):
    return request.param
    
this can be called as below:

    def test_cross_browsers(self, test_browsers):
        print(test_browsers)
        
--to generate html report:

pytest --html=report.html

--To get screenshot,

driver.get_screeshot_as_file("filename.png")

filename will be created and saved in project path itself.
 


http://automationpractice.com/index.php


//ul[@class="product_list grid row"]/li[1]/div/div[2]

*********************************
To clear temp file:

sh temp.sh
df -h
clear

*********************************

Frameworks:

Consist of four main packages under a project:

Python Project:
-test (main execution)
-PageObjects (webelements)
-utilities (select, explicit wait and other simple commonly and repeatedly used steps can be generalised here with the help of arguments as locators, text etc.)

eg:
@pytest.mark.usefixtures("test_dawn_dusk")
class UseFixture:

    def select_option(self, locator, text):
        categories = Select(locator)
        categories.select_by_visible_text(text)
here, the above function select_option will be called by mainclass with two arguments passed. values of the arguments are from page object.

calling mainclass function:
self.select_option(amazonDropDownObj.drop_down(), "Amazon Devices")

-TestData:

to send data like, first name, lastname, password, etc.




input[name="customerName"]

----------------------------------------



If class A want to call a variable C in class B write below code in class A:

B.C

------------------------------------------
inspect.stacK

it is used to inspect the filename, 

import inspect
import sys


def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    print(fileName)
    print(line)
    print(method)
    # print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)

class Hello:

    raiseNotDefined()
    
    
--------------------------------------

criticial
error
warning
info
debug

set levevl from debug.

-------------------------------------

global:

If an object has to be used across multiple functions, use "global" keyword during object creation.

----------------------------------------

to avoid stalereference error:

It is popped up because the element driver trying to find is no longer attached to dom created earlier.
Hence, it the element became stale and it raised error.

To avoid this error, request driver to wait until the element presence is located. Once it is located, get the attribute value from dom.

eg:

myloc = (By.CSS_SELECTOR, "input[name='customerName']")
webdriverObj.find_element(By.CSS_SELECTOR, "input[name='customerName']").send_keys("janani")
print(webdriverObj.find_element(*myloc).get_attribute("value"))

now the element is popped up.

But after clicking, continue button in amazon account creation page, name field will become stale. To get the element again, use explicit wait.

expWait = WebDriverWait(webdriverObj, 10).until(expected_conditions.presence_of_element_located(myloc)).get_attribute("value")
print(expWait)


----------------------------------------------------------

automatic screenshot of failed test cases:


just copy the given code to conftest file and refer webdriver to global. Screenshot will be taken

--------------------------------------------------------------

jenkins installation:

follow the commands for configuration:

custom workspace provide main project directory path.
select "This project is parameterised", pass variable as"browsername" and give browser options like chrome, edge etc.
Select Build section, windows batch and give below commands.


cd PycharmProjects\PycharmProjects\pythonProject2\E2E_Framework
pytest --browser_name "%browsername%" --html=$WORKSPACE\PycharmProjects\PycharmProjects\pythonProject2\reports\report.html

Note %browsername% is the variable used in "This project is parameterised".
$WORKSPACE is used from custom workspace directory path.

----------------------------------------------------------------

EXCEL PYCHARM:

while writing data to excel, ensure the excel is not open. Also, at the end of writing code ensure the workbook save command is written.

eg: below are the multiple ways of writing to a cell.
import openpyxl

cellObj = wsObj.cell(row=5, column=5)
cellObj.value = "hello"
wsObj['F5'] = "hello"
print(wsObj['F5'].value)
cellObj = wsObj.cell(row=5, column=5, value="hello")
print(cellObj.value)
wbObj.save("C:\\Users\\dines\\OneDrive\\Documents\\MyPythonProject\\DataSetUp.xlsx")


------------------------------------------------
object creation and inheritance difference:

If the class does not have a constructor, and if the method is entirely static and self-contained then namespace::class::method will do.

Try it under other conditions and you will likely throw an exception.


---------------------------------------------------

git:

cloning is downloading code from repository for the first time.

to get updates from the same repository, "pull" has to be used instead of "clone"

git:

first time user to create new repository and push code:
git config --global user.name "vsjanani"
git config --global user.email "jansree90@gmail.com"
cd pythonproject #path to upload in git
git init #.git file will be created to store github reference and notes.
git add * #to add all the files in the path selected to stash or staging. - stage 1 of commit.
git status #to check if all the files are added.
git commit -m "my first commit" #files are now commited and ready to push. github only selects commited files to push.
git remote add origin *github repository path* #this path is present in the repository created. this is make connection between repository created with local files located path.
git push origin master #pushes code from local to repository's master branch.

To download the repository for the first time:
git clone *github repository path*
regular user:
cd file path.
git add *
git commit -m "message" (-m (once again) for "detailed message") or git commit and click enter to open editor for detailed message and click esc followed by :wq to save and close the editor window.
git push origin master or git pull origin master

Branches:
It is used if there are any major changes in the framework. Master branch will carry the routine testing untill sub branch framework changes are done.
If completed, sub-branch code will get merged with master branch.

cd file path
git checkout -b branchname #create new branch
git branch #to check which branch we are in.
git add *
git commit -m message
git push origin branchname
git checkout branchname #to jump to existing branch.
make changes
again add , commit and push.
now, git checkout master
git merge branchname #to merge branchcodes into master

C:\\Users\\dines\\AppData\\Local\\Programs\\Python\\Python310\\Scripts'
https://github.com/vsjanani/AutomationPractice.git
My first selenium python project


*****************************************************************************************************

jenkins:
janani
Kels3road

Git:
vsjanani
Sanjeevkrish@01
file:///C:/Program%20Files/Git/ReleaseNotes.html
download git exe.
create github acct.
use steps in learning python notepad for git commands.

selenium python step by step procedure:

install python
add python and pip to system environment variables
to verify, use, "python --version" in command prompt
pip install selenium
to verify, pip show selenium.
install pycharm editor
pip install pytest
to verify, use, pytest -version. Note: ensure latest pip version to be upgraded to avoid "pytest is not an external or internal command"
pip install pytest-html
pip install openpyxl
install git from git downloads, create github acct.


C:/Users/dines/OneDrive/Documents/MyPythonProject/chromedriver.exe

Go to jenkins path: (also check if it is added in env variables)
 C:\Program Files\Jenkins
java -jar jenkins.war
type localhost:8080 in browser and login jenkins

custom workspace in jenkins configuration:  C:\Users\dines\OneDrive\Documents\MyPythonProject

In Build section:
cd PycharmProjects\PycharmProjects\pythonProject2\E2E_Framework
pytest --browser_name "%browsername%" --html=$WORKSPACE\PycharmProjects\PycharmProjects\pythonProject2\reports\report.html-v --junitxml="result.xml"

jenkins css update:
Manage Jenkins->
Manage Nodes->
Click settings(gear icon)->
click Script console on left and type in the following command:

System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")

via github:
Home: C:\Users\dines\AppData\Local\Programs\Python\Python310\python.exe

Under command:
python -m venv env
call ./env/Scripts/activate.bat
pip install -r requirements.txt
pip install seleniumbase
sbase install chromedriver latest
pytest --browser_name "%browsername%" --html=report.html
for more infor: https://www.youtube.com/watch?v=h2Abne2jIjM


Post Build Action section:
PycharmProjects\PycharmProjects\pythonProject2\E2E_Framework\*.xml

To create venv folder:
cd D:\AutomationPractice  #go to project directory
python -m venv D:\AutomationPractice\venv
cd venv
cd Scripts
activate


To get out of venv mode, type deactivate






