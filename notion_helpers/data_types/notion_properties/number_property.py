from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional, Union

from notion_helpers.data_types.notion_properties.property import Property


class NumberPropertyFormats(str, Enum):
    NUMBER = "number"
    NUMBER_WITH_COMMAS = "number_with_commas"
    PERCENT = "percent"
    DOLLAR = "dollar"
    CANADIAN_DOLLAR = "canadian_dollar"
    EURO = "euro"
    POUND = "pound"
    YEN = "yen"
    RUBLE = "ruble"
    RUPEE = "rupee"
    WON = "won"
    YUAN = "yuan"
    REAL = "real"
    LIRA = "lira"
    RUPIAH = "rupiah"
    FRANC = "franc"
    HONG_KONG_DOLLAR = "hong_kong_dollar"
    NEW_ZEALAND_DOLLAR = "new_zealand_dollar"
    KRONA = "krona"
    NORWEGIAN_KRONE = "norwegian_krone"
    MEXICAN_PESO = "mexican_peso"
    RAND = "rand"
    NEW_TAIWAN_DOLLAR = "new_taiwan_dollar"
    DANISH_KRONE = "danish_krone"
    ZLOTY = "zloty"
    BAHT = "baht"
    FORINT = "forint"
    KORUNA = "koruna"
    SHEKEL = "shekel"
    CHILEAN_PESO = "chilean_peso"
    PHILIPPINE_PESO = "philippine_peso"
    DIRHAM = "dirham"
    COLOMBIAN_PESO = "colombian_peso"
    RIYAL = "riyal"
    RINGGIT = "ringgit"
    LEU = "leu"
    ARGENTINE_PESO = "argentine_peso"
    URUGUAYAN_PESO = "uruguayan_peso"
    SINGAPORE_DOLLAR = "singapore_dollar"


@dataclass
class NumberPropertyValue:
    format: Optional[str] = None
    value: Optional[float] = None


class NumberProperty(Property):
    value: NumberPropertyValue

    def get_value(self, payload: Union[Dict[str, Any], str]) -> NumberPropertyValue:
        prop_value = NumberPropertyValue()

        if type(payload) is dict:
            prop_value.format = payload["format"]
        elif type(payload) is int or type(payload) is float:
            prop_value.value = payload

        return prop_value

    def __repr__(self) -> str:
        return super().__repr__(f'value="{self.value.value}"')
