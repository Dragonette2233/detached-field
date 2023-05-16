import logging

def main():
    logging.info('INFO MESSAGE')
    logging.debug('DEBUG info')
    logging.error('ERROR Here')
    


if __name__ == '__main__':
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    # logging.basicConfig(level=level, format=fmt, filename='pylogs.log', filemode='a+')
    main()