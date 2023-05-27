package lu.uni.javaee.restapi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.Optional;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.server.ResponseStatusException;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.json.JsonMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;

import lu.uni.javaee.restapi.Country;

@RestController
public class restApi {

  private Country countryEntity;

  // add a parameter example to the documentation
  @Parameter(in = ParameterIn.QUERY, name = "country", description = "Country name or iso2 code", required = true, example = "LU")
  @Operation(summary = "Get country info", description = "Get country deaths and cases by iso2 or full name country", tags = {
      "Country" })
  @ApiResponses(value = {
      @ApiResponse(responseCode = "200", description = "Successful operation", content = @Content(schema = @Schema(implementation = Country.class))),
      @ApiResponse(responseCode = "400", description = "Bad Request", content = @Content)
  })

  @GetMapping(path = "/exercise4/", produces = "application/json")
  public JsonNode getCountry(@RequestParam(required = true, value = "country") String country)
      throws MalformedURLException, IOException, JsonMappingException, JsonProcessingException {

    URL url = new URL("https://disease.sh/v3/covid-19/countries/");
    ObjectMapper mapper = new ObjectMapper();
    JsonNode root = mapper.readTree(url);

    // iterate over the root node
    for (JsonNode node : root) {
      // if the country exists in case insensitive then return the country info otherwise throw a bad request exception
      if (node.get("country").asText().equals(country.substring(0, 1).toUpperCase() + country.substring(1).toLowerCase()) || node.get("countryInfo").get("iso2").asText().equals(country.toUpperCase())) {
        countryEntity = new Country(country, node.get("cases").asInt(), node.get("deaths").asInt());
        return countryEntity.toJson();
      }
    }
    throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Bad Request");
  }
}