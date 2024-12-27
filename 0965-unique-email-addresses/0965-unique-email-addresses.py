from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # Use a set to store unique email addresses
        
        for email in emails:
            # Split the email into local and domain parts
            local, domain = email.split('@')
            # Process the local part
            local = local.split('+')[0]  # Ignore everything after the first '+'
            local = local.replace('.', '')  # Remove all '.' characters
            
            # Combine the processed local part with the domain part
            unique_email = local + '@' + domain
            unique_emails.add(unique_email)  # Add to the set
        
        # Return the number of unique email addresses
        return len(unique_emails)

# Example usage:
if __name__ == "__main__":
    solution = Solution()