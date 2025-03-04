class CreditCard(object):
    """Class for credit card"""

    def __init__(self, card_name, bank_name):
        self.card_name = card_name
        self.bank_name = bank_name

    def __str__(self):
        obj_repr = f"Card: {self.card_name} of {self.bank_name}"
        return obj_repr

if __name__ == "__main__":
    hdfc_card = CreditCard(card_name="Regalia", bank_name="HDFC")
    sbi_card = CreditCard(card_name="Cash Back", bank_name="SBI")
    print(hdfc_card)
    print(sbi_card)