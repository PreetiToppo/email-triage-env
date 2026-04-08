# emails.py — 50+ realistic emails across industries, tones, urgency levels

EMAILS = [
    # URGENT - Technical
    {
        "id": "e001",
        "subject": "URGENT: Production database down - all services offline",
        "body": "Our entire production database cluster crashed 15 minutes ago. All customer-facing services are down. We're losing approximately $50,000 per minute. Need immediate escalation to your senior engineering team.",
        "sender": "cto@fintech-startup.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "escalat", "immediately", "priorit", "engineer"]
    },
    {
        "id": "e002",
        "subject": "Critical security breach detected",
        "body": "Our security monitoring system has detected unauthorized access to customer data. Approximately 10,000 user records may have been compromised. This happened 30 minutes ago and is ongoing.",
        "sender": "security@enterprise-corp.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "escalat", "security", "immediately", "team"]
    },
    {
        "id": "e003",
        "subject": "API rate limits causing complete service failure",
        "body": "Your API is returning 429 errors for ALL our requests since 2 hours ago. We have a major client demo in 45 minutes and our entire product is non-functional. This is a business emergency.",
        "sender": "dev@saas-company.io",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "limit", "immediately", "resolv", "engineer"]
    },
    {
        "id": "e004",
        "subject": "CRITICAL: Payment processing completely broken",
        "body": "None of our customers can complete purchases. The checkout page shows a server error on every transaction attempt. This started exactly 1 hour ago. We've already lost 200+ failed transactions.",
        "sender": "ops@ecommerce-brand.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "payment", "immediately", "fix", "team"]
    },
    # URGENT - Billing
    {
        "id": "e005",
        "subject": "Account suspended - live client presentation in 1 hour",
        "body": "My account has been suspended due to a payment failure but I have a live demo with a Fortune 500 client in 60 minutes. I've already updated my card details. Please restore access IMMEDIATELY.",
        "sender": "jane.smith@agency.co",
        "label": "urgent",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["apolog", "restor", "immediately", "payment", "account"]
    },
    {
        "id": "e006",
        "subject": "Double charged $4,999 - need immediate refund",
        "body": "I was charged twice for my annual enterprise subscription. $4,999 x2 = $9,998 has been deducted from our company account. This is causing cash flow issues. Need this resolved TODAY.",
        "sender": "finance@mid-size-company.com",
        "label": "urgent",
        "department": "billing",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "refund", "immediately", "charg", "resolv"]
    },
    # NORMAL - Technical
    {
        "id": "e007",
        "subject": "Bug in your API documentation - wrong parameter name",
        "body": "Hi team, the code example in your /auth endpoint documentation uses 'api_token' but the actual parameter name is 'access_token'. This caused me 2 hours of debugging. Please fix the docs.",
        "sender": "dev@startup.io",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["thank", "fix", "update", "document", "report"]
    },
    {
        "id": "e008",
        "subject": "Feature request: webhook retry logic",
        "body": "It would be really helpful if your webhooks had automatic retry logic with exponential backoff. Currently if our server is temporarily down, we lose webhook events entirely.",
        "sender": "engineer@techco.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["thank", "feedback", "featur", "consider", "roadmap"]
    },
    {
        "id": "e009",
        "subject": "SDK throwing null pointer exception on iOS 17",
        "body": "Your iOS SDK version 3.2.1 is throwing a null pointer exception when calling the initialize() method on iOS 17 devices. Works fine on iOS 16. Stack trace attached.",
        "sender": "ios-dev@mobileapp.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["thank", "bug", "investig", "fix", "version"]
    },
    {
        "id": "e010",
        "subject": "How do I export data to CSV?",
        "body": "I've been looking through the documentation but can't find how to export my analytics data to CSV format. Is this feature available? If so, where can I find it?",
        "sender": "user@smallbiz.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["export", "csv", "setting", "help", "step"]
    },
    {
        "id": "e011",
        "subject": "Integration with Salesforce not syncing",
        "body": "We set up the Salesforce integration last week but contacts aren't syncing properly. New contacts created in Salesforce don't appear in your system even after 24 hours.",
        "sender": "admin@sales-team.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["sync", "integrat", "check", "configur", "help"]
    },
    # NORMAL - Billing
    {
        "id": "e012",
        "subject": "Question about my invoice #4521",
        "body": "Hi, I received invoice #4521 for $299 but I thought my plan was $199/month. Can you clarify what the additional $100 charge is for?",
        "sender": "customer@gmail.com",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["invoice", "charg", "clarif", "plan", "explain"]
    },
    {
        "id": "e013",
        "subject": "Can I upgrade mid-cycle?",
        "body": "I'm currently on the Starter plan and want to upgrade to Professional. If I upgrade now, will I be charged the full amount or prorated for the remaining days in my billing cycle?",
        "sender": "user@freelancer.me",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["upgrad", "prorat", "biling", "plan", "charg"]
    },
    {
        "id": "e014",
        "subject": "Need invoice for tax purposes",
        "body": "Hi, I need a detailed invoice for all payments made in 2023 for our tax filing. Can you send me a consolidated invoice or provide a way to download all past invoices?",
        "sender": "accounting@company.org",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["invoic", "download", "histor", "payment", "tax"]
    },
    # NORMAL - Sales
    {
        "id": "e015",
        "subject": "Interested in enterprise plan for 500 users",
        "body": "We're a mid-sized company looking to roll out your platform to our entire sales team of 500 people. Can you share enterprise pricing and whether you offer volume discounts?",
        "sender": "procurement@bigcompany.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["enterpris", "pric", "discount", "schedul", "demo"]
    },
    {
        "id": "e016",
        "subject": "Partnership opportunity - 50k user base",
        "body": "We run a complementary SaaS platform with 50,000 users and believe there's a strong integration opportunity between our products. Would love to explore a partnership.",
        "sender": "bd@partnerco.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["partner", "integrat", "discuss", "schedul", "opportunit"]
    },
    {
        "id": "e017",
        "subject": "Requesting a demo for our team",
        "body": "Our team of 8 is evaluating project management tools and your product looks promising. Could we schedule a 30-minute demo this week? We're available Tuesday or Thursday afternoon.",
        "sender": "manager@consultancy.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["demo", "schedul", "tuesday", "thursday", "team"]
    },
    # SPAM
    {
        "id": "e018",
        "subject": "You've won $1,000,000!!!",
        "body": "Congratulations! You've been selected as our lucky winner. Click here to claim your prize of $1,000,000. Limited time offer. Act now before it expires!",
        "sender": "noreply@prize-winner.xyz",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e019",
        "subject": "Increase your revenue by 10000% guaranteed",
        "body": "Dear Business Owner, our proven system guarantees 10000% revenue increase in 30 days or your money back. Buy our course now at 90% discount. Only 3 spots left!",
        "sender": "guru@getrichfast.biz",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e020",
        "subject": "Your account has been compromised - verify now",
        "body": "ALERT: Suspicious activity detected on your account. Click the link below immediately to verify your identity and prevent account suspension: http://verify-account-now.suspicious.com",
        "sender": "security-alert@phishing-site.ru",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e021",
        "subject": "Buy cheap Rx medications no prescription needed",
        "body": "Get all your medications at 80% off retail price. No prescription required. Worldwide shipping. Discreet packaging. Order now and get free delivery.",
        "sender": "pills@cheapmeds.cn",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e022",
        "subject": "SEO services - rank #1 on Google guaranteed",
        "body": "We guarantee your website will rank #1 on Google within 30 days using our proprietary black-hat SEO techniques. 100% money back guarantee. Reply YES to get started.",
        "sender": "seo@rankfast.spam",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    # More NORMAL - Technical (edge cases)
    {
        "id": "e023",
        "subject": "Performance degradation on large datasets",
        "body": "When processing datasets larger than 100MB, your tool takes 45+ minutes which makes it unusable for our workflows. Is there a way to optimize this or is this a known limitation?",
        "sender": "dataeng@analytics-firm.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["perform", "optim", "dataset", "limit", "help"]
    },
    {
        "id": "e024",
        "subject": "GDPR data deletion request",
        "body": "As per GDPR Article 17, I am requesting complete deletion of all my personal data from your systems within 30 days. Please confirm receipt and provide a timeline.",
        "sender": "citizen@eu-country.de",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["gdpr", "delet", "confirm", "30 day", "compli"]
    },
    {
        "id": "e025",
        "subject": "Two-factor authentication not working",
        "body": "I've enabled 2FA on my account but the codes from my authenticator app are always rejected. I've already re-synced the time on my phone. Still not working.",
        "sender": "secureuser@privateemail.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["2fa", "authent", "reset", "help", "code"]
    },
    {
        "id": "e026",
        "subject": "White label options for our agency",
        "body": "We're a digital agency managing 30+ client accounts. Do you offer white-label options so we can present your platform under our own branding to clients?",
        "sender": "director@digitalagency.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["white label", "brand", "agenc", "plan", "discuss"]
    },
    {
        "id": "e027",
        "subject": "Cancellation request - moving to competitor",
        "body": "I'd like to cancel my subscription. We've decided to move to a competitor product. Please cancel immediately and confirm no further charges will be made.",
        "sender": "user@churning.com",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["cancel", "confirm", "charg", "sorr", "feedback"]
    },
    {
        "id": "e028",
        "subject": "Wrong timezone on scheduled reports",
        "body": "All my scheduled reports are being sent at the wrong time. I've set my timezone to IST (UTC+5:30) in settings but reports still arrive in UTC. Please fix this.",
        "sender": "analyst@india-company.in",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["timezone", "schedul", "report", "setting", "fix"]
    },
    {
        "id": "e029",
        "subject": "Non-profit discount application",
        "body": "We are a registered 501(c)(3) non-profit organization. Your website mentions a 50% non-profit discount. I'd like to apply for this discount for our upcoming renewal.",
        "sender": "admin@nonprofit.org",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["nonprofit", "discount", "verif", "appl", "renew"]
    },
    {
        "id": "e030",
        "subject": "URGENT: Data corruption after your last update",
        "body": "After applying your system update released yesterday, we're seeing data corruption in our exports. Historical records from 2022 are showing incorrect values. This is affecting our compliance reporting.",
        "sender": "compliance@financial-firm.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "escalat", "corrupt", "revert", "priorit"]
    },
    {
        "id": "e031",
        "subject": "Bulk import failing silently",
        "body": "When I try to import a CSV with more than 5,000 rows, the system says 'Import complete' but only 500 records appear. No error message. The other 4,500 records vanish silently.",
        "sender": "ops@growing-startup.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["import", "limit", "bug", "investig", "fix"]
    },
    {
        "id": "e032",
        "subject": "Accessibility issues with screen reader",
        "body": "Your web application is not accessible via screen readers. As a visually impaired user, I'm unable to navigate the dashboard. This may also be a legal compliance issue for your company.",
        "sender": "accessibility@disability-advocate.org",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["accessibl", "screen reader", "priorit", "fix", "compli"]
    },
    {
        "id": "e033",
        "subject": "Want to interview your team for our podcast",
        "body": "Hi! I host a tech podcast with 200,000 monthly listeners. I'd love to interview someone from your leadership team about AI and the future of work. Would anyone be interested?",
        "sender": "host@techpodcast.fm",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["podcast", "interest", "forward", "schedul", "team"]
    },
    {
        "id": "e034",
        "subject": "RE: RE: RE: Still waiting for response - 2 weeks",
        "body": "This is my fourth email. I reported a critical bug 2 weeks ago and have received zero response. Ticket #8821. If I don't hear back today I'll be disputing the charge with my bank.",
        "sender": "frustrated@longtime-customer.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "delay", "priorit", "ticket", "resolv"]
    },
    {
        "id": "e035",
        "subject": "Make money online - work from home",
        "body": "Earn $5000 per week working from home just 2 hours per day! No experience required. Join our proven system today. 10,000 people already making money. Click now!",
        "sender": "opportunity@workfromhome-scam.com",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e036",
        "subject": "Contract renewal discussion",
        "body": "Our annual contract expires in 45 days. We're happy with the service overall but would like to discuss pricing before renewing. Can we schedule a call with your account management team?",
        "sender": "cfo@enterprise-client.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["renew", "schedul", "pric", "account", "discuss"]
    },
    {
        "id": "e037",
        "subject": "Student discount available?",
        "body": "Hi, I'm a computer science student at MIT working on my thesis. Do you offer student discounts or academic licenses? I'd love to use your platform for my research.",
        "sender": "student@mit.edu",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["student", "discount", "academ", "verif", "plan"]
    },
    {
        "id": "e038",
        "subject": "URGENT: Wrong data shown to wrong customers",
        "body": "We've just discovered that some customers are seeing other customers' private data in their dashboards. This is a major privacy breach. At least 50 customers are affected. Happening RIGHT NOW.",
        "sender": "ceo@affected-company.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "escalat", "privacy", "immediately", "isolat"]
    },
    {
        "id": "e039",
        "subject": "Congratulations - you've been pre-approved",
        "body": "Dear valued customer, you've been pre-approved for a $50,000 business loan at 2.9% APR. No credit check required. Funds deposited in 24 hours. Apply now at our secure website.",
        "sender": "loans@instant-approve.net",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e040",
        "subject": "Custom SSO integration needed",
        "body": "We're an enterprise customer on the Business plan and need to integrate your system with our existing Okta SSO setup. Our IT team is ready to implement. Who should we coordinate with?",
        "sender": "it-admin@large-enterprise.com",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["sso", "okta", "integrat", "it", "configur"]
    },
    {
        "id": "e041",
        "subject": "Refund request - product not as described",
        "body": "I purchased the annual plan based on your website saying it includes 'unlimited API calls' but I've now hit a 10,000 call/month limit. This is misleading advertising. I want a full refund.",
        "sender": "unhappy@customer.net",
        "label": "normal",
        "department": "billing",
        "needs_escalation": False,
        "ideal_reply_keywords": ["refund", "apolog", "limit", "clarif", "resolv"]
    },
    {
        "id": "e042",
        "subject": "URGENT: Ransomware detected on our systems",
        "body": "Our IT team has detected ransomware that appears to have entered through your third-party integration. All files are encrypted. We are shutting down the integration immediately. Need your security team on a call NOW.",
        "sender": "it@victim-company.com",
        "label": "urgent",
        "department": "technical",
        "needs_escalation": True,
        "ideal_reply_keywords": ["escalat", "security", "immediately", "team", "call"]
    },
    {
        "id": "e043",
        "subject": "Translation needed - Spanish support",
        "body": "Hola, soy un usuario de México y tengo problemas con mi cuenta. No puedo acceder a mis datos de los últimos 3 meses. ¿Pueden ayudarme? (I cannot access my last 3 months of data.)",
        "sender": "usuario@mexico.mx",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["access", "data", "help", "account", "assist"]
    },
    {
        "id": "e044",
        "subject": "Charity fundraiser - seeking sponsorship",
        "body": "We are organizing a charity run for cancer research and are seeking corporate sponsors. Would your company be interested in sponsoring our event at the $5,000 gold tier level?",
        "sender": "fundraising@charity-run.org",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["sponsor", "charit", "forward", "discuss", "team"]
    },
    {
        "id": "e045",
        "subject": "Your free trial expires tomorrow",
        "body": "I notice my free trial expires tomorrow. I'm very interested in continuing but the pricing page is confusing. Can someone walk me through which plan is right for a 3-person startup?",
        "sender": "founder@new-startup.co",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["trial", "plan", "startup", "schedul", "recommend"]
    },
    {
        "id": "e046",
        "subject": "Data residency requirements - EU",
        "body": "We are a European company and our legal team requires that all customer data must be stored within the EU. Can you confirm your data residency options and provide documentation for our compliance team?",
        "sender": "legal@eu-company.eu",
        "label": "normal",
        "department": "technical",
        "needs_escalation": False,
        "ideal_reply_keywords": ["eu", "data residency", "compli", "document", "gdpr"]
    },
    {
        "id": "e047",
        "subject": "Bitcoin investment opportunity - 300% returns",
        "body": "Exclusive opportunity! Invest in our Bitcoin fund and earn guaranteed 300% returns in 60 days. Trusted by 50,000 investors. Minimum investment $500. Limited spots available.",
        "sender": "invest@crypto-scam.io",
        "label": "spam",
        "department": "none",
        "needs_escalation": False,
        "ideal_reply_keywords": []
    },
    {
        "id": "e048",
        "subject": "URGENT: Billing system charging all customers incorrectly",
        "body": "We are a reseller and have discovered that ALL our 200 customers have been overcharged by 20% this month due to what appears to be a bug in your billing system. Total overcharge: $45,000.",
        "sender": "billing@reseller-partner.com",
        "label": "urgent",
        "department": "billing",
        "needs_escalation": True,
        "ideal_reply_keywords": ["apolog", "escalat", "refund", "immediately", "resolv"]
    },
    {
        "id": "e049",
        "subject": "Congratulations on your product launch!",
        "body": "Hi team, I just saw the announcement about your new AI features. Really impressive work! Just wanted to drop a note to say keep it up. Looking forward to trying the new features.",
        "sender": "fan@happy-customer.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["thank", "appreciat", "feedback", "enjoy", "featur"]
    },
    {
        "id": "e050",
        "subject": "Competitor offering 50% less - match the price?",
        "body": "I've received a proposal from your competitor offering identical features at 50% of your price. I prefer your platform but can't justify the cost difference to my CFO. Can you price match?",
        "sender": "decision-maker@considering-churn.com",
        "label": "normal",
        "department": "sales",
        "needs_escalation": False,
        "ideal_reply_keywords": ["price", "match", "value", "discuss", "schedul"]
    },
]