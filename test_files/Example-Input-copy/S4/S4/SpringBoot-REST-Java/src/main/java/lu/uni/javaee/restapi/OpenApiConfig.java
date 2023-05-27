package lu.uni.javaee.restapi;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.media.NumberSchema;
import io.swagger.v3.oas.models.media.ObjectSchema;
import io.swagger.v3.oas.models.media.StringSchema;
import org.springdoc.core.SpringDocUtils;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("Countries COVID API")
                        .description(
                                "A RESTful API implemented with SpringBoot and Java.")
                        .contact(new Contact().name("Tatiana Lopes")));
    }

    // Add an example to the Schema values with the country name, deaths and cases
    static {
        ObjectSchema schema = (ObjectSchema) new ObjectSchema().addProperty("cases",
        new NumberSchema().example(297757));      
        schema.addProperty("deaths", new NumberSchema().example(1133));
        SpringDocUtils.getConfig().replaceWithSchema(Country.class, schema);
    }
}