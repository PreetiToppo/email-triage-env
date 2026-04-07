# emails.py — Sample email dataset for the environment

EMAILS = [
    {
        "id": "e001",
        "subject": "URGENT: Server is down, losing $10k/min",
        "body": "Our production server crashed 10 minutes ago. All services are offline. Need immediate help.",
        "sender": "cto@bigcorp.com",
        "label": "urgent",
        "department": "technical",
        "ideal_reply_keywords": ["apology", "escalat", "immediately", "priorit"]
    },
    {
        "id": "e002",
        "subject": "Question about my invoice",
        "body": "Hi, I received invoice #4521 but the amount seems wrong. Can you clarify?",
        "sender": "customer@gmail.com",
        "label": "normal",
        "department": "billing",
        "ideal_reply_keywords": ["invoice", "review", "clarif", "assist"]
    },
    {
        "id": "e003",
        "subject": "You won $1,000,000!!!",
        "body": "Click here to claim your prize. Limited time offer. Act now!",
        "sender": "noreply@prize-winner.xyz",
        "label": "spam",
        "department": "none",
        "ideal_reply_keywords": []
    },
    {
        "id": "e004",
        "subject": "Bug in your API documentation",
        "body": "The code example in your docs for the /auth endpoint is incorrect. The parameter name is wrong.",
        "sender": "dev@startup.io",
        "label": "normal",
        "department": "technical",
        "ideal_reply_keywords": ["thank", "fix", "update", "document"]
    },
    {
        "id": "e005",
        "subject": "URGENT: Payment failed, account suspended",
        "body": "My payment failed and now my account is suspended. I have a live demo in 2 hours. Please help ASAP.",
        "sender": "jane@agency.com",
        "label": "urgent",
        "department": "billing",
        "ideal_reply_keywords": ["apology", "restore", "immediately", "payment"]
    },
    {
        "id": "e006",
        "subject": "Partnership opportunity",
        "body": "We are a marketing agency interested in exploring a partnership with your company.",
        "sender": "bd@marketingco.com",
        "label": "normal",
        "department": "sales",
        "ideal_reply_keywords": ["interest", "discuss", "schedul", "partner"]
    },
]