from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dixit.serializers import PlayerSerializer
import redis
import pickle


class CurrentUserView(APIView):

    def get(self, request):
        serializer = PlayerSerializer(request.user)
        return Response(serializer.data)

class GameParticipantsView(APIView):

    def get(self, request, *args, **kwargs):
        redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)
        print(kwargs['game_id'])
        game =redis_db.get(kwargs['game_id'])
        print(game)
        if game is not None:
            game =  pickle.loads(game)
            participants = game.get_participants()

            found = False
            for p in participants:
                if p==request.user:
                    found=True
                    break
            # if not found:
            #     return Response(status=status.HTTP_401_UNAUTHORIZED)
            results = [PlayerSerializer(participant).data for participant in participants]
            return Response(results)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

