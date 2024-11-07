import React from 'react';
import '../styles/WeatherSearchAndDisplay.css';

const WeatherDisplay = ({ weatherData, error }) => {
  return (
    <div className="weather-display-container">
      {error && <p className="error-message">{error}</p>}
      
      {weatherData ? (
        <div className="weather-details">
          <h2>Weather Data</h2>
          <div className="weather-info">
            <p><strong>Location:</strong> {`${weatherData.city}, ${weatherData.country}`}</p>
            <p><strong>Temperature:</strong> {`${weatherData.temperatureMin}°C - ${weatherData.temperatureMax}°C`}</p>
            <p><strong>Humidity:</strong> {`${weatherData.humidity}%`}</p>
            <p><strong>Time:</strong> {weatherData.time}</p>
          </div>
        </div>
      ) : (
        <p className="no-data-message">No weather data available. Please search for a location.</p>
      )}
    </div>
  );
};

export default WeatherDisplay;
