package Exercice4.RESTfullWS;

import com.google.gson.*;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Objects;




@SpringBootApplication
@RestController
public class RESTfullWsApplication {

	public String getJSONFile(String info) throws IOException{
			// URL of the API
			URL jsonURL = new URL("https://disease.sh/v3/covid-19/countries");
			// Read the JSON file
			InputStreamReader reader = new InputStreamReader(jsonURL.openStream());

			JsonArray jsonFile = new Gson().fromJson(reader, JsonArray.class);
			//Create a JsonArray to store the data.
			JsonObject country = new JsonObject();

			//Sanity check
			if (info.length() == 2) {
				info = info.toUpperCase();
			}
			else {
				info = info.substring(0, 1).toUpperCase() + info.substring(1).toLowerCase();
			}


			//Create a for loop to go through the JSON file.
			for (JsonElement o : jsonFile ){
				//Get the ISO2 of the country and check if the value is not null.
				String getISO2 = o.getAsJsonObject().getAsJsonObject("countryInfo").get("iso2") != JsonNull.INSTANCE ? o.getAsJsonObject().getAsJsonObject("countryInfo").get("iso2").getAsString() : null;
				//If the country is equal to the info parameter or if the ISO2 is equal to the info parameter, then we get the informations.
				if (o.getAsJsonObject().get("country").getAsString().equals(info) || Objects.equals(getISO2, info)){
					String getCases = o.getAsJsonObject().get("cases").getAsString();
					String getDeaths = o.getAsJsonObject().get("deaths").getAsString();
					//We add the informations to JsonObject.
					country.add("Cases", new JsonPrimitive(getCases));
					country.add("Deaths", new JsonPrimitive(getDeaths));

					//We return the JsonObject.
					return country.toString();
				}
			}
			//If the country is not found, we return an error message.
			return "Country not found";
	}

	//OpenAPI
	@Operation(
	tags = {"Exercice 4"},
	summary = "Get the number of cases and deaths of a country",
	description = "Enter a country name or a country ISO2 code to get the number of cases and deaths of the country.",
	responses = {
			@ApiResponse(responseCode = "200", description = "SUCCESS : Return the number of cases and deaths of a country"),
			@ApiResponse(responseCode = "404", description = "Country not found")
		}
	)



	@GetMapping("/exercice4")
	public String readJsonWithObjectMapper(@RequestBody String country) throws IOException {
		//Call the getJSONFile method and return the result.
		return getJSONFile(country);
	}



	public static void main(String[] args) { SpringApplication.run(RESTfullWsApplication.class, args); }



}
