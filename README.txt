1) Model
	a) Download the word-embeddings model from
	https://mega.nz/#!rihQiYhL!jdGipAwlxX4F-RWTRjoNQLZWH_fit2zwQZBCn8QsQxc 
	b) Create the folder "models" 
	c) Put the download model on the created folder
	
2) This folder contains the implementation of SUAEx which is organized in three folders
	a) word_simils
	b) category_atribution
	c) select_aspects
3) Through this implementation, we can run SUAEx on the restaurant ABAE dataset. Bellow the steps to run the example
	a) On "word_simils/code/" run the python script  getaspectbysimil_v3restaurant.py
		python getaspectbysimil_v3restaurant.py
	b) On "category_atribution/" run the python script cat_atrib_rest.py
		python cat_atrib_rest.py
	c) On "select_aspects/" run the python script   select.py
		python select.py

4) Requirements
	python3
	gensim
	sklearn
