#Title:SIF Calc
#
#Description:
##Calculates SIF Total PFDavg and RRF for most common voting configurations.
##Voted subsystems are limited to having the same devices i.e. same failure rate data, prrof test interval, etc.
#
#Written by: Matthew Bates
#Date: 2nd September 2020
#Revision 0: Initial compilation
#
sif_name = input('Enter SIF name: ')

print('\nSubsystem: Sensor') #Start sensor subsytem calcs
sensor_voting = input('Enter sensor voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))

if sensor_voting == '1oo1': #ISA TR84-02-P2 eqn3
	sensor_pfd = (sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2
	sensor_hft = 0
elif sensor_voting == '1oo2': #ISA TR84-02-P2 eqn4b
	sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
	sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / 8760
	sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
	sensor_pfd = ((sensor_du_failure_rate_yr**2 * sensor_proof_test_yr**2) / 3) + (sensor_du_failure_rate_yr * sensor_dd_failure_rate_yr * sensor_mttr *sensor_proof_test_yr) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
	sensor_hft = 1
elif sensor_voting == '1oo3': #ISA TR84-02-P2 eqn5
	sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
	sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / 8760
	sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
	sensor_pfd = ((sensor_du_failure_rate_yr**3 * sensor_proof_test_yr**3) / 4) + (sensor_du_failure_rate_yr**2 * sensor_dd_failure_rate_yr * sensor_mttr * sensor_proof_test_yr**2) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
	sensor_hft = 2
elif sensor_voting == '2oo2': #ISA TR84-02-P2 eqn6
	sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
	sensor_pfd = (sensor_du_failure_rate_yr * sensor_proof_test_yr) + (sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr)
	sensor_hft = 0
elif sensor_voting == '2oo3': #ISA TR84-02-P2 eqn7
	sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
	sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / 8760
	sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
	sensor_pfd = ((sensor_du_failure_rate_yr**2 * sensor_proof_test_yr**2)) + (3 * sensor_du_failure_rate_yr * sensor_dd_failure_rate_yr * sensor_mttr *sensor_proof_test_yr) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
	sensor_hft = 1
else:
	print('Invalid voting')
print('Sensor PFDavg = ', sensor_pfd)
print('Sensor HFT = ', sensor_hft)

print('\nSubsystem: Logic Solver') #Start logic solver subsytem calcs
ls_voting = input('Enter logic solver voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))

if ls_voting == '1oo1': #ISA TR84-02-P2 eqn3
	ls_pfd = (ls_du_failure_rate_yr * ls_proof_test_yr) / 2
	ls_hft = 0
elif ls_voting == '1oo2': #ISA TR84-02-P2 eqn4b
	ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
	ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / 8760
	ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
	ls_pfd = ((ls_du_failure_rate_yr**2 * ls_proof_test_yr**2) / 3) + (ls_du_failure_rate_yr * ls_dd_failure_rate_yr * ls_mttr * ls_proof_test_yr) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
	ls_hft = 1
elif ls_voting == '1oo3': #ISA TR84-02-P2 eqn5
	ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
	ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / 8760
	ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
	ls_pfd = ((ls_du_failure_rate_yr**3 * ls_proof_test_yr**3) / 4) + (ls_du_failure_rate_yr**2 * ls_dd_failure_rate_yr * ls_mttr * ls_proof_test_yr**2) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
	ls_hft = 2
elif ls_voting == '2oo2': #ISA TR84-02-P2 eqn6
	ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
	ls_pfd = (ls_du_failure_rate_yr * ls_proof_test_yr) + (ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr)
	ls_hft = 0
elif ls_voting == '2oo3': #ISA TR84-02-P2 eqn7
	ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
	ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / 8760
	ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
	ls_pfd = ((ls_du_failure_rate_yr**2 * ls_proof_test_yr**2)) + (3 * ls_du_failure_rate_yr * ls_dd_failure_rate_yr * ls_mttr *ls_proof_test_yr) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
	ls_hft = 1
else:
	print('Invalid voting')
print('Logic Solver PFDavg = ', ls_pfd)
print('Logic Solver HFT = ', ls_hft)

print('\nSubsystem: Final Element') #Start final element subsytem calcs
fe_voting = input('Enter final element voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))

if fe_voting == '1oo1': #ISA TR84-02-P2 eqn3
	fe_pfd = (fe_du_failure_rate_yr * fe_proof_test_yr) / 2
	fe_hft = 0
elif fe_voting == '1oo2': #ISA TR84-02-P2 eqn4b
	fe_ccf = float(input('Enter final element Common Cause Factor: '))
	fe_mttr = float(input('Enter final element MTTR in hours: ')) / 8760
	fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
	fe_pfd = ((fe_du_failure_rate_yr**2 * fe_proof_test_yr**2) / 3) + (fe_du_failure_rate_yr * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
	fe_hft = 1
elif fe_voting == '1oo3': #ISA TR84-02-P2 eqn5
	fe_ccf = float(input('Enter final element Common Cause Factor: '))
	fe_mttr = float(input('Enter final element MTTR in hours: ')) / 8760
	fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
	fe_pfd = ((fe_du_failure_rate_yr**3 * fe_proof_test_yr**3) / 4) + (fe_du_failure_rate_yr**2 * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr**2) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
	fe_hft = 2
elif fe_voting == '2oo2': #ISA TR84-02-P2 eqn6
	fe_ccf = float(input('Enter final element Common Cause Factor: '))
	fe_pfd = (fe_du_failure_rate_yr * fe_proof_test_yr) + (fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr)
	fe_hft = 0
elif fe_voting == '2oo3': #ISA TR84-02-P2 eqn7
	fe_ccf = float(input('Enter final element Common Cause Factor: '))
	fe_mttr = float(input('Enter final element MTTR in hours: ')) / 8760
	fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
	fe_pfd = ((fe_du_failure_rate_yr**2 * fe_proof_test_yr**2)) + (3 * fe_du_failure_rate_yr * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
	fe_hft = 1
else:
	print('Invalid voting')
print('Final Element PFDavg = ', fe_pfd)
print('Final Element HFT = ', fe_hft)

#Calculate Total PFDavg and RRF
sif_pfd = sensor_pfd + ls_pfd + fe_pfd
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

print('\n')
print(sif_name, 'SIF Total PFDavg = ', round(sif_pfd, 6), '\nSIF Total RRF = ', round(sif_rrf, 2))
print(sil)
print('Sensor HFT: ', sensor_hft, '\nLogic Solver HFT: ', ls_hft, '\nFinal Element HFT: ', fe_hft)
