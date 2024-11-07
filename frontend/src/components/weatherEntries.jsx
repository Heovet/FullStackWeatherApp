import React from "react";
import '../styles/WeatherEntries.css';
import IconButton from 'rsuite/IconButton';
import {Trash} from '@rsuite/icons';
import {Search} from '@rsuite/icons';

const WeatherEntries = ({weatherEntries, updateCallback, handleSearch})=>{
    const onDelete = async (id)=>{
        try{
            const options ={
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_weather_entry/${id}`, options);
            if (response.status === 200){
                updateCallback();
            } else{
                console.error("Failed to delete");
            }
        }
        catch (error){
            alert(error);
        }
    }

    return (<div className="search-history-container">
        <h2>Search History</h2>
        <table className="history-table">
          <thead>
            <tr>
              <th>City</th>
              <th>Country</th>
              <th>Temperature (°C)</th>
              <th>Time</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {weatherEntries.map((weatherEntry) => (
              <tr key={weatherEntry.id}>
                <td>{weatherEntry.city}</td>
                <td>{weatherEntry.country}</td>
                <td>{weatherEntry.temperatureMin}°C - {weatherEntry.temperatureMax}°C</td>
                <td>{weatherEntry.time}</td>
                <td>
                  <IconButton icon={<Search />}
                    className="search-again-btn" 
                    onClick={() => handleSearch(weatherEntry.city, weatherEntry.country)}
                  >
                  </IconButton>
                  <IconButton icon={<Trash />}
                    className="delete-btn" 
                    onClick={() => onDelete(weatherEntry.id)}>
                    </IconButton>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>);};

export default WeatherEntries;