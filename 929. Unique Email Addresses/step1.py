class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_addresses = set()
        for email in emails:
            local, domain = email.split("@")
            email_address = ""
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                email_address += c

            unique_email_addresses.add(email_address + "@" + domain)

        return len(unique_email_addresses)
