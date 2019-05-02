###SUAEx 
The "Simple Unsupervised Similarity-based Aspect Extraction" is a method to extract aspect words(most relevant words in a given sentence and domain). SUAEx implements a simple approach that only relies on word-embeddings similarity with respect to reference words. Furthermore, it emulates the attention mechanism of neural networks by using only the similarity of words. 

#### Dependencies

```
* python3 
* gensim 3.5.2
* sklearn 0.0
```

#### Usage

##### Model 
	* Download the word-embeddings model from(restaurant.txt): 
			https://mega.nz/#!rihQiYhL!jdGipAwlxX4F-RWTRjoNQLZWH_fit2zwQZBCn8QsQxc
	* Create the folder "models"
	* Put the download model on the created folder
##### This folder contains the implementation of SUAEx which is organized in three folders
	* word_simils
	* category_atribution
	* select_aspects
##### Through this implementation, we can run SUAEx on the restaurant ABAE dataset. Bellow the steps to run the example
	* On "word_simils/code/" run the python script  getaspectbysimil_v3restaurant.py
			*python getaspectbysimil_v3restaurant.py*
	* On "category_atribution/" run the python script cat_atrib_rest.py
			*python cat_atrib_rest.py*
	* On "select_aspects/" run the python script select.py
			*python select.py*		

#### Citation <br />
```	
If using SUAEx, please cite our work by : 
		@inproceedings{Suarez19, 
  		title={Simple Unsupervised Similarity-Based Aspect Extraction}, 
  		author={Danny Suarez Vargas, Lucas R. C. Pessutto, and
               Viviane Pereira Moreira}, 
  		booktitle={20th International Conference on Computational Linguistics and Intelligent Text Processing (CICLing)}, 
  		year={2019} 
		} 
```
