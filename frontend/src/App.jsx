//import './App.css'
import { useState, useEffect } from 'react';
import WeatherEntries  from './components/weatherEntries';
import WeatherSearch from './components/WeatherSearch';
import WeatherDisplay from './components/WeatherDisplay';

function App() {
  const [weatherEntries, setWeatherEntries] = useState([]);
  const [dataToDisplay, setDataToDisplay] = useState(null);
  const [error, setError] = useState(null);
  
  useEffect(()=>{
    fetchContacts();
  }, [])

  const fetchContacts = async () =>{
    const response = await fetch("http://127.0.0.1:5000/weather_entries");
    const data = await response.json();
    setWeatherEntries(data.weatherEntries);
    console.log(data.weatherEntries);
  }

    // Function to handle API call
  const handleSearch = async (city, country) => {
      const data = {city, country};
      const url = "http://127.0.0.1:5000/new_weather_entry";
      const options = {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify(data)
      };
      try {
        const response = await fetch(url, options);
        const message = await response.json();
        if (response.status !== 201 && response.status !== 200){
          const message = await response.json();
          setError(message)
        } else{
          setDataToDisplay(message);
          setError(null);
        }
      } catch (err) {
        setDataToDisplay(null);
        setError('Error fetching weather data');
      }
      fetchContacts()
    };

  return <>
    <WeatherSearch handleSearch={handleSearch}/>
    <WeatherDisplay weatherData={dataToDisplay} error={error}/>
    <WeatherEntries weatherEntries={weatherEntries} updateCallback={fetchContacts} handleSearch={handleSearch}/>
  </>
}

export default App;
