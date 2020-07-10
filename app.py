from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time,sys,os
import pandas
from sys import platform
from modules import initializeFile
cur_path = sys.path[0]

print("\n\nProcessing.....")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def extractData():
    # Username Extractor
    username = browser.find_elements_by_xpath('//div[@class="_2b05"]/a')

    for u in username:
        # print(u.text)
        # print(u.get_attribute('href'))
        name.append(u.text)
        links.append(u.get_attribute('href'))
        groups_name.append(group_name)
        groups_url.append(url)
    comments = browser.find_elements_by_xpath('//div[@data-sigil="comment-body"]')
    for t in comments:
        text.append(t.text)

if platform == "linux" or platform == "linux2":
    # linux
    path = resource_path('driver/chromedriver')
else:
    path = resource_path('driver/chromedriver.exe')
    # Windows...


browser =webdriver.Chrome(path)
# open link
# link = input("Enter link: ")
# req=driver.get('https://www.facebook.com/permalink.php?story_fbid=285099952677276&id=100035318194986')

# while(True):
# if(driver.title == "Facebook" or driver.title == "Log in to Facebook | Facebook"):
browser.get('https://m.facebook.com/')
signup_elem = browser.find_element_by_id('m_login_email')
signup_elem.send_keys('@gmail.com')

login_elem = browser.find_element_by_id('m_login_password')
login_elem.send_keys('pass')

ins = browser.find_elements_by_tag_name('button')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        break
#then key here move to mobile version as that doesn't support javascript
time.sleep(5)
# initialize main file
initializeFile()
groups_url = []
groups_name = []
text= []
name = []
links = []
subtext = []
c = 0
# enter post link here make sure to edit www. to m. to use mobile view
with open(cur_path+'/urls.txt','r') as f:
    line = f.readlines()
    for e in line:
        url = e
        group_name = url.replace("https://m.facebook.com/groups/","")

        browser.get(url)
        time.sleep(3)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        browser.execute_script("scrollBy(0,250);")

        # time.sleep(10)
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        post_links = []
        # URL Extractor
        posts = browser.find_elements_by_xpath("//div[@class='_52jc _5qc4 _78cz _24u0 _36xo']/a")
        print("selected all...about to iterate")
        for p in posts:
            rel_url = p.get_attribute('href')
            post_links.append(rel_url)

        # Go to those URLS
        for urls in post_links:
            print("Group# "+ str(c))
            browser.get(urls)
            time.sleep(3)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            browser.execute_script("scrollBy(0,0);")

            # Comments Extractor
            # comments = browser.find_elements_by_class_name("_14v5")
            # for d in comments:
            #     # print(d.text)
            #     text.append(d.text)
            extractData()


            try:
                browser.find_element_by_link_text("View more comments…").click()
                
                time.sleep(4)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                extractData()
                print("Finding more")
            except Exception as e:
                continue
            else:
                browser.find_element_by_link_text("View previous comments…").click()
                time.sleep(4)
                browser.execute_script("scrollBy(0,250);")
                extractData()
                print("Finding more")

        c+=1


print(len(groups_name))
print(len(groups_url))
print(len(links))
print(len(text))
print(len(name))





data =  {
    "Group Name": groups_name, 
    "Group URL" : groups_url,
    "Comments": text,
    "Commentor Name" : name,
    "Commentor Profile URL" : links
}

df = pandas.DataFrame(data,columns=["Group Name", "Group URL", "Comments","Commentor Name","Commentor Profile URL"])
df.to_csv(cur_path +  "/combined_file.csv", mode='a', header=False)
print(df)
print("Complete...")