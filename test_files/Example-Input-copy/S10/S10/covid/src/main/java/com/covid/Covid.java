package com.covid;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.Locale;
import java.util.Set;

/**
 *
 * @author Marnix Van den Wijngaert
 */

public class Covid {

    private static Locale locale = new Locale("de");
    private static final Set<String> ISO_COUNTRIES = Set.of(locale.getISOCountries());

    public static boolean isValidISOCountry(String s) {
        s = s.toUpperCase();
        for (String iso : ISO_COUNTRIES) {
            if (iso.equals(s)) {
                return true;
            }
        }
        return false;
    }

    public static boolean isValidCountry(String s) {
        s = s.toUpperCase();
        for (String country : ISO_COUNTRIES) {
            Locale obj = new Locale("en", country);
            if (obj.getDisplayCountry().toUpperCase().equals(s)) {
                return true;
            }
        }
        return false;
    }

    public boolean checkCountry(String country) {
        boolean help = false;
        if (isValidCountry(country)) {
            help = true;
        }
        if (isValidISOCountry(country)) {
            help = true;
        }
        return help;
    }

    public JSONObject getCountry(String country) {
        if(!checkCountry(country)) {
            return new JSONObject().put("error", "Invalid country code");
        }

        HttpClient httpClient = HttpClientBuilder.create().build();
        try {
            String url = "https://disease.sh/v3/covid-19/countries/" + country;
            HttpGet request = new HttpGet(url);
            HttpResponse response = httpClient.execute(request);
            HttpEntity entity = response.getEntity();
            String data = EntityUtils.toString(entity, "UTF-8");

            JSONObject js = new JSONObject(data);
            String countryName = js.getString("country");
            int cases = js.getInt("cases");
            int deaths = js.getInt("deaths");

            JSONObject result = new JSONObject();
            result.put("country", countryName);
            result.put("cases", cases);
            result.put("deaths", deaths);

            return result;
        } catch (JSONException | IOException ex) {
            return new JSONObject("{\"error\": \"Country not found\"}");
        }
    }
}
