import re
import logging


class matchstring:
    def section_email(self):
        with open('content.txt', 'r') as Content:
            for content in Content:
                section_numbers = re.findall(r'\d+\.\d+\.\d+', content)
                email_ids = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

                result = {'section_numbers': section_numbers, 'email_ids': email_ids}
                print(result)
                # logging.info(result)


match = matchstring()
match.section_email()
