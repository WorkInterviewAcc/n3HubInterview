I was unable to finish the technical challenge.

Going forward I would like to have linked gen.py to the file_manager. 
api.py would call this to create the file at first point. 

I would need to store the column type information somewhere to validate 
posted data against. Keeping the data in order would have been accomplished
by requesting id/sequence numbers.

I would also need to know the number of data rows being sent. I imagine
connecting a database to store meta data about the files.

I have included testing data in the DataFolder which should automatically be 
read. This simulates a call to the database.

I have included testing requests which should hit the data I have created. This
should simplify the testing process.