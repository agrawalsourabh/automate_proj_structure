#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


class Git_Repo(object):
    """docstring for ClassName"""
    username = ""
    password = ""
    repo_name = ""
    isCreated = False

    def __init__(self, uname, pwd, repo):
        super(Git_Repo, self).__init__()

        self.username = uname
        self.password = pwd
        self.repo_name = repo

        print("creating git repository " + self.repo_name + "...")

        self.setup()

    def setup(self):
        driver = webdriver.Chrome('/home/shivam/Downloads/chromedriver')
        driver.get('https://github.com/login')
        self.login(driver, self.username, self.password, self.repo_name)


    def login(self, driver, username, password, repo_name):

        try:
            uname = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='login']")))
            uname.send_keys(username)

            pwd = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
            pwd.send_keys(password)

            submit = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
            submit.click()

            self.create_new_repo(driver, repo_name)

        finally:
            self.close_browser(driver)

    def close_browser(self, driver):
        driver.quit()

    def create_new_repo(self, driver, repo_name):
        driver.get('https://github.com/new')
        repo_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='repository_name']")))
        repo_input.send_keys(repo_name)

        init_readme = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='repository_auto_init']")))
        init_readme.click()

        sub_btn = driver.find_element_by_css_selector('button.first-in-line')
        sub_btn.submit()

        exp_url = "https://github.com/agrawalsourabh/" + repo_name

        if exp_url == driver.current_url:
            print("Repo created successfully")

        else:
            print("Repo might already be present.")

