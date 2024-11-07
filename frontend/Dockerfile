# Step 1: Build the React app
FROM node:18 AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the React app
RUN npm run build

# Step 2: Serve the app with a lightweight web server (e.g., nginx)
FROM nginx:alpine

# Copy the build folder from the previous image to the nginx public folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose the default HTTP port
EXPOSE 80

# Start nginx to serve the app
CMD ["nginx", "-g", "daemon off;"]
