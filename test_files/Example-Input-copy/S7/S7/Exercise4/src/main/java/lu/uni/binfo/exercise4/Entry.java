/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lu.uni.binfo.exercise4;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 *
 * @author student
 */

// POJO representing an entry in the JSON COVID data

// Ignore properties that we are not interested in
@JsonIgnoreProperties(ignoreUnknown = true)
public class Entry {
    
    // Define attributes for each field in the JSON data we want to retrieve
    private String country;
    
    // Since the information on the ISO code is contained inside a nested object
    // we need to define another class to retrieve the latter
    private CountryInfo countryInfo;
    
    private int cases, deaths;

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public CountryInfo getCountryInfo() {
        return countryInfo;
    }

    public void setCountryInfo(CountryInfo countryInfo) {
        this.countryInfo = countryInfo;
    }

    public int getCases() {
        return cases;
    }

    public void setCases(int cases) {
        this.cases = cases;
    }

    public int getDeaths() {
        return deaths;
    }

    public void setDeaths(int deaths) {
        this.deaths = deaths;
    }
    
    
    
}
