package lu.uni.exercise4;

import org.json.simple.JSONObject;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class CovidData {

    @GetMapping(path = "exercise4/{country}", produces = "application/json")
    public String getCountryData(@PathVariable String country) {
        String url = "https://disease.sh/v3/covid-19/countries/" + country;
        RestTemplate restTemplate = new RestTemplate();
        JSONObject result = restTemplate.getForObject(url, JSONObject.class);
        assert result != null;
        return "{Country: " + result.get("country") + "\nCases: " + result.get("cases") + "\nDeaths: " + result.get("deaths") + "}";
    }
}
