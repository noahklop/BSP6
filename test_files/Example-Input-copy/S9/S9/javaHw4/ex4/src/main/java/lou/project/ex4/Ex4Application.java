package lou.project.ex4;


import com.google.gson.*;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import java.io.*;
import java.net.URL;



@SpringBootApplication
@RestController
public class Ex4Application {

	@GetMapping("/exercise4")
	public String getCovidData (@RequestBody String mybody) throws IOException {
		Gson gson = new Gson();
		URL url = new URL("https://disease.sh/v3/covid-19/countries");
		InputStreamReader reader = new InputStreamReader(url.openStream());
		JsonArray arrayValues = gson.fromJson(reader ,JsonArray.class);

		//------------------------------------------------------------------------------------------------//
		//Working country retriever
		for (JsonElement o : arrayValues) {
			JsonObject jsonObject = gson.fromJson(o, JsonObject.class);

			if (mybody.equals(jsonObject.get("country").getAsString())){
				return "Number of cases: " + jsonObject.get("cases").toString() + " Number of Deaths: " + jsonObject.get("deaths").toString();
			}
		}
		//------------------------------------------------------------------------------------------------//
		//Getting ISO2

		for (JsonElement o : arrayValues){
			JsonObject jsonObject = gson.fromJson(o, JsonObject.class);
			JsonObject info = jsonObject.getAsJsonObject("countryInfo");
			Object key = info.get("iso2");
//REGEX to get rid of ""
			if (mybody.equals(key.toString().replaceAll("^\"|\"$", ""))){
				return "Number of cases: " + jsonObject.get("cases").toString() + " Number of Deaths: " + jsonObject.get("deaths").toString();
			}
		}
		reader.close();
		//Misspelled ISO2 or Country throw back error
		return "This might be an error: " + mybody;
	}

	//RUN
	public static void main(String[] args) {

		SpringApplication.run(Ex4Application.class, args);
	}

}
