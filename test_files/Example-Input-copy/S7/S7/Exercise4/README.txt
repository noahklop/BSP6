Exercise 4

# 1. Running the API 

The API can be run using the Gradle dependency manager:

	gradle bootRun

# 2. Using the API

To access the API use the link below (the context path was set to /exercise4)

	localhost:8080/exercise4

If you are not providing any information to the server, the request will fail.
An error message will be shown.

There are 3 different ways to get COVID data related to a given country.

	1. Using path variables
	
		localhost:8080/exercise4/Luxembourg
		localhost:8080/exercise4/lu
	
	2. Using request parameters

		localhost:8080/exercise4/?country=Luxembourg
		localhost:8080/exercise4/?country=lu

	3. Sending the country name or ISO in the body of the request

		curl -X GET -d "Luxembourg" localhost:8080/exercise4
		curl -X GET -d "lu" localhost:8080/exercise4

# 3. How it's done

	The Jackson library was used to read the JSON data into a POJO (Entry.java)
	
	An instance of ObjectMapper is reading values from the JSON file
	and converting it into an Entry object (which has attributes with the
	same name as the fields in the JSON object). 

	Given an ISO code or country name the API will perform a search through
	a list of Entry objects to find a matching country name. Once found, it
	is able to return the number of deaths and cases for that country.
	Otherwise, it will generate a 404 Not Found error.


