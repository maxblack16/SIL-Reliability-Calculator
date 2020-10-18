# Title:SIF Calc
#
# Description:
# Calculates SIF Total PFDavg and RRF for most common voting configurations.
# Voted subsystems are limited to having the same devices i.e. same failure rate data, prrof test interval, etc.
# Calculations are for Low Demand functions.
# Calculations are simplified to exclude Diagnostic Interval (DI) due to negligible contribution to subsystem PFDavg.
#
# Written by: Matthew Bates
# Date: 2nd September 2020
#
# Initialise variables:
pfd = 0
hft = 0
vote = 0
hours_per_year = 8760

# Custom Functions:
def results(pfd, hft):
    print('%s PFDavg = %g' % (subsystem, pfd))
    print('%s HFT = %d' % (subsystem, hft))

def vote_1oo1(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr):
    global pfd
    global hft
    pfd = ((du_failure_rate_yr * proof_test_yr) / 2) + ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)
    hft = 0
    results(pfd, hft)

def vote_1oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd
    global hft
    pfd = ((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)))**2 + (((ccf * du_failure_rate_yr * proof_test_yr) / 2) + ((ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)))
    hft = 1
    results(pfd, hft)

def vote_1oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd
    global hft
    pfd = ((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)))**3 + (((ccf * du_failure_rate_yr * proof_test_yr) / 2) + ((ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)))
    hft = 2
    results(pfd, hft)

def vote_2oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr):
    global pfd
    global hft
    pfd = 2*(((du_failure_rate_yr * proof_test_yr) / 2) + ((du_failure_rate_yr + dd_failure_rate_yr) * mttr))
    hft = 0
    results(pfd, hft)

def vote_2oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd
    global hft
    pfd = 3*((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * (du_failure_rate_yr + dd_failure_rate_yr) * mttr))**2 + (ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)
    hft = 1
    results(pfd, hft)

def subcalc(vote):
    while True:
        try:
            global voting
            vote = input('Enter voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
            voting = vote
            if voting == '1oo1': #ISA-TR84.00.02-2015 Table C.2-1oo1
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                vote_1oo1(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr)
                break
            elif voting == '1oo2': #ISA-TR84.00.02-2015 Table C.2-1oo2
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_1oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            elif voting == '1oo3': #ISA-TR84.00.02-2015 Table C.2-1oo3
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_1oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            elif voting == '2oo2': #ISA-TR84.00.02-2015 Table C.2-2oo2
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                vote_2oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr)
                break
            elif voting == '2oo3': #ISA-TR84.00.02-2015 Table C.2-2oo3
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_2oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            else:
                print('Invalid voting')
                continue
        except:
            print('Invalid input. Please try again.')

# Main code:
sif_name = input('Enter SIF name: ')
sif_name = sif_name.upper()
#%%
print('\nSubsystem: Sensor') #Start sensor subsytem calcs
subsystem = "Sensor"
subcalc(vote)
sensor_pfd = pfd
sensor_hft = hft
#%%
print('\nSubsystem: Logic Solver') #Start logic solver subsytem calcs
subsystem = "Logic Solver"
subcalc(vote)
ls_pfd = pfd
ls_hft = hft
#%%
print('\nSubsystem: Final Element') #Start final element subsytem calcs
subsystem = "Final Element"
subcalc(vote)
fe_pfd = pfd
fe_hft = hft
#%%
# Calculate Total PFDavg and RRF:
sif_pfd = sensor_pfd + ls_pfd + fe_pfd #ISA-TR84.00.02-2015 Equation 8.1
sif_rrf = 1 / sif_pfd
if 10 > sif_rrf:
	sil = 'sub SIL1'
elif 10 <= sif_rrf <100:
	sil = 'SIL1'
elif 100 <= sif_rrf < 1000:
	sil = 'SIL2'
elif 1000 <= sif_rrf <10000:
	sil = 'SIL3'
else:
	sil = 'Greater than SIL3, review data validity'

sensor_pcnt = (sensor_pfd/sif_pfd)*100
ls_pcnt = (ls_pfd/sif_pfd)*100
fe_pcnt = (fe_pfd/sif_pfd)*100
print('\nSIF: %s \nSIF Total PFDavg: %g \nSIF Total RRF: %g \nSIL: %s\n\nSensor HFT: %d \nLogic Solver HFT: %d \nFinal Element HFT: %d' %(sif_name, round(sif_pfd, 6), round(sif_rrf, 2), sil, sensor_hft, ls_hft, fe_hft))
print('\nSensor contribution: %g%%\nLogic Solver contribution: %g%%\nFinal ELement contribution: %g%%' % (round(sensor_pcnt, 2), round(ls_pcnt, 2), round(fe_pcnt, 2)))
#%%
fout = open(sif_name+'.txt','w')
print(fout)
line1 = '\nSIF: %s \nSIF Total PFDavg: %g \nSIF Total RRF: %g \nSIL: %s\n\nSensor HFT: %d \nLogic Solver HFT: %d \nFinal Element HFT: %d' %(sif_name, round(sif_pfd, 6), round(sif_rrf, 2), sil, sensor_hft, ls_hft, fe_hft)
fout.write(line1)
fout.close()