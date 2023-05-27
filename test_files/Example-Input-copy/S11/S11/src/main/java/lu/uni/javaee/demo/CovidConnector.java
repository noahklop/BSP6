package lu.uni.javaee.demo;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.springframework.http.ResponseEntity;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Locale;

public class CovidConnector {
    private static final String API_ENDPOINT = "https://disease.sh/v3/covid-19/countries";

    public ResponseEntity<String> getDataForCountry(String countryCode) {
        // Verify the country code
            // Retrieve the data from the API
            JsonNode data = getDataFromApi(countryCode);
            // Return the json data for the country
            if (data != null) {
                return ResponseEntity.status(200).body(parseData(data));
            }
        return ResponseEntity.status(422).body("{\"error\":\"invalid country code\"}");
    }

    private JsonNode getDataFromApi(String country) {
        try {
            // Create the URL object
            URL url = new URL(API_ENDPOINT + "/" + country);
            // Create the ObjectMapper object
            ObjectMapper mapper = new ObjectMapper();
            // Read the data from the URL and return it
            return mapper.readTree(url);
        } catch (IOException e) {
            return null;
        }
    }

    private String parseData(JsonNode data) {
        // Iterate over every country in the json data
            ObjectMapper mapper = new ObjectMapper();
            ObjectNode rootNode = mapper.createObjectNode();

            rootNode.put("cases", data.get("cases").asInt());
            rootNode.put("deaths", data.get("deaths").asInt());

            try {
                // Return the json object as a string
                return mapper.writeValueAsString(rootNode);
            } catch (IOException e) {
                e.printStackTrace();
            }
        return "{\"error\":\"No data for country code\"}";
    }
}
