import csv;

# CALCULATE SIMPLE DIETZ RATE OF RETURN
# Reference: https://en.wikipedia.org/wiki/Simple_Dietz_method
def simpleDietz(a, b, c, d, e, f, g):
    numerator = c;
    net_external_inflow = b-(d+e+f);
    denominator = a + (0.5*net_external_inflow)
    if(denominator != 0):
        return(100*numerator/denominator)
    else:
        return 0;

# Write estimated return values for csv file, save in the folder titled "output_files"
def writeToFile(entity, csvData):
    with open('output_files/'+entity+'.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)

# Extract information from the 990 csv
# This is done using the xpath identifier for each field.
# The xpath for a field differs from year to year, so the OR statements take this into account when processing 990 CSV files from different years.
# This can definitely be cleaned up. I used a quick and dirty method since I was testing whether the idea would work.
def extractInformation(entitycode, year_start, year_end):
    print(entitycode, year_start, year_end)
    csvData = [['year', 'timecode', 'return']]

    aCY = bCY = cCY = dCY = eCY = fCY = gCY = 0;
    a1Y = b1Y = c1Y = d1Y = e1Y = f1Y = g1Y = 0;
    a2Y = b2Y = c2Y = d2Y = e2Y = f2Y = g2Y = 0;
    a3Y = b3Y = c3Y = d3Y = e3Y = f3Y = g3Y = 0;
    a4Y = b4Y = c4Y = d4Y = e4Y = f4Y = g4Y = 0;


    for x in range(year_start, year_end+1):
        try:
            with open('990csv_files/'+entitycode+str(x)+'.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # CURRENT YEAR - Beginning year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/BeginningOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/BeginningYearBalanceAmt')):
                        aCY = float(row['value'])
                    # CURRENT YEAR - End year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/Contributions') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/ContributionsAmt')):
                        bCY = float(row['value'])
                    # CURRENT YEAR - Investment Earnings
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/InvestmentEarningsOrLosses') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/InvestmentEarningsOrLossesAmt')):
                        cCY = float(row['value'])
                    # CURRENT YEAR - Grants or Scholarships
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/GrantsOrScholarships') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/GrantsOrScholarshipsAmt')):
                        dCY = float(row['value'])
                    # CURRENT YEAR - Other Expenditures
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/OtherExpenditures') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/OtherExpendituresAmt')):
                        eCY = float(row['value'])
                    # CURRENT YEAR - Administrative Expenses
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/AdministrativeExpenses') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/AdministrativeExpensesAmt')):
                        fCY = float(row['value'])
                    # CURRENT YEAR - EOY Balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYear/EndOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYEndwmtFundGrp/EndYearBalanceAmt')):
                        gCY = float(row['value'])



                    # 1 YEAR - Beginning year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/BeginningOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/BeginningYearBalanceAmt')):
                        a1Y = float(row['value'])
                    # 1 YEAR - End year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/Contributions') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/ContributionsAmt')):
                        b1Y = float(row['value'])
                    # 1 YEAR - Investment Earnings
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/InvestmentEarningsOrLosses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt')):
                        c1Y = float(row['value'])
                    # 1 YEAR - Grants or Scholarships
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/GrantsOrScholarships') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/GrantsOrScholarshipsAmt')):
                        d1Y = float(row['value'])
                    # 1 YEAR - Other Expenditures
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/OtherExpenditures') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/OtherExpendituresAmt')):
                        e1Y = float(row['value'])
                    # 1 YEAR - Administrative Expenses
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/AdministrativeExpenses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/AdministrativeExpensesAmt')):
                        f1Y = float(row['value'])
                    # 1 YEAR - EOY Balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus1Year/EndOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/EndYearBalanceAmt')):
                        g1Y = float(row['value'])



                    # 2 YEAR - Beginning year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/BeginningOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/BeginningYearBalanceAmt')):
                        a2Y = float(row['value'])
                    # 2 YEAR - End year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/Contributions') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/ContributionsAmt')):
                        b2Y = float(row['value'])
                    # 2 YEAR - Investment Earnings
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/InvestmentEarningsOrLosses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt')):
                        c2Y = float(row['value'])
                    # 2 YEAR - Grants or Scholarships
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/GrantsOrScholarships') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/GrantsOrScholarshipsAmt')):
                        d2Y = float(row['value'])
                    # 2 YEAR - Other Expenditures
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/OtherExpenditures') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/OtherExpendituresAmt')):
                        e2Y = float(row['value'])
                    # 2 YEAR - Administrative Expenses
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/AdministrativeExpenses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/AdministrativeExpensesAmt')):
                        f2Y = float(row['value'])
                    # 2 YEAR - EOY Balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus2Years/EndOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/EndYearBalanceAmt')):
                        g2Y = float(row['value'])



                    # 3 YEAR - Beginning year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/BeginningOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/BeginningYearBalanceAmt')):
                        a3Y = float(row['value'])
                    # 3 YEAR - End year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/Contributions') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/ContributionsAmt')):
                        b3Y = float(row['value'])
                    # 3 YEAR - Investment Earnings
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/InvestmentEarningsOrLosses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt')):
                        c3Y = float(row['value'])
                    # 3 YEAR - Grants or Scholarships
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/GrantsOrScholarships') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/GrantsOrScholarshipsAmt')):
                        d3Y = float(row['value'])
                    # 3 YEAR - Other Expenditures
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/OtherExpenditures') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/OtherExpendituresAmt')):
                        e3Y = float(row['value'])
                    # 3 YEAR - Administrative Expenses
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/AdministrativeExpenses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/AdministrativeExpensesAmt')):
                        f3Y = float(row['value'])
                    # 3 YEAR - EOY Balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus3Years/EndOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/EndYearBalanceAmt')):
                        g3Y = float(row['value'])




                    # 4 YEAR - Beginning year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/BeginningOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/BeginningYearBalanceAmt')):
                        a4Y = float(row['value'])
                    # 4 YEAR - End year balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/Contributions') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/ContributionsAmt')):
                        b4Y = float(row['value'])
                    # 4 YEAR - Investment Earnings
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/InvestmentEarningsOrLosses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt')):
                        c4Y = float(row['value'])
                    # 4 YEAR - Grants or Scholarships
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/GrantsOrScholarships') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/GrantsOrScholarshipsAmt')):
                        d4Y = float(row['value'])
                    # 4 YEAR - Other Expenditures
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/OtherExpenditures') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/OtherExpendituresAmt')):
                        e4Y = float(row['value'])
                    # 4 YEAR - Administrative Expenses
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/AdministrativeExpenses') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/AdministrativeExpensesAmt')):
                        f4Y = float(row['value'])
                    # 4 YEAR - EOY Balance
                    if((row['xpath'] == '/IRS990ScheduleD/CurrentYearMinus4Years/EndOfYearBalance') or (row['xpath'] == '/IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/EndYearBalanceAmt')):
                        g4Y = float(row['value'])

            current = [x-1, "CY", simpleDietz(aCY, bCY, cCY, dCY, eCY, fCY, gCY)];
            # print(x, aCY, bCY, cCY, dCY, eCY, fCY, gCY);
            csvData.append(current);
            oneyear = [x-2, "1Y", simpleDietz(a1Y, b1Y, c1Y, d1Y, e1Y, f1Y, g1Y)];
            # print(x, a1Y, b1Y, c1Y, d1Y, e1Y, f1Y, g1Y);
            csvData.append(oneyear);
            twoyear = [x-3, "2Y", simpleDietz(a2Y, b2Y, c2Y, d2Y, e2Y, f2Y, g2Y)];
            # print(x, a2Y, b2Y, c2Y, d2Y, e2Y, f2Y, g2Y);
            csvData.append(twoyear);
            threeyear = [x-4, "3Y", simpleDietz(a3Y, b3Y, c3Y, d3Y, e3Y, f3Y, g3Y)];
            # print(x, a3Y, b3Y, c3Y, d3Y, e3Y, f3Y, g3Y);
            csvData.append(threeyear);
            fouryear = [x-5, "4Y", simpleDietz(a4Y, b4Y, c4Y, d4Y, e4Y, f4Y, g4Y)];
            # print(x, a4Y, b4Y, c4Y, d4Y, e4Y, f4Y, g4Y);
            csvData.append(fouryear);
        except:
            print("error")

    writeToFile(entitycode, csvData)


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

for key, value in cornerstone.items():
    extractInformation(key, 2012, 2017);
