# ActiveLights

![ActiveLights](image.png)

```yaml
type: custom:auto-entities
filter:
  include:
    - domain: light
      state: "on"
show_empty: false
card:
  show_name: true
  show_icon: true
  show_state: false
  type: glance
  columns: 4
  state_color: true
  title: Active Lights
  card_mod:
    style: |
      ha-card {
        background: var(--card-background-color, var(--ha-card-background));
        border-radius: 12px;
        padding: 12px;
        margin-top: 10px;
        margin-bottom: 10px;
      }
      .header {
        font-weight: bold;
        padding: 8px 16px;
        color: var(--primary-text-color);
      }
      .name {
        font-size: 14px;
      }
      ha-card .entity {
        background: rgba(var(--rgb-primary-color), 0.05);
        border-radius: 12px;
        margin: 4px;
        padding: 8px;
        border: 1px solid rgba(var(--rgb-primary-color), 0.1);
      }
      ha-card .entity:hover {
        background: rgba(var(--rgb-primary-color), 0.1);
        transform: scale(1.02);
        transition: all 0.2s ease-in-out;
      }
sort:
  method: none
  reverse: false

```
