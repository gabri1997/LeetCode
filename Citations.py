"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.
"""

def hIndex(citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)  # Ordiniamo le citazioni in ordine decrescente
        h_index = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index

if __name__ == '__main__':
        
        citations = [3,0,6,1,5,5,5]
        h_index = hIndex(citations)
        print(h_index)