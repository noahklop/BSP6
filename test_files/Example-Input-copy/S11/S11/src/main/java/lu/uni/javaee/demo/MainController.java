package lu.uni.javaee.demo;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.validation.constraints.NotBlank;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class MainController {
    @Operation(summary = "Get data for a country")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Valid country code",
                    content = { @Content(mediaType = "application/json") }),
            @ApiResponse(responseCode = "422", description = "Invalid input",
                    content = @Content)
    })
    @NotBlank(message = "Country code is required")
    @GetMapping(value = "/exercise4", produces = "application/json")
    public ResponseEntity<String> getDataOnParam(@RequestParam(value="countryCode") String countryCode) {
        return getFromConnector(countryCode);
    }

    @Operation(summary = "Get data for a country")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Valid country code",
                    content = { @Content(mediaType = "application/json") }),
            @ApiResponse(responseCode = "422", description = "Invalid input",
                    content = @Content)
    })
    @NotBlank(message = "Country code is required")
    @GetMapping(value = "/exercise4/{country}", produces = "application/json")
    public ResponseEntity<String> getDataOnPath(@PathVariable(value="country") String countryCode) {
        return getFromConnector(countryCode);
    }

    private ResponseEntity<String> getFromConnector(String countryCode) {
        if (countryCode != null  && (countryCode.length() == 2 || countryCode.length() > 3)) {
            return new CovidConnector().getDataForCountry(countryCode);
        }
        return ResponseEntity.status(422).body("{\"error\":\"Invalid input\"}");
    }
}