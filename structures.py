from dataclasses import dataclass


@dataclass
class DailyResult:
    # Meeting results
    success: int
    postponed: int
    refused: int

    # Offers
    invite_friend: int
    transfer_abroad: int
    mobile_bank: int
    debit_card: int
    credit_card: int
    sim_card: int
    investments: int
    junior: int
    subscription: int
    card_protection: int