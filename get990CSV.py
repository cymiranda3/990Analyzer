import os, csv
year_array = ['2012', '2013', '2014', '2015', '2016', '2017']

# Lists for EINs:

# EINDictionary = {
    # 'cornell':'150532082',
    # 'gwu':'530196584', # GW - Good
    # 'nd':'350868188', # Notre Dame
    # 'ups': '910564961', # Puget Sound
    # 'mhc': '042103578',
    # 'soc':'410693979', #Saint Olaf - Good
    # 'fiu':'237047106',
    # 'msu':'640410581',
    # 'uor':'160743209'
    # 'ouf': '316402269'
    # 'cwf':'540505888'
    # 'tc':'060646927'
    # 'uod': '840404231' #University of Denver -- i think Good
    # 'dc':'231365954', #dickinson college -- i think good
    # 'risd':'050258956'
    # 'iit': '362170136',
    # 'rit':'160743140', # good - mercer
    # 'su':'150532081' # good - mercer
    # 'wsuf':'911075542'
    # 'ncsu':'566049503'
# }

# GEM = {
#     'christensen':'946055879',
#     'haasfund': '946068932',
#     'jmfamily': '591390794',
#     'planting': '111770097',
#     'shelteringarms':'541615599',
#     'willamette':'930386972',
#     'risd':'050258956',
#     'lighthouse':'464215298'
# }

cornerstone = {
    'animas':'431617896',
    'depauw':'350869045',
    'wisc_scholars':'261412296',
    'hoag':'951643327',
    'jkcf':'541896244',
    'kenyon':'314379507',
    'lumina':'351813228',
    'mfh':'431880952',
    'ohf':'510249728',
    'sageworth':'233089620',
    'sp':'581437002',
    'sjhs':'223243418',
    'sunhealth':'237107959',
    'tnc':'530242652',
    'tll':'756037406',
    'soc':'410693979',
    'ceeb':'131623965',
}

# GETS THE OBJECT IDs FOR ANY ENTITY, GIVEN THE EIN NUMBER
def getObjectIds(EIN):
    objectIDList = {};
    for year in year_array:
        with open('index_files/index_'+year+'.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['EIN'] == EIN:
                    objectIDList[year] = row['OBJECT_ID'];
    return objectIDList


# Downloads the CSV for each EIN
# Files are saved in 990csv_files as the "code"+"year"
for key, value in cornerstone.items():
    print(key, value)
    objectIDList = getObjectIds(value)
    print(objectIDList)
    for year, identifier in objectIDList.items():
        os.system("irsx --format=csv --file='990csv_files/"+key+year+".csv' "+identifier);
