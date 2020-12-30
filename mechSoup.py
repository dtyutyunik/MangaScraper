from selenium import webdriver

driver = webdriver.Firefox()

# get geeksforgeeks.org 
# driver.get("https://www.geeksforgeeks.org/") 
  
# get element  
# element = driver.find_element_by_class_name("gsc-input") 
  
# print complete element 
# print(element.text) 
# https://s41.mkklcdnv41.com/mangakakalot/p1/pn918005/vol2_chapter_132/1.jpg


solo='https://manganelo.com/chapter/pn918005/chapter_132'
driver.get(solo)
# result = driver.find_element_by_class_name("container-chapter-reader")
images=driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))
# print(result.getAttribute("title"))

# for article in search_bar:
    # title = article.find_element_by_xpath('/img')
    # print(title)

# all_links = driver.find_elements_by_tag_name('a')
# h1 = driver.find_element_by_xpath('//h1')
driver.close()



# driver.get('https://google.com')