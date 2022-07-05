class Luhn:
    def __init__(self, card_num:str):
        self.card_num = card_num
        pass

    def valid(self):
        card_num = self.card_num

        # symbol check
        for num in card_num:
            if num == " ":
                pass
            elif not num.isdigit():
                return False
        
        clean_card_num = card_num.replace(" ","")

        # lenght check
        if len(clean_card_num) <= 1:
            return False
        
        result = 0
        
        # reverse card_num
        clean_card_num = clean_card_num[::-1]
        
        # algorithm check
        for index,num in enumerate(clean_card_num):
            num = int(num)
            if index % 2 != 0:
                n_double = num*2
                if n_double > 9:
                    n_double -= 9
                result += n_double
            else:
                result += num
        return result % 10 == 0