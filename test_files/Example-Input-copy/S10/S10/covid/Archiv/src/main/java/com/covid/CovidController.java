package com.covid;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CovidController {

    public Covid covid = new Covid();

    @GetMapping("/")
    public String index() {
        return "Please write a country name after the slash!";
    }

    //@GetMapping("exercise4/{name}")
    @GetMapping(value="/exercise4/{name}", produces = "application/json")
    public String getCountry(@PathVariable(value="name") String name)
    {
        System.out.println("Country:" + name);
        return covid.getCountry(name);
    }
}
