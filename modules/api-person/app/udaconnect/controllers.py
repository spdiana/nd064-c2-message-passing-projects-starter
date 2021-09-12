from app.udaconnect.models import Person
from app.udaconnect.schemas import (
    PersonSchema
)
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling

@api.route("/persons")
@api.route("/persons/<person_id>")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> Person:
        person_id = request.args.get('person_id')
        if person_id:
            person: Person = PersonService.retrieve(person_id)
            persons: list = [person]
            return persons
        else:
            persons: List[Person] = PersonService.retrieve_all()
            return persons














