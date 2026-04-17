# STAGE 1: Build the React application
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# STAGE 2: Serve the app with Apache (The 'A' in LAMP)
FROM httpd:2.4-alpine
COPY --from=build /app/build /usr/local/apache2/htdocs/
EXPOSE 80