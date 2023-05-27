package lu.uni.javaee.restapi;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class Country {

  private String countryID;
  private int cases;
  private int deaths;

  public Country(String countryID, int cases, int deaths) {
    this.countryID = countryID;
    this.cases = cases;
    this.deaths = deaths;
  }

  public String getCountryID() {
    return this.countryID;
  }

  public void setCountryID(String country) {
    this.countryID = country;
  }

  public int getCases() {
    return this.cases;
  }

  public void setCases(int cases) {
    this.cases = cases;
  }

  public int getDeaths() {
    return this.deaths;
  }

  public void setDeaths(int deaths) {
    this.deaths = deaths;
  }

  public JsonNode toJson() throws JsonMappingException, JsonProcessingException {

     ObjectNode objectNode = new ObjectMapper().createObjectNode();
     ObjectMapper mapper = new ObjectMapper();

     objectNode.put("cases", this.getCases());
     objectNode.put("deaths", this.getDeaths());
     JsonNode jsonNode = mapper.readTree(objectNode.toString());
    return jsonNode;
  }
}
