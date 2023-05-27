package com.example.demo;

import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
//import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;


@RestController
@RequestMapping
public class AppController {

    // @Operation(
    //     responses = {@ApiResponse(responseCode = "200", content = @Content(schema = @Schema(implementation = String.class)))}
    // )

    @GetMapping("/exercise4/{body}")
    public ResponseEntity<Object> getData(@PathVariable String body) throws IOException{
        RestTemplate restTemplate = new RestTemplate();
        String url = "https://disease.sh/v3/covid-19/countries";
        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);
        String str = response.getBody();
        JSONArray arr = new JSONArray(str);
        for(int i = 0; i < arr.length(); i++){
            JSONObject obj = arr.getJSONObject(i);
            String country = obj.getString("country");
            String iso = obj.getJSONObject("countryInfo").get("iso2").toString();
            if(body.equals(country) || body.equals(iso)){
                JSONObject objAdd = new JSONObject();
                objAdd.put("cases", obj.getInt("cases"));
                objAdd.put("deaths", obj.getInt("deaths"));
                return new ResponseEntity<>(objAdd.toMap(), HttpStatus.OK);
            }
        }

        JSONObject whatev = new JSONObject();
        whatev.put("error", "country or iso not found!");
        return new ResponseEntity<>(whatev.toMap(), HttpStatus.NOT_FOUND);
    }  

}
