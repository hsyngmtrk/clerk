"""
from actionstep.api import ActionstepAPI 
api = ActionstepAPI() 
"""
from .filenotes import FilenoteEndpoint
from .users import UserEndpoint
from .actions import ActionEndpoint
from .participants import ParticipantEndpoint
from .files import FileEndpoint

from actionstep.models import AccessToken


class ActionstepAPI:
    """
    Object providing acccess to all Actionstep API endpoints.
    
    """

    def __init__(self):
        access_token = AccessToken.objects.freshest()
        base_url, token = access_token.api_endpoint, access_token.token
        self.filenotes = FilenoteEndpoint(base_url, token)
        self.users = UserEndpoint(base_url, token)
        self.actions = ActionEndpoint(base_url, token)
        self.participants = ParticipantEndpoint(base_url, token)
        self.files = FileEndpoint(base_url, token)

    def __str__(self):
        return self.base_url
