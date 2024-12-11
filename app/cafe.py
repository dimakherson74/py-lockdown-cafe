from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expired vaccine")

        if (visitor["wearing_a_mask"] is False
                or "wearing_a_mask" not in visitor):
            raise NotWearingMaskError("Visitor without mask")

        return f"Welcome to {self.name}"
