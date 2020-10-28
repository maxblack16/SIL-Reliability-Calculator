# Title:openSIF reliability calculation tool
# Written by: Matthew Bates
#
# Description:
# Calculates SIF Total PFDavg and RRF for most common voting configurations.
# Voted subsystems are limited to having the same devices i.e. same failure rate data, prrof test interval, etc.
# Calculations are for Low Demand functions.
# Calculations are simplified to exclude Diagnostic Interval (DI) due to negligible contribution to subsystem PFDavg.
#
#
import os
from datetime import datetime

pfd = 0
hft = 0
vote = 0
hours_per_year = 8760
calc = ""

# Custom Functions:
def results(pfd, hft, calc):
    print('%s subsystem calculation: %s' % (subsystem, calc))
    print('%s PFDavg: %g' % (subsystem, pfd))
    print('%s HFT: %d' % (subsystem, hft))

def vote_1oo1(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr):
    global pfd, hft, calc, du_fr, pt, beta
    calc =  'ISA-TR84.00.02-2015 Table C.2-1oo1'
    pfd = ((du_failure_rate_yr * proof_test_yr) / 2) + ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)
    hft = 0
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = 'Not Applicable'
    results(pfd, hft, calc)

def vote_1oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd, hft, calc, du_fr, pt, beta
    calc = 'ISA-TR84.00.02-2015 Table C.2-1oo2'
    pfd = ((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)))**2 + (((ccf * du_failure_rate_yr * proof_test_yr) / 2) + ((ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)))
    hft = 1
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = ccf
    results(pfd, hft, calc)

def vote_1oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd, hft, calc, du_fr, pt, beta
    calc = 'ISA-TR84.00.02-2015 Table C.2-1oo3'
    pfd = ((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * ((du_failure_rate_yr + dd_failure_rate_yr) * mttr)))**3 + (((ccf * du_failure_rate_yr * proof_test_yr) / 2) + ((ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)))
    hft = 2
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = ccf
    results(pfd, hft, calc)

def vote_2oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr):
    global pfd, hft, calc, du_fr, pt, beta
    calc = 'ISA-TR84.00.02-2015 Table C.2-2oo2'
    pfd = 2*(((du_failure_rate_yr * proof_test_yr) / 2) + ((du_failure_rate_yr + dd_failure_rate_yr) * mttr))
    hft = 0
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = 'Not Applicable'
    results(pfd, hft, calc)

def vote_2oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf):
    global pfd, hft, calc, du_fr, pt, beta
    calc = 'ISA-TR84.00.02-2015 Table C.2-2oo3'
    pfd = 3*((((1-ccf) * du_failure_rate_yr * proof_test_yr) / 2) + ((1-ccf) * (du_failure_rate_yr + dd_failure_rate_yr) * mttr))**2 + (ccf * (du_failure_rate_yr + dd_failure_rate_yr) * mttr)
    hft = 1
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = ccf
    results(pfd, hft, calc)

def vote_3oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr):
    global pfd, hft, calc, du_fr, pt, beta
    calc = 'ISA-TR84.00.02-2015 Table C.2-3oo3'
    pfd = 3*(((du_failure_rate_yr * proof_test_yr) / 2) + ((du_failure_rate_yr + dd_failure_rate_yr) * mttr))
    hft = 0
    du_fr = du_failure_rate_yr
    pt = proof_test_yr
    beta = 'Not Applicable'
    results(pfd, hft, calc)

def subcalc(vote):
    while True:
        try:
            global voting
            vote = input('Enter voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3, 3oo3): ')
            voting = vote
            if voting == '1oo1':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                vote_1oo1(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr)
                break
            elif voting == '1oo2':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_1oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            elif voting == '1oo3':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_1oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            elif voting == '2oo2':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                vote_2oo2(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr)
                break
            elif voting == '2oo3':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                ccf = float(input('Enter Common Cause Factor: '))
                vote_2oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr, ccf)
                break
            elif voting == '3oo3':
                du_failure_rate_yr = float(input('Enter dangerous undiagnosed failure rate per year: '))
                proof_test_yr = float(input('Enter proof test interval in years: '))
                mttr = float(input('Enter MTTR in hours: ')) / hours_per_year
                dd_failure_rate_yr = float(input('Enter dangerous diagnosed failure rate per year: '))
                vote_3oo3(subsystem, du_failure_rate_yr, proof_test_yr, mttr, dd_failure_rate_yr)
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
sensor_pt = pt
sensor_du = du_fr
sensor_ccf = beta
sensor_pfd = pfd
sensor_hft = hft
sensor_calc = calc
#%%
print('\nSubsystem: Logic Solver') #Start logic solver subsytem calcs
subsystem = "Logic Solver"
subcalc(vote)
ls_pt = pt
ls_du = du_fr
ls_ccf = beta
ls_pfd = pfd
ls_hft = hft
ls_calc = calc
#%%
print('\nSubsystem: Final Element') #Start final element subsytem calcs
subsystem = "Final Element"
subcalc(vote)
fe_pt = pt
fe_du = du_fr
fe_ccf = beta
fe_pfd = pfd
fe_hft = hft
fe_calc = calc
#%%
# Calculate Total PFDavg and RRF:
sif_pfd = sensor_pfd + ls_pfd + fe_pfd #ISA-TR84.00.02-2015 Equation 8.1
sif_rrf = 1 / sif_pfd
if 10 > sif_rrf:
	sil = 'Less than SIL1'
elif 10 <= sif_rrf <100:
	sil = 'SIL1'
elif 100 <= sif_rrf < 1000:
	sil = 'SIL2'
elif 1000 <= sif_rrf <10000:
	sil = 'SIL3'
else:
	sil = 'Greater than SIL3, review data validity'
#%%
# Calculate subsystem PFDavg percentage contribution to the Total PFDavg
sensor_pcnt = (sensor_pfd/sif_pfd)*100
ls_pcnt = (ls_pfd/sif_pfd)*100
fe_pcnt = (fe_pfd/sif_pfd)*100
print('\nSIF: %s \nSIF Total PFDavg: %g \nSIF Total RRF: %g \nSIL: %s\n' %(sif_name, round(sif_pfd, 6), round(sif_rrf, 2), sil))
print('\nSubsystem: Sensor\n%s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n' % (sensor_calc, round(sensor_pfd, 6), round(sensor_pcnt, 2), sensor_hft))
print('\nSubsystem: Logic Solver\n%s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n' % (ls_calc, round(ls_pfd, 6), round(ls_pcnt, 2), ls_hft))
print('\nSubsystem: Final Element\n%s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n' % (fe_calc, round(fe_pfd, 6), round(fe_pcnt, 2), fe_hft))
#%%
revision_stamp = datetime.now()
revision_stamp = revision_stamp.strftime("%d/%m/%Y %H:%M:%S")

path = os.getcwd()
path = path + "\\" + sif_name + "\\"

if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)

fout = open(sif_name+'.txt','a')
line0 = '-------------------------------\n----- %s -----\n-------------------------------' % revision_stamp
line1 = '\nSIF: %s \nSIF Total PFDavg: %g \nSIF Total RRF: %g \nSIL: %s\n-----' % (sif_name, round(sif_pfd, 6), round(sif_rrf, 2), sil)
line2 = '\nSubsystem: Sensor\n%s\nDangerous Undiagnosed Failure Rate: %s\nProof Test Interval: %s\nCommon Cause Factor: %s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n' % (sensor_calc, sensor_du, sensor_pt, sensor_ccf, round(sensor_pfd, 6), round(sensor_pcnt, 2), sensor_hft)
line3 = '\nSubsystem: Logic Solver\n%s\nDangerous Undiagnosed Failure Rate: %s\nProof Test Interval: %s\nCommon Cause Factor: %s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n' % (ls_calc, ls_du, ls_pt, ls_ccf, round(ls_pfd, 6), round(ls_pcnt, 2), ls_hft)
line4 = '\nSubsystem: Final Element\n%s\nDangerous Undiagnosed Failure Rate: %s\nProof Test Interval: %s\nCommon Cause Factor: %s\nPFDavg: %g\n%% of Total PFDavg: %g%%\nHFT: %d\n\n' % (fe_calc, fe_du, fe_pt, fe_ccf, round(fe_pfd, 6), round(fe_pcnt, 2), fe_hft)
fout.writelines([line0, line1, line2, line3, line4])
fout.close()
