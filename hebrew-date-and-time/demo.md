# HebrewDateAndTime

![HebrewDateAndTime](image.png)

```yaml
type: grid
columns: 2
square: false
cards:
  - type: custom:button-card
    entity: sensor.hebcal_hebrew_date
    show_name: false
    show_state: true
    show_icon: false
    styles:
      card:
        - background: "linear-gradient(135deg, #4B6CB7 0%, #182848 100%)"
        - border-radius: 15px
        - padding: 16px
      state:
        - color: white
        - font-weight: bold
        - font-size: 18px
        - text-align: center
        - justify-self: center
  - type: custom:button-card
    entity: sensor.time
    show_name: false
    show_state: true
    show_icon: false
    styles:
      card:
        - background: "linear-gradient(135deg, #4B6CB7 0%, #182848 100%)"
        - border-radius: 15px
        - padding: 16px
      state:
        - color: white
        - font-weight: bold
        - font-size: 22px
        - text-align: center
        - justify-self: center

```
