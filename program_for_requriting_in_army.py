requirements = {
    'height' : 5.8,
    'weight' : 65,
    'health_status' : 'healthy',
    'education' : '+2 pass',
    'criminal_record' : False
}

while True:
    height = float(input('Enter your height: '))
    weight = float(input('Enter your weight: '))
    health_status = input('Make sure if you are haalthy? : ')
    education = float(input('Enter your education qualification: '))
    for keys, values in requirements:
        for check in ['height', 'weight', 'health_status', 'education']:
            if height> weight: