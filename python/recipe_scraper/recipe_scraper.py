#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import json
import time

BASE_URL = 'https://chefgohan.gnavi.co.jp/card/detail/'

NG_WORDS = [u'材料・調味料', u'■具材']

file = open('output.txt', 'w')
recipe_dict = dict()
for recipe_id in range(1,100):
    recipe_html = urlopen(BASE_URL+str(recipe_id))
    receipe_soup = BeautifulSoup(recipe_html)
    if receipe_soup.select(".recipe_name") == []:
        continue
    for recipe in receipe_soup.select(".recipe_name"):
        recipe_name = recipe.string.strip(u'■').strip(u' ')
    recipe_material_list = []
    for recipe_material in receipe_soup.select(".materials"):
        reipe_material_string = recipe_material.string
        if not reipe_material_string in NG_WORDS:
            if reipe_material_string[0] != u'■':
                recipe_material_list += [reipe_material_string.strip()]
    recipe_dict[recipe_name] = recipe_material_list
    time.sleep(0.2)


file.write(json.dumps(recipe_dict,sort_keys=True, ensure_ascii=False, indent=2))
