package com.uni.exercise4;
import io.swagger.v3.oas.annotations.*;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import java.io.IOException;
import org.json.simple.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@SuppressWarnings("unchecked")
@SpringBootApplication
@RestController
@OpenAPIDefinition(info=@Info(title="Exercise 4 REST API Documentation"),externalDocs = @ExternalDocumentation(url = "https://www.uni.lu",description = "Project by Ahmad Mohamed Ali from the University of Luxembourg"))
public class Exercise4Application {
	//constructor to throw exceptions.
	public Exercise4Application() throws IOException, org.json.simple.parser.ParseException {
	}
	//main method to run the springboot API
	public static void main(String[] args) {
		SpringApplication.run(Exercise4Application.class, args);
	}
	//call the method class that contains the methods needed for the get request later.
	Methods methods = new Methods();

	//@Operation is used to add documentation to the OpenAPI library.
	@Operation(
		//call the get requests and put them all under one tag (GetRequests.)
		tags = {"GetRequests"},
			//add a summary to our get request.
			summary = "Get request with string parameter",
			//give description to the get request.
			description = "Get request with string parameter to get you the deaths and cases of COVID-19 in a chosen country.",
			//give description to the parameters used inside the get request, and give some examples of inputs.
			parameters = {@Parameter(name = "country",description = "The country name you enter can be of type ISO2 or the country name. "+
			"First Letter has to be capital, and if ISO2 then both letters have to be capital.",example = "luxembourg/Luxembourg/LUXEMBOURG/Lu/lu/LU")},
			//give the possible responses of this get request, descripe them, and give example of how they should look like. 
			responses = {
				@ApiResponse(responseCode = "200",
				content = @Content(schema = @Schema(implementation = ResponseItem.class),mediaType = MediaType.APPLICATION_JSON_VALUE),
				description = "Success response would get you the number of cases  and the number of deaths"),
				@ApiResponse(responseCode = "406",
				content = @Content(schema = @Schema(implementation = BadResponseItem.class),mediaType = MediaType.APPLICATION_JSON_VALUE),
				description = "wrong value passed"),
				@ApiResponse(responseCode = "404",
				content = @Content(schema = @Schema(implementation = BadResponseItem.class),mediaType = MediaType.APPLICATION_JSON_VALUE),
				description = "Country name or Country iso is not found")
			}
	)
	//create a get request with endpoint exercise4 and parameters that pass in the path as country.
	@GetMapping(value = "/exercise4/{country}")
    public ResponseEntity<JSONObject> getJSON(@PathVariable String country) {
		//check if the variable received is not iso, since iso 2 consist of two letters, we can check if we have more than 2 letters.
		//this will mean that the variable received is not iso2.
		if(country.length() > 2){
			//apply the method to check with contryname with the received variable.
			return methods.checkWithName(country);
		}
		//check if the variable received is iso, since iso 2 consist of two letters, we check if the variable has exactly 
		//two letters.
		else if(country.length() == 2){
			//apply the method to check with country ISO with the received variable.
			return methods.checkWithIso(country);
		}
		//other than those two conditions, an error with input value is wrong is sent as response.
		JSONObject result = new JSONObject();
		result.put("error", "Input Value is wrong.");
		return new ResponseEntity<>(result, HttpStatus.NOT_ACCEPTABLE);
    }
}