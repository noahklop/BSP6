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

public class Covid {

    public Covid() {
    }

    public String getCountry(String country) {

        HttpClient httpClient = HttpClientBuilder.create().build();
        try {
            String url = "https://disease.sh/v3/covid-19/countries/" + country;
            HttpGet request = new HttpGet(url);
            HttpResponse response = httpClient.execute(request);
            HttpEntity entity = response.getEntity();
            String data = EntityUtils.toString(entity, "UTF-8");
            System.out.println(data);
            JSONObject js = new JSONObject(data);
            //JSONArray array = new JSONArray(data);
            System.out.println("Country:" + country);
            String countryName = js.getString("country");
            int cases = js.getInt("cases");
            int deaths = js.getInt("deaths");
            return "Country: " + countryName + " Cases: " + cases + " Deaths: " + deaths;
        } catch (JSONException | IOException | UnsupportedOperationException ex) {
            return "Country not found!";
        }
        /*try {
            URL url = new URL("https://disease.sh/v3/covid-19/countries/" + country);
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("User-Agent", "Mozilla/5.0");
            int responseCode = con.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) { // success
                BufferedReader in = new BufferedReader(new InputStreamReader(
                        con.getInputStream()));
                String inputLine;
                StringBuffer response = new StringBuffer();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();

                return response.toString();
            } else {
                return "GET request not worked";
            }
        } catch (IOException e) {
            return "Country not found!";
        }*/
    }
}
