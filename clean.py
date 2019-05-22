def clean_price(self, string):
        return string.replace('\n', ''). \
                      replace('£', ''). \
                      replace('\t', ''). \
                      replace('\r', ''). \
                      replace('(', ''). \
                      replace(')', ''). \
                      replace('€', ''). \
                      replace('.', ''). \
                      replace(',', '.'). \
                      replace(' ', '')

def clean_json(self, string):
        return string.replace('\\n', '').replace("\\'", '')\
                    .replace('\\xc3', '').replace('\\x88', '')\
                    .replace('\\x89', '').replace('\\x82', '')\
                    .replace('\\xc2', '').replace('\\xa0', '')\
                    .replace('\\xa9', '').replace('\\xa8', '')\
                    .replace('\\xe2', '').replace('\\x82', '')\
                    .replace('\\xac', '').replace('\\xb6', '')\
                    .replace('\\xbc', '').replace('\\x80', '')\
                    .replace('\\xb4', '').replace('\\x84', '')\
                    .replace('\\xa2', '').replace('\\xaa', '')\
                    .replace('\\x96', '').replace('\\x9f', '')\
                    .replace('\\xa4', '').replace('\\xae', '')\
                    .replace('\\x94', '').replace('\\xb8', '')\
                    .replace('\\xc5', '').replace('\\xb0', '')
        
def clean_unicode(self, string):
        return string.replace('Ã¨', 'è')\
                    .replace('Ã©', 'é')\
                    .replace('Ã©', 'é')\
                    .replace('Ã¢', 'â')\
                    .replace('Ã ', 'à')\
                    .replace('Â', '')\
                    .replace('Ã' + chr(130), 'Â')\
                    .replace('Ã' + chr(137), 'E')\
                    .replace('Å' + chr(146), 'oe')\
                    .replace(''.join(['â', chr(128), chr(153)]), "'")
