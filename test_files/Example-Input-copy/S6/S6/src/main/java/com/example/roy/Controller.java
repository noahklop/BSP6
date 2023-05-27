package com.example.roy;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.net.URL;

@RestController
public class Controller {

    @RequestMapping("/")
    public String home() {
        return "Springboot online";
    }

    @GetMapping(value = "/exercise4/{info}", produces = "application/json")
    public String exercise4(@PathVariable String info){
        JsonNode node = null;
        ObjectMapper mapper = new ObjectMapper();
        try {
            URL url = new URL("https://disease.sh/v3/covid-19/countries/"+ info);
            node = mapper.readTree(url);
            int cases = node.get("cases").asInt();
            int deaths = node.get("deaths").asInt();
            ObjectNode newNode =  mapper.createObjectNode();
            newNode.put("Cases",cases);
            newNode.put("Deaths",deaths);
            return mapper.writeValueAsString(newNode);
        }catch (Exception e){
            return e.getMessage();
        }
    }
}
