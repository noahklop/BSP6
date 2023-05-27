package uni.lu.restfulAPI;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Locale;
import java.util.Set;

public class CovidData {
    // This attribute will be used to store the country code/name.
    private static String country;

    /*
        The following Set will be used to store the country codes and the function isValidISOCountry() will be used to
        check if the country code is valid.
        I found this check on the following website:
        https://stackoverflow.com/questions/15921332/cleaner-way-to-check-if-a-string-is-iso-country-of-iso-language-in-java
    */
    private static final Set<String> ISO_COUNTRIES = Set.of(Locale.getISOCountries());

    private static boolean isValidISOCountry(String givenCountry) {
        // The givenCountry will be converted to uppercase to make sure that the country code is valid and will be
        // stored in the country attribute.
        country = givenCountry.toUpperCase();
        return ISO_COUNTRIES.contains(country);
    }

    /*
        The following function is a check to see if the givenCountry is a valid country name. If it is, the country
        name will be stored in the country attribute.
     */
    private static boolean isValidCountryName(String givenCountry) {
        // For each country code in the ISO_COUNTRIES set, the country name will be checked.
        for (String isoCountry : ISO_COUNTRIES) {
            // Get the country name in English
            Locale locale = new Locale("en", isoCountry);
            // To make sure that the country name is in English because getDisplayCountry() returns the country
            // name in the default language of the locale
            Locale.setDefault(locale);
            // Get the country name in English (e.g. Luxembourg)
            String countryName = locale.getDisplayCountry();
            // Change the first letter of the given country name to uppercase and the rest to lowercase
            givenCountry = givenCountry.substring(0, 1).toUpperCase()
                    + givenCountry.substring(1).toLowerCase();
            // Check if the country name is the same as the input country name
            if (countryName.equals(givenCountry)) {
                // If it is, the country name will be stored in the country attribute
                country = givenCountry;
                return true;
            }
        }
        return false;
    }

    /*
        The following function is called by the CovidDataController class. It will check if the givenCountry is a
        valid country code or a valid country name. If it is, the function will return the covid data of the given
        country. If it is not, the function will return an error message.
     */
    public static Object getCovidData(String givenCountry) {
        // Check if the input is a valid country code or a valid country name
        if(isValidISOCountry(givenCountry) || isValidCountryName(givenCountry)){
            // If the input is a valid country code or a valid country name, then return the covid data of that country
            try {
                // Since the givenCountry is a valid country code or a valid country name, the country attribute will
                // be used to get the covid data of that country, because the country attribute is the country code
                // or the country name in English.
                return getCovidDataFromWebsite(country);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        else{
            // If the input is not a valid country code or a valid country name, then return an error message in JSON
            // format.
            return "{\"error\": \"The given country is not a valid country code or a valid country name.\"}";
        }
    }

    /*
        The following function will get the covid data of the given country from the following website:
        https://api.covid19api.com/summary.
        The function will return the covid data of the given country in json format.

        To get the covid data of a specific country, I used the following website to check how to do it:
        https://www.digitalocean.com/community/tutorials/java-httpurlconnection-example-java-http-request-get-post
     */
    private static Object getCovidDataFromWebsite(String country) throws IOException {
        // Create a new URL object with the following website as the parameter
        URL url = new URL("https://disease.sh/v3/covid-19/countries/"+country);
        // Open a connection to the website
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        // Set the request method to GET
        con.setRequestMethod("GET");
        // Set the request property to User-Agent
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        // Get the response code
        int responseCode = con.getResponseCode();
        // Check if the response code is 200 (OK)
        if (responseCode == HttpURLConnection.HTTP_OK) {
            // If the response code is 200 (OK), then read the response
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            // Create a new StringBuffer object
            StringBuffer response = new StringBuffer();

            // Read the response line by line
            while ((inputLine = in.readLine()) != null) {
                // Append the response line to the StringBuffer object
                response.append(inputLine);
            }
            // Close the BufferedReader object
            in.close();

            // Return the response in json format
            return getCasesAndDeaths(response);
        } else {
            // If the response code is not 200 (OK), then return an error message in JSON format
            return "{\"error\": \"GET request not worked to retrieve the covid data.\"}";
        }
    }

    /*
        The following function is used to get the covid data of the given country from the response of the
        getCovidDataFromWebsite() function. The function will return the covid data of the given country in json
        format and it will return only the cases and deaths of the given country.
     */
    private static String getCasesAndDeaths(StringBuffer response){
        // Split the response into an array of strings
        String[] responseArray = response.toString().split(",");
        String cases = "";
        String deaths = "";
        // For each string in the responseArray, check if the string contains the cases or the deaths of the given
        // country
        for(String content: responseArray){
            // Split the string into an array of strings
            String[] contentArray = content.split(":");
            // Check if the string equals the word "cases"
            if(contentArray[0].equals("\"cases\"")){
                // If the string equals the word "cases", then get the cases of the given country
                cases = contentArray[1];
            }
            // Check if the string equals the word "deaths"
            else if(contentArray[0].equals("\"deaths\"")){
                // If the string equals the word "deaths", then get the deaths of the given country
                deaths = contentArray[1];
            }
        }
        // Return the cases and deaths of the given country in json format
        return "{\"cases\":"+cases+",\"deaths\":"+deaths+"}";
    }
}
