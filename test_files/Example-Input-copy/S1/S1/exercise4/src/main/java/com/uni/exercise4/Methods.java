package com.uni.exercise4;

import java.io.IOException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import org.apache.commons.io.IOUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

@SuppressWarnings("unchecked")
public class Methods {
    public Methods() throws IOException, org.json.simple.parser.ParseException {
	}
    //getting the JSON file that contains the data of the covid-19 Cases
	URL url = new URL("https://disease.sh/v3/covid-19/countries");
	//download the JSON file from the URL
	String json = IOUtils.toString(url, StandardCharsets.UTF_8);
	//parse the JSON file into JSONArray.
    JSONParser parser = new JSONParser();
	Object obj = parser.parse(json);
	JSONArray countriesArray =  (JSONArray) obj;

    //method to check for an iso2 variable.
    //return the cases and deaths of this country as a responseEntity that contains jsonObject.
    public ResponseEntity<JSONObject> checkWithIso(String body){
        //convert the received body to Upper case in case it comes lowerCase.
        body = body.toUpperCase();
        // create a for loop to loop inside the JSONarray that contains all the countries.
        for (Object o : countriesArray) {
            //pass each object to JSONobject
            JSONObject countryObject = (JSONObject) o;
            //get the key CountryInfo that contains nested inside it the iso2 code.
            JSONObject countryInfo = (JSONObject) countryObject.get("countryInfo");
            // get the value of the key iso2 inside the key countryInfo and convert it as a string.
            String iso2 = (String) countryInfo.get("iso2");
            //check if the iso2 string equals the received variable.
            if(String.valueOf(iso2).equals(body)){
                //create a jsonobject ot pass as a response.
                JSONObject response = new JSONObject();
                //get the values of the keys cases and deaths, then create a new JSONobject, then pass it as a response.
                response.put("cases", countryObject.get("cases"));
                response.put("deaths", countryObject.get("deaths"));
                return new ResponseEntity<>(response, HttpStatus.OK);
            }
        }
        //create an error response if the iso is not found.
        JSONObject response = new JSONObject();
        response.put("error", "ISO NOT FOUND");
        return new ResponseEntity<>(response, HttpStatus.NOT_FOUND);
    }

    //method to check for a country name variable, 
    //return the cases and deaths of this country as a responseEntity that contains jsonObject.
    public ResponseEntity<JSONObject> checkWithName(String body){
        //capitalize the first letter and lower case the rest, to match it with the country name from the JSON file countries.
        body = body.substring(0, 1).toUpperCase() + body.substring(1).toLowerCase();
        // create a for loop to loop inside the JSONarray that contains all the countries.
        for (Object o : countriesArray) {
            //pass each object to JSONobject
            JSONObject jsonObject = (JSONObject) o;
            //get the country name value using the key "country"
            //check if it is equal to the received variable.
            if (jsonObject.get("country").equals(body)){
                //create a jsonobject ot pass as a response.
                JSONObject response = new JSONObject();
                //get the values of the keys cases and deaths, then create a new JSONobject, then pass it as a response.
                response.put("cases", jsonObject.get("cases"));
                response.put("deaths", jsonObject.get("deaths"));
                return new ResponseEntity<>(response, HttpStatus.OK);
            }
        }
        //create an error response if the country is not found.
        JSONObject response = new JSONObject();
        response.put("error", "COUNTRY NOT FOUND");
        return new ResponseEntity<>(response, HttpStatus.NOT_FOUND);
    }
}
