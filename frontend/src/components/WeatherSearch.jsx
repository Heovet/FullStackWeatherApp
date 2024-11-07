import React, { useState } from 'react';
import '../styles/WeatherSearchAndDisplay.css';

const WeatherSearch = ({ handleSearch }) => {
  const [city, setCity] = useState('');
  const [country, setCountry] = useState('');

  const handleClear = () => {
    setCity('');
    setCountry('');
  };

  return (
    <div className="weather-search-container">
      <h1 className="weather-search-title">Weather Search</h1>
      <form className="weather-search-form" onSubmit={(e) => {
        e.preventDefault();
        handleSearch(city, country);
      }}>
        <div className="input-group">
          <input
            id="city-input"
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter city"
            className="weather-input"
          />
        </div>
        <div className="input-group">
          <input
            id="country-input"
            type="text"
            value={country}
            onChange={(e) => setCountry(e.target.value)}
            placeholder="Enter country"
            className="weather-input"
          />
        </div>
        <div className="button-group">
          <button type="submit" className="search-button">Search</button>
          <button type="button" onClick={handleClear} className="clear-button">Clear</button>
        </div>
      </form>
    </div>
  );
};

export default WeatherSearch;
