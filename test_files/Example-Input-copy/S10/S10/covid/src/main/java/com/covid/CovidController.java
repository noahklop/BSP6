package com.covid;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author Marnix Van den Wijngaert
 */

@RestController
public class CovidController {

    public Covid covid = new Covid();

    @GetMapping("exercise4")
    public String index() {
        return "Please write a country name after the slash!";
    }

    @GetMapping(value="/exercise4/{name}", produces = "application/json")
    public String getCountry(@PathVariable(value="name") String name)
    {
        return covid.getCountry(name).toString();
    }
}
