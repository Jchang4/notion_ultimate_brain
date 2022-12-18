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
    PropertyTypes.RELATION: {
        "Goal": {
            "id": "%5B%3BNK",
            "name": "Goal",
            "type": "relation",
            "relation": {
                "database_id": "a8d444de-8bfa-4127-90b7-ad92485ad1b5",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Projects",
                    "synced_property_id": "%5BVBy",
                },
            },
        },
        "Pulled Resources": {
            "id": "_P%3EW",
            "name": "Pulled Resources",
            "type": "relation",
            "relation": {
                "database_id": "fdfd8fed-07cb-469b-8598-904921940785",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Pulls",
                    "synced_property_id": "q%3DnZ",
                },
            },
        },
        "Tasks": {
            "id": "fyxc",
            "name": "Tasks",
            "type": "relation",
            "relation": {
                "database_id": "76117a77-b95c-4dde-910c-18dfd4210cd2",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Project",
                    "synced_property_id": "a~%7Cl",
                },
            },
        },
        "Area": {
            "id": "lnvs",
            "name": "Area",
            "type": "relation",
            "relation": {
                "database_id": "fdfd8fed-07cb-469b-8598-904921940785",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Projects",
                    "synced_property_id": "WjLi",
                },
            },
        },
        "Notes": {
            "id": "pVgn",
            "name": "Notes",
            "type": "relation",
            "relation": {
                "database_id": "ff1483e0-2ed6-4931-9aeb-71bf1fbd8e24",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Project",
                    "synced_property_id": "%7CUS%7C",
                },
            },
        },
        "Pulled Notes": {
            "id": "ptmt",
            "name": "Pulled Notes",
            "type": "relation",
            "relation": {
                "database_id": "ff1483e0-2ed6-4931-9aeb-71bf1fbd8e24",
                "type": "dual_property",
                "dual_property": {
                    "synced_property_name": "Pulls",
                    "synced_property_id": "RmO%3B",
                },
            },
        },
    },
    PropertyTypes.ROLLUP: {
        "Root Area": {
            "id": "i%7CfO",
            "name": "Root Area",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Root Area",
                "relation_property_name": "Area/Resource",
                "rollup_property_id": "ETg>",
                "relation_property_id": "h>gC",
                "function": "show_original",
            },
        },
        "Resource Pulls": {
            "id": "pXKR",
            "name": "Resource Pulls",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Pulls",
                "relation_property_name": "Area/Resource",
                "rollup_property_id": "q=nZ",
                "relation_property_id": "h>gC",
                "function": "show_original",
            },
        },
        "Project Archived": {
            "id": "qF%5BV",
            "name": "Project Archived",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Archived",
                "relation_property_name": "Project",
                "rollup_property_id": "Giws",
                "relation_property_id": "|US|",
                "function": "show_original",
            },
        },
        "Project Area": {
            "id": "p%5Dy%5D",
            "name": "Project Area",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Area",
                "relation_property_name": "Project",
                "rollup_property_id": "lnvs",
                "relation_property_id": "a~|l",
                "function": "show_original",
            },
        },
        "Goal Area": {
            "id": "OUg%7D",
            "name": "Goal Area",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Area",
                "relation_property_name": "Goal",
                "rollup_property_id": "vY;v",
                "relation_property_id": "[;NK",
                "function": "show_original",
            },
        },
        "Overdue Tasks": {
            "id": "BkqU",
            "name": "Overdue Tasks",
            "type": "rollup",
            "rollup": {
                "rollup_property_name": "Late",
                "relation_property_name": "Tasks",
                "rollup_property_id": "aG|O",
                "relation_property_id": "fyxc",
                "function": "not_empty",
            },
        },
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
    PropertyTypes.RELATION: {
        "Goal": {
            "id": "%5B%3BNK",
            "type": "relation",
            "relation": [],
            "has_more": False,
        },
        "Area": {
            "id": "lnvs",
            "type": "relation",
            "relation": [{"id": "88907c19-0192-4c23-98f5-20694246e97d"}],
            "has_more": False,
        },
        "Tasks": {
            "id": "fyxc",
            "type": "relation",
            "relation": [
                {"id": "d173c4b3-4659-4acc-9176-236aadd897cd"},
                {"id": "8f17ef75-3f10-4f16-ba49-8a9984a14933"},
                {"id": "c8da872c-fffa-4e47-bdf4-771b1e982f2e"},
                {"id": "23a8f857-b9c6-4e15-b8ac-4e4fa13bed62"},
                {"id": "e4fe6252-c9fb-440c-b20a-6e2158ed1955"},
            ],
            "has_more": False,
        },
        "Pulled Resources": {
            "id": "_P%3EW",
            "type": "relation",
            "relation": [
                {"id": "a45a591e-5111-4f38-a0ab-ec037f3c8a2d"},
                {"id": "3cdbfd5a-e7eb-493a-b991-44d1ee35396d"},
            ],
            "has_more": False,
        },
        "Notes": {
            "id": "pVgn",
            "type": "relation",
            "relation": [
                {"id": "e5c05e0f-bff2-4c37-98f0-cc9b04cfb8fc"},
                {"id": "e8c9307f-5ace-4a7a-9687-83b8f784849e"},
                {"id": "84a19c9c-3f2f-43fd-8241-2f57c46f531d"},
            ],
            "has_more": False,
        },
    },
    PropertyTypes.ROLLUP: {
        "Overdue Tasks": {
            "id": "BkqU",
            "type": "rollup",
            "rollup": {"type": "number", "number": 0, "function": "not_empty"},
        },
        "Goal Area": {
            "id": "OUg%7D",
            "type": "rollup",
            "rollup": {"type": "array", "array": [], "function": "show_original"},
        },
        "Project Tasks": {
            "id": "u%3Ff%3A",
            "type": "rollup",
            "rollup": {"type": "number", "number": 0, "function": "unchecked"},
        },
        "Tasks Done": {
            "id": "vRV%40",
            "type": "rollup",
            "rollup": {"type": "number", "number": 1, "function": "percent_checked"},
        },
    },
}
