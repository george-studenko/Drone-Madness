from Object_Detection import *

def main():

    print('Detecting objects...')
    person = 'img/person.jpg'
    car = 'img/car.jpg'
    city = 'img/city.jpg'
    detector = Object_Detection()
    detector.detect(person)
    detector.detect(car)
    detector.detect(city)
    print('Done...')


if __name__ == '__main__':
    main()

