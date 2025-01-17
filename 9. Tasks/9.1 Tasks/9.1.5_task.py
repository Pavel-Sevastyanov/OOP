import re


class DomainException(Exception):
    pass


class Domain:
    regex = r'[a-zA-Z]+\.[a-zA-Z]+'

    def __init__(self, domain):
        self.domain = self.check_domain(domain)

    def __str__(self):
        return self.domain

    @classmethod
    def from_url(cls, url):
        if not re.fullmatch(fr'https?://{Domain.regex}', url):
            raise DomainException('Недопустимый домен, url или email')
        return cls(re.findall(Domain.regex, url)[0])

    @classmethod
    def from_email(cls, email):
        if not re.fullmatch(fr'[a-zA-Z]+@{Domain.regex}', email):
            raise DomainException('Недопустимый домен, url или email')
        return cls(re.findall(Domain.regex, email)[0])
    
    def check_domain(self, domain):
        if not re.fullmatch(fr'{Domain.regex}', domain):
            raise DomainException('Недопустимый домен, url или email')
        return domain