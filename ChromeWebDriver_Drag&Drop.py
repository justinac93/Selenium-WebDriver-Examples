# function to test moving draggable item into box then back




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def dragMe():
    with webdriver.Chrome() as driver:
        action = ActionChains(driver) 
            # with statement ensures proper closure of driver 

        driver.get('https://demoqa.com/droppable')
        driver.implicitly_wait(1)
        drag_me = driver.find_element(By.ID, 'draggable')
        drop_me = driver.find_element(By.ID, 'droppable')
        action.drag_and_drop(drag_me, drop_me).perform()
            # clicks 'drag_me' and drops to 'drop_me'
        time.sleep(1)
        action.drag_and_drop_by_offset(drag_me, -200, 0).perform()
            # reclicks 'drag_me' and moves 200 pixels to the left
        time.sleep(1)


dragMe()
