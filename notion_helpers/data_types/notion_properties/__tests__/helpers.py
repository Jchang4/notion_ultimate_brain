from notion_helpers.data_types.notion_properties.property import PropertyTypes

DATABASE_PROPERTY_DATA = {
    PropertyTypes.DATE: {
        "id": "%5ExHo",
        "name": "End time with spaces",
        "type": "date",
        "date": {},
    },
    PropertyTypes.CREATED_TIME: {
        "id": "Izyd",
        "name": "Created time",
        "type": "created_time",
        "created_time": {},
    },
    PropertyTypes.NUMBER: {
        "id": "cHjm",
        "name": "My dummy number",
        "type": "number",
        "number": {"format": "number"},
    },
    PropertyTypes.URL: {
        "id": "jqst",
        "name": "URL",
        "type": "url",
        "url": {},
    },
}

PAGE_PROPERTY_DATA = {
    PropertyTypes.DATE: {
        "id": "M%3BBw",
        "type": "date",
        "date": {"start": "2022-10-14", "end": None, "time_zone": None},
    },
    PropertyTypes.CREATED_TIME: {
        "id": "eB_%7D",
        "object": "property_item",
        "type": "created_time",
        "created_time": "2022-10-12T16:34:00.000Z",
    },
    PropertyTypes.NUMBER: {
        "id": "WPj%5E",
        "object": "property_item",
        "type": "number",
        "number": 42,
    },
    PropertyTypes.URL: {
        "id": "bB%3D%5B",
        "type": "url",
        "url": "https://developers.notion.com/",
    },
}
