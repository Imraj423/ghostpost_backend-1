from rest_framework.serializers import ModelSerializer

from api.models import GhostPost


class GhostPostSerializer(ModelSerializer):
    class Meta:
        model = GhostPost
        fields = (
            'id',
            'boast',
            'roast',
            'post_input',
            'up_vote',
            'down_vote',
            'sum_of_votes',
            'date',
        )