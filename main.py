import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
import json

os.chdir('D:/Personal Projects/Recipe_Scraper')

# Install driver
opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)


def scroll_to_end(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)  # sleep_between_interactions

# no license issues


def getRecipes(name, totalRecipes, driver):

    search_url = 'https://www.epicurious.com/search/{name}?content=recipe'
    driver.get(search_url.format(name=name))
    recipes = []
    recipe_count = 0

    scroll_to_end(driver)

    results = driver.find_elements_by_xpath(
        '//article[contains(@class,"recipe-content-card")]')

    while recipe_count < totalRecipes:
        # name, reviews, make it again, url
        recipe = {
            'name': results[recipe_count].find_element_by_css_selector(
                'a.view-complete-item').get_attribute('title'),
            'review_count': results[recipe_count].find_element_by_css_selector(
                'dl.recipes-ratings-summary').get_attribute('data-reviews-count'),
            'rating': results[recipe_count].find_element_by_css_selector(
                'dl.recipes-ratings-summary').get_attribute('data-reviews-rating'),
            'make_it_again': results[recipe_count].find_element_by_css_selector(
                'dd.make-again-percentage').text,
            'url': results[recipe_count].find_element_by_css_selector(
                'a.view-complete-item').get_attribute('href')
        }
        recipes.append(recipe)
        recipe_count += 1

    return recipes


def saveToTextFile(searchNames, destDir, totalRecipes, driver):
    for name in list(searchNames):
        path = os.path.join(destDir, name + '.txt', )
        if os.path.exists(path):
            os.remove(path)

        recipes = getRecipes(name, totalRecipes, driver)

        # No recipes exist
        if recipes is None:
            print('images not found for :', name)
            continue
        else:
            with open(path, 'w') as file:
                for recipe in recipes:
                    file.write(json.dumps(recipe))
                    file.write('\n')


searchNames = ['christmas', 'korean']
destDir = f'./data/'
totalRecipes = 5

saveToTextFile(searchNames, destDir, totalRecipes, driver)
print("DONE")
