# NextShabbat

![NextShabbat](image.png)

```yaml
type: grid
title: Next Shabbat
titleColor: white
columns: 2
square: false
cards:
  - type: entity
    entity: sensor.hebcal_start_of_shabbat
    name: Shabbat In
    card_mod:
      style: |
        ha-card {
          background: linear-gradient(120deg, #2980b9, #6dd5fa);
          border-radius: 15px;
          padding: 15px;
        }
        .card-content {
          color: white !important;
        }
        .primary {
          font-size: 1.8em;
          font-weight: bold;
          color: white !important;
        }
        .secondary {
          font-size: 1.2em;
          color: white !important;
        }
        :host {
          --primary-text-color: white;
          --secondary-text-color: white;
        }
  - type: entity
    entity: sensor.hebcal_end_of_shabbat
    name: Shabbat Out
    card_mod:
      style: |
        ha-card {
          background: linear-gradient(120deg, #2980b9, #6dd5fa);
          border-radius: 15px;
          padding: 15px;
        }
        .card-content {
          color: white !important;
        }
        .primary {
          font-size: 1.8em;
          font-weight: bold;
          color: white !important;
        }
        .secondary {
          font-size: 1.2em;
          color: white !important;
        }
        :host {
          --primary-text-color: white;
          --secondary-text-color: white;
        }

```
