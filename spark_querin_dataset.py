# First we need to import the following Row class
from pyspark.sql import SQLContext, Row
# Create a RDD peopleAge,
# when this is done the RDD will
# be partitioned into three partitions
peopleAge = sc.textFile("examples/src/main/resources/people.txt")
# Since name and age are separated by a comma let's split them
parts = peopleAge.map(lambda l: l.split(","))
# Every line in the file will represent a row
# with 2 columns name and age.
# After this line will have a table called people
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))
# Using the RDD create a DataFrame
schemaPeople = sqlContext.createDataFrame(people)
# In order to do sql query on a dataframe,
# you need to register it as a table
schemaPeople.registerTempTable("people")
# Finally we are ready to use the DataFrame.
# Let's query the adults that are aged between 21 and 50
adults = sqlContext.sql("SELECT name FROM people \
       WHERE age >= 21 AND age <= 50")
# loop through names and ages
adults = adults.map(lambda p: "Name: " + p.name)
for Adult in adults.collect():
  print Adult