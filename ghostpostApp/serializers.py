from rest_framework import serializers

from ghostpostApp.models import ghostpost


class GhostpostSerializer(serializers.ModelSerializer):
    
    vote_score = serializers.SerializerMethodField(read_only=True)
    
    def vote_score(self, ghostpost):
        self.vote_score

    # sorted(models.ghostpost.objects.all(), key=lambda x: x.vote_score, reverse=True)

    class Meta:
        model = ghostpost
        fields = [
            'id',
            'ghostpost_choice',
            'ghostpost_content',
            'upvotes',
            'downvotes',
            'vote_score',
            'creation_date',
            'updated'
            ]