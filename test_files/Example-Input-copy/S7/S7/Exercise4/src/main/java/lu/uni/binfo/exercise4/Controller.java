/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lu.uni.binfo.exercise4;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Optional;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

/**
 *
 * @author student
 */
@RestController
public class Controller implements ErrorController {

    private Entry[] entries;

    public Controller() {
        try {
            ObjectMapper objectMapper = new ObjectMapper();

            URL jsonUrl = new URL("https://disease.sh/v3/covid-19/countries");

            //read JSON file and convert to an Entry object
            entries = objectMapper.readValue(jsonUrl, Entry[].class);
            
        } catch (MalformedURLException ex) {
            Logger.getLogger(Controller.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Controller.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public Entry findEntry(String country) {
        Entry found = null;
        for (Entry entry1 : entries) {
            String countryName = entry1.getCountry();
            String iso = entry1.getCountryInfo().getIso2();

            if (iso != null && (countryName.equalsIgnoreCase(country)
                    || iso.equalsIgnoreCase(country))) {
                found = entry1;
            }

        }
        return found;
    }

    // Define GET request with path variable
    // EX: localhost:8080/exercise4/LU
    // EX: localhost:8080/exercise4/Luxembourg
    @RequestMapping("/{country}")
    public Entry getCovidDataByCountryPathVariable(
            @PathVariable("country") String country)
            throws MalformedURLException, IOException {

        Entry result = findEntry(country);

        if (result == null) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND, "Country not found"
            );
        }

        return result;
    }

    // Define GET request with request parameters or body content
    // EX: localhost:8080/exercise4/?country=LU
    // EX: localhost:8080/exercise4/?country=Luxembourg
    
    // EX: curl -X GET -d "Luxembourg" localhost:8080/exercise4
    @RequestMapping("/")
    public Entry getCovidDataByCountryWithRequestParam(
            @RequestParam("country") Optional<String> country,
            @RequestBody(required=false) String countryBody)
            throws MalformedURLException, IOException {

        Entry result = null;

        // Check if country information was provided in the request parameters
        if (country.isPresent()) {
            result = findEntry(country.get());
        } 
        // Look for country information in the body of the request
        else if(countryBody != null) {
            result = findEntry(countryBody);
        }

        if (result == null) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND, "Country not found"
            );
        }

        return result;
    }

    // Define a method to handle errors
    @RequestMapping(value = "/error", produces = "text/plain")
    public String handleError() {

        String result = "Something went wrong!"
                + "\nMake sure you typed in the correct ISO code or country name..."
                + "\n\nHere are examples on how to use the API:"
                + "\nlocalhost:8080/exercise4/LU"
                + "\nlocalhost:8080/exercise4/?country=Luxembourg";

        return result;
    }

}
