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
@JsonIgnoreProperties(ignoreUnknown = true)
public class CountryInfo {
    
    private String iso2;

    public String getIso2() {
        return iso2;
    }

    public void setIso2(String iso2) {
        this.iso2 = iso2;
    }    
    
}
