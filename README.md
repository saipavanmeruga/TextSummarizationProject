# End to End TextSummarizationProject

## Workflows

1. Update config.yaml
2. Update Params.yaml
3. Update entity
4. Update Configuration manager in src/config/
5. Update the components 
6. Update the pipeline
7. Update the main.py
8. Update the app.py


## Error Faced while building Data Ingestion Component
The urlib library in python provides a function called request.urlretrieve() but I got an authetication error and the data from
github repository was not getting downloaded.

I did not find a way to fix error, however, I used an alternative provided in the sources I read from the internet.
The alternative is to install wget package for python and use wget.download() function to get the dataset from github repository.

