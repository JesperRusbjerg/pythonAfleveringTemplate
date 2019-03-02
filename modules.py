import numpy as np
import matplotlib.pyplot as plt

def findEnglishSpeakingAndNonEnglishSpeaking(data):
    
    english_countries = [5170,5309, 5502, 5303, 5305,5526, 5314, 5326,5339, 5308,5142,
5352, 5514, 5625, 5347, 5311, 5374,5390]

    english_mask = (data[:,0] == 2015) & np.in1d(data[:,3], english_countries)
        
    # print('Total of english people:' + str(sum(data[english_mask][:,4])))
    eng_speaking = sum(data[english_mask][:,4])
    
    non_english_mask = (data[:,0] == 2015)
    non_eng_speaking = sum(data[non_english_mask][:,4])-eng_speaking
    
    return {'eng_speaking': eng_speaking, 'non_eng_speaking': non_eng_speaking}

def filterFunc(data, mask):
    return data[mask]

def xValues(data, xValue):
    return sum(data[:,xValue])

def get_data_by_age(data, start, end, year=2015):
    mask = (data[:, 0] == year) & (data[:, 2] >= start) & (data[:, 2] <= end)
    age_data = data[mask]
    return {age : np.sum(age_data[(age_data[:, 2] == age)][:,4]) for age in age_data[:, 2]}

def findPeopleMask(data, age_group, area=3, year=2015):
    dicts = {}
    for ages in age_group:
        addString = '{}-{}'.format(ages[0], ages[-1])
        dicts[addString] = 0
        osterbro_only_mask = (data[:,1] == area) & (data[:,0] == year) & (np.in1d(data[:,2], ages))
        dicts[addString] = sum(data[osterbro_only_mask][:,4])
    return dicts