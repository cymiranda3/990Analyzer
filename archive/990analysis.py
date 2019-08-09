import csv;
from irsx.xmlrunner import XMLRunner;

cornell = ['150532082'] # Cornell University
puget = ['910564961']
washu = ['430653611']
gw = ['530196584']
year_array = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

# GETS THE OBJECT IDs FOR ANY ENTITY, GIVEN THE EIN NUMBER
def getObjectIds(targetarray):
    ID_dictionary = {};
    for year in year_array:
        year_dictionary = {};
        with open('index_files/index_'+year+'.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['EIN'] in targetarray:
                    ID_dictionary[year] = row['OBJECT_ID']
    return(ID_dictionary)

# EXTRACT VARIABLES FROM 990 AND RUN THROUGH DIETZ ANALYSIS
def analyze990(filing_number):
    xml_runner = XMLRunner();
    parsed_filing = xml_runner.run_filing(filing_number);
    result = parsed_filing.get_csv_result()
    print(result)

    # schedule_list = parsed_filing.list_schedules()
    # scheduleDLocation = schedule_list.index('IRS990ScheduleD');

    # print(result[scheduleDLocation])
    # print("\n\n\n\n")

    # CY_A = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_BgnnngYrBlncAmt'])
    # CY_B = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_CntrbtnsAmt'])
    # CY_C = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_InvstmntErnngsOrLsssAmt'])
    # CY_D = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_GrntsOrSchlrshpsAmt'])
    # CY_E = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_OthrExpndtrsAmt'])
    # CY_F = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_AdmnstrtvExpnssAmt'])
    # CY_G = float(result[scheduleDLocation]['schedule_parts']['skedd_part_v']['CYEndwmtFnd_EndYrBlncAmt'])
    #
    # print(simpleDietz(CY_A, CY_B, CY_C, CY_D, CY_E, CY_F, CY_G))

# CALCULATE SIMPLE DIETZ RATE OF RETURN
def simpleDietz(a, b, c, d, e, f, g):
    numerator = c;
    net_external_inflow = b-(d+e+f);
    denominator = a + (0.5*net_external_inflow)
    return(numerator/denominator)

# print(getObjectIds(gw));


# for key, value in cornell_idents.items():
#     print(analyze990(value))

# cornell
# analyze990(201121369349302867);
# analyze990(201221359349305637);
# analyze990(201331339349303193);
# analyze990(201401349349302840);
# analyze990(201501319349302275);
# analyze990(201631349349307318);
# analyze990(201741309349302099);

# puget sound
# analyze990(201141319349302534);
# analyze990(201201309349300215);
# analyze990(201321339349303832);
# analyze990(201411349349303826);
# analyze990(201541329349302784);
# analyze990(201641379349304869);
# analyze990(201711329349306681);

# gw
analyze990(201141309349302104);
# analyze990(201231329349301258);
# analyze990(201331309349302878);
# analyze990(201411329349301706);
# analyze990(201531339349305548);
# analyze990(201641349349306559);
# analyze990(201741319349303099);

# objectIDList = getObjectIds(cornell);





# NOTES:
# 1. Should be accessing object id by EIN, not name.
# 2. Need to run it for each year.
# 3. Need to put everything into a CSV to to properly read it.
# 4. Need to backtest for Strategic clients.
# 5. Split up by fiscal year end dates for comparison across endowments.
