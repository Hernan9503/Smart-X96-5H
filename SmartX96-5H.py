#!/usr/bin/python

import minimalmodbus

rs485 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
rs485.serial.baudrate = 9600
rs485.serial.bytesize = 8
rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
rs485.serial.stopbits = 1
rs485.serial.timeout = 1
rs485.debug = False
rs485.mode = minimalmodbus.MODE_RTU
print rs485

Volts_1 = rs485.read_float(00, functioncode=4, numberOfRegisters=2)
Volts_2 = rs485.read_float(02, functioncode=4, numberOfRegisters=2)
Volts_3 = rs485.read_float(04, functioncode=4, numberOfRegisters=2)
Current_1 = rs485.read_float(06, functioncode=4, numberOfRegisters=2)
Current_2 = rs485.read_float(08, functioncode=4, numberOfRegisters=2)
Current_3 = rs485.read_float(0A, functioncode=4, numberOfRegisters=2)
Active_Power_1 = rs485.read_float(0C, functioncode=4, numberOfRegisters=2)
Active_Power_2 = rs485.read_float(0E, functioncode=4, numberOfRegisters=2)
Active_Power_3 = rs485.read_float(10, functioncode=4, numberOfRegisters=2)
Apparent_Power_1 = rs485.read_float(12, functioncode=4, numberOfRegisters=2)
Apparent_Power_2 = rs485.read_float(14, functioncode=4, numberOfRegisters=2)
Apparent_Power_3 = rs485.read_float(16, functioncode=4, numberOfRegisters=2)
Reactive_Power_1 = rs485.read_float(18, functioncode=4, numberOfRegisters=2)
Reactive_Power_2 = rs485.read_float(1A, functioncode=4, numberOfRegisters=2)
Reactive_Power_3 = rs485.read_float(1C, functioncode=4, numberOfRegisters=2)
Power_Factor_1 = rs485.read_float(1E, functioncode=4, numberOfRegisters=2)
Power_Factor_2 = rs485.read_float(20, functioncode=4, numberOfRegisters=2)
Power_Factor_3 = rs485.read_float(22, functioncode=4, numberOfRegisters=2)
Phase_Angle_1 = rs485.read_float(24, functioncode=4, numberOfRegisters=2)
Phase_Angle_2 = rs485.read_float(26, functioncode=4, numberOfRegisters=2)
Phase_Angle_3 = rs485.read_float(28, functioncode=4, numberOfRegisters=2)
Sum_of_line_currents = rs485.read_float(30, functioncode=4, numberOfRegisters=2)
Total_system_power = rs485.read_float(34, functioncode=4, numberOfRegisters=2)
Frequency_of_supply_voltages = rs485.read_float(46, functioncode=4, numberOfRegisters=2)
Total_Import_Active_Energy = rs485.read_float(48, functioncode=4, numberOfRegisters=2) 
Total_Export_Active_Energy = rs485.read_float(4A, functioncode=4, numberOfRegisters=2)
Total_Import_Reactive_Energy = rs485.read_float(4C, functioncode=4, numberOfRegisters=2)
total_Export_Reactive_Energy = rs485.read_float(4E, functioncode=4, numberOfRegisters=2)
Total_Active_Energy = rs485.read_float(56, functioncode=4, numberOfRegisters=2)
#Total_Reactive_Energy = rs485.read_float(344, functioncode=4, numberOfRegisters=2)

print 'Voltage_1: {0:.1f} Volts'.format(Volts_1)
print 'Voltage_2: {0:.1f} Volts'.format(Volts_2)
print 'Voltage_3: {0:.1f} Volts'.format(Volts_3)
print 'Current_1: {0:.1f} Amps'.format(Current_1)
print 'Current_2: {0:.1f} Amps'.format(Current_2)
print 'Current_3: {0:.1f} Amps'.format(Current_3)
print 'Active power_1: {0:.1f} Watts'.format(Active_Power_1)
print 'Active power_2: {0:.1f} Watts'.format(Active_Power_2)
print 'Active power_3: {0:.1f} Watts'.format(Active_Power_3)
print 'Apparent power_1: {0:.1f} VoltAmps'.format(Apparent_Power_1)
print 'Apparent power_2: {0:.1f} VoltAmps'.format(Apparent_Power_2)
print 'Apparent power_3: {0:.1f} VoltAmps'.format(Apparent_Power_3)
print 'Reactive power_1: {0:.1f} VAr'.format(Reactive_Power_1)
print 'Reactive power_2: {0:.1f} VAr'.format(Reactive_Power_2)
print 'Reactive power_3: {0:.1f} VAr'.format(Reactive_Power_3)
print 'Power factor_1: {0:.1f}'.format(Power_Factor_1)
print 'Power factor_2: {0:.1f}'.format(Power_Factor_2)
print 'Power factor_3: {0:.1f}'.format(Power_Factor_3)
print 'Phase angle_1: {0:.1f} Degree'.format(Phase_Angle_1)
print 'Phase angle_2: {0:.1f} Degree'.format(Phase_Angle_2)
print 'Phase angle_3: {0:.1f} Degree'.format(Phase_Angle_3)
print 'Sum of line currents: {0:.1f} Amps'.format(Sum_of_line_currents)
print 'Total system power: {0:.1f} Watts'.format(Total_system_power)
print 'Frequency of supply voltages: {0:.1f} Hz'.format(Frequency_of_supply_voltages)
print 'Total Import active energy: {0:.3f} Kwh'.format(Total_Import_Active_Energy)
print 'Total Export active energy: {0:.3f} kwh'.format(Total_Export_Active_Energy)
print 'Total Import reactive energy: {0:.3f} kvarh'.format(Total_Import_Reactive_Energy)
print 'Total Export reactive energy: {0:.3f} kvarh'.format(Total_Export_Reactive_Energy)
print 'Total active energy: {0:.3f} kwh'.format(Total_Active_Energy)

#print 'Total reactive energy: {0:.3f} kvarh'.format(Total_Reactive_Energy)
#print 'Current Yield (V*A): {0:.1f} Watt'.format(Volts * Current)
