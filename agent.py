def honey_pot_agent(history, last_message):
    replies = [
        "Mujhe thoda samajh nahi aa raha, aap explain kar sakte ho?",
        "Isme bank select karne ko aa raha hai, kaunsa bank choose karu?",
        "Link thoda alag lag raha hai, ye safe hai?",
        "Maine try kiya tha, fail ho gaya. Dobara bhej do.",
        "UPI ID daalu ya account number?"
    ]

    index = len(history) % len(replies)
    return replies[index]

