from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema
)
from app.udaconnect.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        payload = request.get_json()
        new_location: Location = LocationService.create(payload)
        return new_location

    @responds(schema=LocationSchema, many=True)
    def get(self) -> Location:
        loc_id = request.args.get('location_id')
        if loc_id:
            location: Location = LocationService.retrieve(loc_id)
            locations: list = [location]
            return locations
        else:
            location: List[Location] = LocationService.retrieve_all()
            return location







