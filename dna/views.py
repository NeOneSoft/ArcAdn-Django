from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from dna.models import Dna
from dna.serializers import DnaSerializer


class DnaViewSet(viewsets.ModelViewSet):
    """
    POST/mutation endpoint
    """

    queryset = Dna.objects.all()
    serializer_class = DnaSerializer

    # Declare constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],  # Define all 8 possible directions
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def hasMutation(self, dna, row, col, word):

        # If first character of adn string doesn't match
        # with the given starting position in 2DArray[][].
        if dna[row][col] != word[0]:
            return False

        # Search adn in all 8 directions
        # starting from (row, col)
        for x, y in self.dir:

            # Initialize starting position
            # for current direction
            rd, cd = row + x, col + y
            flag = True

            # First character is already checked,
            # match remaining characters
            for k in range(1, len(word)):

                # If out of bound or not matched, break
                if (0 <= rd < self.R and
                        0 <= cd < self.C and
                        word[k] == dna[rd][cd]):

                    # Moving in particular direction
                    rd += x
                    cd += y
                else:
                    flag = False
                    break

            # If all character matched, then
            # value of flag must be false
            if flag:
                return True
        return False

    @action(detail=True, methods=['GET'])
    def statics(self, request, pk=None):
        counter_mut = 0
        counter_notmut = 0
        dna = self.get_object()
        dna = dna.dna
        mut_seq = ['AAAA', 'GGGG', 'CCCC', 'TTTT']
        for i in mut_seq:
            word = i
            # Rows and columns in given grid
            self.R = len(dna)
            self.C = len(dna[0])

            # Consider every position as starting point
            # and search given adn
            for row in range(self.R):
                for col in range(self.C):
                    if self.hasMutation(dna, row, col, word):
                        counter_mut += 1
            counter_notmut += 1
        ratio = counter_mut / counter_notmut
        return Response({"count_mutations": counter_mut,
                         "count_no_mutation": counter_notmut,
                         "ratio": ratio
                         })

    @action(detail=True, methods=['GET'])
    def dna(self, request, pk=None):
        dna = self.get_object()
        dna = dna.dna
        mut_seq = ['AAAA', 'GGGG', 'CCCC', 'TTTT']
        for i in mut_seq:
            word = i
            # Rows and columns in given grid
            self.R = len(dna)
            self.C = len(dna[0])

            # Consider every position as starting point
            # and search given adn
            for row in range(self.R):
                for col in range(self.C):
                    if self.hasMutation(dna, row, col, word):
                        return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
