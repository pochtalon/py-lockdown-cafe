import datetime

from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine period is over. "
                                       "Update your vaccine.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Damn! Just buy the mask, man!")
        return f"Welcome to {self.name}"
