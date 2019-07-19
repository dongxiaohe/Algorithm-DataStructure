class Solution(object):
    def numUniqueEmails(self, emails):
        uniqueEmails = set()
        for email in emails:
            localName, domain = email.split('@')
            localName = localName.split('+')[0]
            uniqueEmails.add(localName.replace(',', '') + "@" + domain)
        return len(uniqueEmails)

