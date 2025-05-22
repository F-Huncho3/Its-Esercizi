def find_disappeared_numbers(nums: list[int]) -> list[int]:


    lista_mancanti:list = []

    for i in range(1,len(nums) + 1):

        if i not in nums:

            lista_mancanti.append(i)

    return lista_mancanti









