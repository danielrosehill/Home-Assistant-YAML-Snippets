# TempAndHumidityGagues

![TempAndHumidityGagues](image.png)

```yaml
square: true
type: grid
cards:
  - type: gauge
    entity: sensor.0xa4c138704b4a7984_temperature
    name: Temperature
    needle: true
    severity:
      green: 0
      yellow: 23
      red: 24
  - type: gauge
    entity: sensor.0xa4c138704b4a7984_humidity
    name: Humidity
    needle: true
    severity:
      green: 0
      yellow: 60
      red: 70
columns: 2

```
