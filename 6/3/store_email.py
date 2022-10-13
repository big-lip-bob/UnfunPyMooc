def store_email(mails):
    domains = {}
    for mail in mails:
        [user, domain] = mail.split('@')
        domains.setdefault(domain, []).append(user)
    for domain in domains: domains[domain].sort()
    return domains