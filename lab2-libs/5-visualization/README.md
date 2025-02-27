## VISUALIZATION

`matplotlib` `plotly` `seaborn` `pairplot` `boxplot` `hist`

### Условие

В этом задании вам нужно проанализировать данные о кинофильмах из датасета IMDB с помощью pandas и визуализации.

Задания находятся в jupyter-ноутбуке `imdb.ipynb`, там же вам нужно будет провести анализ и нарисовать графики. Ответы на задания для автоматической проверки нужно заполнить в файле `imdb.py`. Закоммитить нужно оба файла!

### Данные

Данные лежат в файле `imdb.csv`. Они были взяты с [kaggle](https://www.kaggle.com/orgesleka/imdbmovies), который уже недоступен, но осталась [сохраненная копия](http://web-old.archive.org/web/20200726101316/https://www.kaggle.com/orgesleka/imdbmovies) описания.

The IMDB Movies Dataset contains information about 14,762 movies. 
Information about these movies was downloaded with wget for the purpose of creating a movie recommendation app. 
The data was preprocessed and cleaned to be ready for machine learning applications.

Content
* title
* wordsInTitle
* url
* imdbRating
* ratingCount
* duration
* year
* type
* nrOfWins
* nrOfNominations
* nrOfPhotos
* nrOfNewsArticles
* nrOfUserReviews
* nrOfGenre

The rest of the fields are dummy (0/1) variables indicating if the movie has the given genre:
* Action
* Adult
* Adventure
* Animation
* Biography
* Comedy
* Crime
* Documentary
* Drama
* Family
* Fantasy
* FilmNoir
* GameShow
* History
* Horror
* Music
* Musical
* Mystery
* News
* RealityTV
* Romance
* SciFi
* Short
* Sport
* TalkShow
* Thriller
* War
* Western