from Object_Detection import *

def main():

    print('Detecting objects...')
    path = 'img/person.jpg'
    detector = Object_Detection()
    detector.detect(path)
    print('Done...')


if __name__ == '__main__':
    main()
