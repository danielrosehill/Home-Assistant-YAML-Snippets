# RedAlertStatuses

![RedAlertStatuses](image.png)

```yaml
square: false
type: grid
columns: 2
cards:
  - type: custom:button-card
    entity: binary_sensor.oref_alert_jerusalem_all_areas
    name: Jerusalem All Areas
    icon: mdi:check-circle
    styles:
      card:
        - padding: 12px
      name:
        - font-weight: bold
        - color: white
      state:
        - color: white
      icon:
        - color: white
        - width: 24px
        - height: 24px
    state:
      - value: "on"
        name: Jerusalem All Areas (UNSAFE)
        icon: mdi:alert-octagram
        styles:
          card:
            - background-color: "#ea4335"
          icon:
            - animation: blink 1s ease infinite
      - value: "off"
        name: Jerusalem All Areas (Safe)
        styles:
          card:
            - background-color: "#34a853"
      - value: unavailable
        styles:
          card:
            - background-color: "#ffa500"
  - type: custom:button-card
    entity: binary_sensor.oref_alert
    name: Jerusalem Center
    icon: mdi:check-circle
    styles:
      card:
        - padding: 12px
      name:
        - font-weight: bold
        - color: white
      state:
        - color: white
      icon:
        - color: white
        - width: 24px
        - height: 24px
    state:
      - value: "on"
        name: Jerusalem Center (UNSAFE)
        icon: mdi:alert-octagram
        styles:
          card:
            - background-color: "#ea4335"
          icon:
            - animation: blink 1s ease infinite
      - value: "off"
        name: Jerusalem Center (Safe)
        styles:
          card:
            - background-color: "#34a853"
      - value: unavailable
        styles:
          card:
            - background-color: "#ffa500"
title: Red Alerts

```
