const form = document.getElementById('converter-form');
const temperatureInput = document.getElementById('temperature');
const unitSelect = document.getElementById('unit');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const temperature = parseFloat(temperatureInput.value);
    const unit = unitSelect.value;

    if (isNaN(temperature)) {
        resultDiv.textContent = 'Please enter a valid temperature.';
        return;
    }

    let convertedTemperature;
    let convertedUnit;

    if (unit === 'celsius') {
        convertedTemperature = (temperature * 9/5) + 32;
        convertedUnit = 'Fahrenheit';
    } else {
        convertedTemperature = (temperature - 32) * 5/9;
        convertedUnit = 'Celsius';
    }

    resultDiv.textContent = `Converted Temperature: ${convertedTemperature.toFixed(2)} ${convertedUnit}`;
});
