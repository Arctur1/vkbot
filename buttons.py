import json

BUTTONS_GET_CITY = json.dumps({
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "Да",
          "payload": ""
        },
        "color": "positive"
      }
    ],
    [
      {
        "action": {
          "type": "text",
          "label": "Нет",
          "payload": ""
        },
        "color": "negative"
      }
    ]
  ]
})

BUTTONS_SEX = json.dumps({
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "Мужской",
          "payload": ""
        },
        "color": "primary"
      },
      {
        "action": {
          "type": "text",
          "label": "Женский",
          "payload": ""
        },
        "color": "secondary"
      }
    ]
  ]
})