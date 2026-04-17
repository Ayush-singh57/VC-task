# Stage 1: Build the app using Maven
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app

# Copy the pom and source code
COPY pom.xml .
COPY src ./src

# Compile and package the JAR file
RUN mvn clean package -DskipTests

# Stage 2: Run the app using Java Runtime
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]