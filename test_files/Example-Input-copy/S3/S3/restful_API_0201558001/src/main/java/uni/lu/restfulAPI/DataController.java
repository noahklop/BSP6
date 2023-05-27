package uni.lu.restfulAPI;

import org.springframework.web.bind.annotation.*;

@RestController
public class DataController {

    //Function called on the start page of the website if the /exercise4 endpoint is not specified
    @RequestMapping("/")
    public String startPage_without_Exercise4_endpoint()
    {
        // Return the following message in JSON format
        return "{\"message\": \"Please specify the /exercise4 endpoint to get to the Covid Data API.\"}";
    }

    //Function called on the start page of the website if the /exercise4 endpoint is specified
    @RequestMapping("/exercise4")
    public String startPage_with_Exercise4_endpoint()
    {
        // Return the following message in JSON format
        return "{\"message\": \"Welcome to the Covid Data API. Please specify the country code or the country name " +
                "in English to get the Covid Data of that country. Or add /api to check " +
                "the documentation of the API.\"}";
    }

    /*
        GET Request to retrieve the covid data of a specific country
        produces = "application/json => Response of this is json encoded
        Returns the result of the function getCountryData.
    */
    @GetMapping(value="/exercise4/{country}", produces = "application/json")
    public Object get_either_Covid_Data_or_API_Documentation(@PathVariable("country") String country){
        return CovidData.getCovidData(country);
    }
}
