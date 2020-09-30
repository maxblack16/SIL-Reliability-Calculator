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
hours_per_year = 8760

sif_name = input('Enter SIF name: ')

print('\nSubsystem: Sensor') #Start sensor subsytem calcs
while True:
	sensor_voting = input('Enter sensor voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
	try:
		if sensor_voting == '1oo1': #ISA TR84-02-P2 eqn3
			sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
			sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))
			sensor_pfd = (sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2
			sensor_hft = 0
			break
		elif sensor_voting == '1oo2': #ISA TR84-02-P2 eqn4b
			sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
			sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))
			sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
			sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / hours_per_year
			sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
			sensor_pfd = ((sensor_du_failure_rate_yr**2 * sensor_proof_test_yr**2) / 3) + (sensor_du_failure_rate_yr * sensor_dd_failure_rate_yr * sensor_mttr *sensor_proof_test_yr) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
			sensor_hft = 1
			break
		elif sensor_voting == '1oo3': #ISA TR84-02-P2 eqn5
			sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
			sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))
			sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
			sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / hours_per_year
			sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
			sensor_pfd = ((sensor_du_failure_rate_yr**3 * sensor_proof_test_yr**3) / 4) + (sensor_du_failure_rate_yr**2 * sensor_dd_failure_rate_yr * sensor_mttr * sensor_proof_test_yr**2) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
			sensor_hft = 2
			break
		elif sensor_voting == '2oo2': #ISA TR84-02-P2 eqn6
			sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
			sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))
			sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
			sensor_pfd = (sensor_du_failure_rate_yr * sensor_proof_test_yr) + (sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr)
			sensor_hft = 0
			break
		elif sensor_voting == '2oo3': #ISA TR84-02-P2 eqn7
			sensor_du_failure_rate_yr = float(input('Enter sensor dangerous undiagnosed failure rate per year: '))
			sensor_proof_test_yr = float(input('Enter sensor proof test interval in years: '))
			sensor_ccf = float(input('Enter sensor Common Cause Factor: '))
			sensor_mttr = float(input('Enter sensor MTTR in hours: ')) / hours_per_year
			sensor_dd_failure_rate_yr = float(input('Enter sensor dangerous diagnosed failure rater per year: '))
			sensor_pfd = ((sensor_du_failure_rate_yr**2 * sensor_proof_test_yr**2)) + (3 * sensor_du_failure_rate_yr * sensor_dd_failure_rate_yr * sensor_mttr *sensor_proof_test_yr) + ((sensor_ccf * sensor_du_failure_rate_yr * sensor_proof_test_yr) / 2)
			sensor_hft = 1
			break
		else:
			print('Invalid voting')
			continue
	except:
		print('Invalid input. Please try again.')
print('Sensor PFDavg = %g' % sensor_pfd)
print('Sensor HFT = %d' % sensor_hft)

print('\nSubsystem: Logic Solver') #Start logic solver subsytem calcs
while True:
	ls_voting = input('Enter logic solver voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
	try:
		if ls_voting == '1oo1': #ISA TR84-02-P2 eqn3
			ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
			ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))
			ls_pfd = (ls_du_failure_rate_yr * ls_proof_test_yr) / 2
			ls_hft = 0
			break
		elif ls_voting == '1oo2': #ISA TR84-02-P2 eqn4b
			ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
			ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))
			ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
			ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / hours_per_year
			ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
			ls_pfd = ((ls_du_failure_rate_yr**2 * ls_proof_test_yr**2) / 3) + (ls_du_failure_rate_yr * ls_dd_failure_rate_yr * ls_mttr * ls_proof_test_yr) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
			ls_hft = 1
			break
		elif ls_voting == '1oo3': #ISA TR84-02-P2 eqn5
			ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
			ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))
			ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
			ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / hours_per_year
			ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
			ls_pfd = ((ls_du_failure_rate_yr**3 * ls_proof_test_yr**3) / 4) + (ls_du_failure_rate_yr**2 * ls_dd_failure_rate_yr * ls_mttr * ls_proof_test_yr**2) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
			ls_hft = 2
			break
		elif ls_voting == '2oo2': #ISA TR84-02-P2 eqn6
			ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
			ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))
			ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
			ls_pfd = (ls_du_failure_rate_yr * ls_proof_test_yr) + (ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr)
			ls_hft = 0
			break
		elif ls_voting == '2oo3': #ISA TR84-02-P2 eqn7
			ls_du_failure_rate_yr = float(input('Enter logic solver dangerous undiagnosed failure rate per year: '))
			ls_proof_test_yr = float(input('Enter logic solver proof test interval in years: '))
			ls_ccf = float(input('Enter logic solver Common Cause Factor: '))
			ls_mttr = float(input('Enter logic solver MTTR in hours: ')) / hours_per_year
			ls_dd_failure_rate_yr = float(input('Enter logic solver dangerous diagnosed failure rater per year: '))
			ls_pfd = ((ls_du_failure_rate_yr**2 * ls_proof_test_yr**2)) + (3 * ls_du_failure_rate_yr * ls_dd_failure_rate_yr * ls_mttr *ls_proof_test_yr) + ((ls_ccf * ls_du_failure_rate_yr * ls_proof_test_yr) / 2)
			ls_hft = 1
			break
		else:
			print('Invalid voting')
			continue
	except:
		print('Invalid input. Please try again.')
print('Logic Solver PFDavg = %g' % ls_pfd)
print('Logic Solver HFT = %d' % ls_hft)

print('\nSubsystem: Final Element') #Start final element subsytem calcs
while True:
	fe_voting = input('Enter final element voting (1oo1, 1oo2, 1oo3, 2oo2, 2oo3): ')
	try:
		if fe_voting == '1oo1': #ISA TR84-02-P2 eqn3
			fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
			fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))
			fe_pfd = (fe_du_failure_rate_yr * fe_proof_test_yr) / 2
			fe_hft = 0
			break
		elif fe_voting == '1oo2': #ISA TR84-02-P2 eqn4b
			fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
			fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))
			fe_ccf = float(input('Enter final element Common Cause Factor: '))
			fe_mttr = float(input('Enter final element MTTR in hours: ')) / hours_per_year
			fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
			fe_pfd = ((fe_du_failure_rate_yr**2 * fe_proof_test_yr**2) / 3) + (fe_du_failure_rate_yr * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
			fe_hft = 1
			break
		elif fe_voting == '1oo3': #ISA TR84-02-P2 eqn5
			fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
			fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))
			fe_ccf = float(input('Enter final element Common Cause Factor: '))
			fe_mttr = float(input('Enter final element MTTR in hours: ')) / hours_per_year
			fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
			fe_pfd = ((fe_du_failure_rate_yr**3 * fe_proof_test_yr**3) / 4) + (fe_du_failure_rate_yr**2 * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr**2) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
			fe_hft = 2
			break
		elif fe_voting == '2oo2': #ISA TR84-02-P2 eqn6
			fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
			fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))
			fe_ccf = float(input('Enter final element Common Cause Factor: '))
			fe_pfd = (fe_du_failure_rate_yr * fe_proof_test_yr) + (fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr)
			fe_hft = 0
			break
		elif fe_voting == '2oo3': #ISA TR84-02-P2 eqn7
			fe_du_failure_rate_yr = float(input('Enter final element dangerous undiagnosed failure rate per year: '))
			fe_proof_test_yr = float(input('Enter final element proof test interval in years: '))
			fe_ccf = float(input('Enter final element Common Cause Factor: '))
			fe_mttr = float(input('Enter final element MTTR in hours: ')) / hours_per_year
			fe_dd_failure_rate_yr = float(input('Enter final element dangerous diagnosed failure rater per year: '))
			fe_pfd = ((fe_du_failure_rate_yr**2 * fe_proof_test_yr**2)) + (3 * fe_du_failure_rate_yr * fe_dd_failure_rate_yr * fe_mttr * fe_proof_test_yr) + ((fe_ccf * fe_du_failure_rate_yr * fe_proof_test_yr) / 2)
			fe_hft = 1
			break
		else:
			print('Invalid voting')
			continue
	except:
		print('Invalid input. Please try again.')
print('Final Element PFDavg = %g' % fe_pfd)
print('Final Element HFT = %d' % fe_hft)

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

print('\nSIF: %s \nSIF Total PFDavg: %g \nSIF Total RRF: %g \nSIL: %s\n\nSensor HFT: %d \nLogic Solver HFT: %d \nFinal Element HFT: %d' %(sif_name, round(sif_pfd, 6), round(sif_rrf, 2), sil, sensor_hft, ls_hft, fe_hft))
