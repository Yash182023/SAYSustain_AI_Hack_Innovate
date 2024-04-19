// Define the map container
var map = L.map('map').setView([20.5937, 78.9629], 5);

// Create a tile layer using OpenStreetMap data
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Load the location data from the CSV file
var locations = [
    {
        "Location Name": "Mumbai",
        "Latitude": 19.0760,
        "Longitude": 72.8777,
        "Description": "Located near major highways and railroads. Abundant workforce in the area.",
        "Industry Type": "Manufacturing",
        "Demographic Information": "Population: 12,478,447; Median Income: $20,000",
        "Environmental Factors": "Moderate air quality, coastal city"
    },
    {
        "Location Name": "Delhi",
        "Latitude": 28.7041,
        "Longitude": 77.1025,
        "Description": "Situated in the capital city with access to skilled workforce and tech infrastructure.",
        "Industry Type": "Technology",
        "Demographic Information": "Population: 11,034,555; Median Income: $22,000",
        "Environmental Factors": "Moderate air quality, inland city"
    },
    {
        "Location Name": "Kolkata",
        "Latitude": 22.5726,
        "Longitude": 88.3639,
        "Description": "Adjacent to a major seaport with easy access to global markets.",
        "Industry Type": "Logistics",
        "Demographic Information": "Population: 4,496,694; Median Income: $18,000",
        "Environmental Factors": "Proximity to water, potential water pollution concerns"
    },
    {
        "Location Name": "Chennai",
        "Latitude": 13.0827,
        "Longitude": 80.2707,
        "Description": "Large tracts of open land suitable for agricultural and food processing industries.",
        "Industry Type": "Agriculture",
        "Demographic Information": "Population: 7,088,000; Median Income: $21,000",
        "Environmental Factors": "Moderate air quality, coastal city"
    },
    {
        "Location Name": "Bangalore",
        "Latitude": 12.9716,
        "Longitude": 77.5946,
        "Description": "Hub of technology and innovation. Home to many multinational corporations.",
        "Industry Type": "Technology",
        "Demographic Information": "Population: 8,443,675; Median Income: $25,000",
        "Environmental Factors": "Moderate air quality, temperate climate"
    },
    {
        "Location Name": "Hyderabad",
        "Latitude": 17.3850,
        "Longitude": 78.4867,
        "Description": "Growing IT hub with a strong presence of pharmaceutical and biotechnology industries.",
        "Industry Type": "Technology",
        "Demographic Information": "Population: 6,809,970; Median Income: $23,000",
        "Environmental Factors": "Moderate air quality, inland city"
    },
    {
        "Location Name": "Ahmedabad",
        "Latitude": 23.0225,
        "Longitude": 72.5714,
        "Description": "Major industrial and economic hub in western India.",
        "Industry Type": "Manufacturing",
        "Demographic Information": "Population: 5,570,585; Median Income: $19,000",
        "Environmental Factors": "Moderate air quality, inland city"
    },
    {
        "Location Name": "Pune",
        "Latitude": 18.5204,
        "Longitude": 73.8567,
        "Description": "Education and IT center with a strong automotive and manufacturing presence.",
        "Industry Type": "Technology",
        "Demographic Information": "Population: 3,124,458; Median Income: $24,000",
        "Environmental Factors": "Moderate air quality, inland city"
    }
];

// Add markers for each location
locations.forEach(function(location) {
    var marker = L.marker([location.Latitude, location.Longitude]).addTo(map);
    marker.bindPopup(
        "<b>" + location["Location Name"] + "</b><br>" +
        "<b>Industry Type:</b> " + location["Industry Type"] + "<br>" +
        "<b>Description:</b> " + location["Description"] + "<br>" +
        "<b>Demographic Information:</b> " + location["Demographic Information"] + "<br>" +
        "<b>Environmental Factors:</b> " + location["Environmental Factors"]
    );
});
