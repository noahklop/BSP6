package uni.lu.restfulAPI;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class JavaeeSpringbootRestfulAPI {
    public static void main(String[] args) {
        SpringApplication.run(
                JavaeeSpringbootRestfulAPI.class, args);
    }
}
