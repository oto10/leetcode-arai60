class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")
            normalized_local = local.split("+", 1)[0]
            normalized_local = normalized_local.replace(".", "")
            unique_emails.add(normalized_local + "@" + domain)

        return len(unique_emails)
