import os
import selenium
from selenium import webdriver
import time
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager

os.chdir('C:/Projects/Recipe_Scraper')

# Install driver
opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)


def scroll_to_end(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)  # sleep_between_interactions


def getRecipesByName(name, totalRecipes):
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
            'id': recipe_count + 1,
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


def getRecipesByNameFiltered(name, totalRecipes, include, exclude):
    search_url = 'https://www.epicurious.com/search/{name}?content=recipe'

    # include
    for i in range(len(include)):
        if i == 0:
            search_url += '&include=' + include[0]
        else:
            search_url += '%2C' + include[i]
    # exclude
    for i in range(len(exclude)):
        if i == 0:
            search_url += '&exclude=' + exclude[0]
        else:
            search_url += '%2C' + exclude[i]

    print('URL: ', search_url)

    driver.get(search_url.format(name=name))
    recipes = []
    recipe_count = 0

    scroll_to_end(driver)

    results = driver.find_elements_by_xpath(
        '//article[contains(@class,"recipe-content-card")]')

    while recipe_count < totalRecipes:
        # name, reviews, make it again, url
        recipe = {
            'id': recipe_count + 1,
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


def getRecipesByIngredients(totalRecipes, include, exclude):
    search_url = 'https://www.epicurious.com/search/?content=recipe'

    # include
    for i in range(len(include)):
        if i == 0:
            search_url += '&include=' + include[0]
        else:
            search_url += '%2C' + include[i]
    # exclude
    for i in range(len(exclude)):
        if i == 0:
            search_url += '&exclude=' + exclude[0]
        else:
            search_url += '%2C' + exclude[i]

    print('URL: ', search_url)

    driver.get(search_url)
    recipes = []
    recipe_count = 0

    scroll_to_end(driver)

    results = driver.find_elements_by_xpath(
        '//article[contains(@class,"recipe-content-card")]')

    while recipe_count < totalRecipes:
        # name, reviews, make it again, url
        recipe = {
            'id': recipe_count + 1,
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
